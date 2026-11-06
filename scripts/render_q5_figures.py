"""Make exploratory draft figures from the repo's supplied Titanic CSVs."""
from pathlib import Path
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from functions.data_loader import load_data
from functions.feature_eng import create_family_size
from functions.family_processing import create_family_type

p=argparse.ArgumentParser()
p.add_argument('--output',type=Path,required=True)
a=p.parse_args(); a.output.mkdir(parents=True,exist_ok=True)
train=load_data('data/train.csv'); test=load_data('data/test.csv')
assert len(train)==891 and len(test)==418 and 'Survived' not in test
assert train['Survived'].isin([0,1]).all() and train.PassengerId.is_unique
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'bold','figure.facecolor':'white'})

# Survival proportions use labelled training data only.
fig, ax=plt.subplots(figsize=(9.5,5.7))
summary=train.groupby(['Pclass','Sex'])['Survived'].agg(['sum','count','mean'])
x=np.arange(3); width=.33
for sex,offset,color in [('female',-width/2,'#2a7580'),('male',width/2,'#d37a55')]:
 s=summary.xs(sex,level='Sex').reindex([1,2,3])
 ax.bar(x+offset,s['mean'],width,label=sex.capitalize(),color=color)
 for xx,(_,row) in zip(x+offset,s.iterrows()):
  ax.text(xx,row['mean']+.025,f"{row['mean']:.0%}\nn={int(row['count'])}",ha='center',va='bottom',fontsize=9)
ax.set_xticks(x,['1st','2nd','3rd']); ax.set_ylim(0,1.12); ax.yaxis.set_major_formatter(PercentFormatter(1)); ax.set_ylabel('Survived / passengers in group');ax.set_xlabel('Passenger class');ax.set_title('Survival differs by sex and passenger class',loc='left',fontsize=15); ax.legend(frameon=False,ncol=2,loc='upper right'); ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True)
fig.text(.12,.01,'Labelled training set only (n=891). Rates are descriptive; group sizes shown.',fontsize=9,color='#555');fig.tight_layout(rect=(0,.06,1,1));fig.savefig(a.output/'q5_01_sex_class.png',dpi=180,bbox_inches='tight');plt.close(fig)

family=create_family_type(create_family_size(train)); s=family.groupby('Family Type')['Survived'].agg(['sum','count','mean']).reindex(['Single','Small','Large'])
assert s['count'].sum()==len(train)
fig,ax=plt.subplots(figsize=(8.5,5.4)); bars=ax.bar(['No recorded\nrelatives (1)','Small (2–4)','Large (5+)'],s['mean'],color=['#7e9e9b','#2a7580','#d37a55'],width=.55)
for bar,(_,row) in zip(bars,s.iterrows()): ax.text(bar.get_x()+bar.get_width()/2,row['mean']+.025,f"{row['mean']:.1%}\nn={int(row['count'])}",ha='center',fontsize=10)
ax.set_ylim(0,.75);ax.yaxis.set_major_formatter(PercentFormatter(1));ax.set_ylabel('Survived / passengers in group');ax.set_xlabel('Family size, including passenger');ax.set_title('Survival varies with recorded family size',loc='left',fontsize=15);ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True)
fig.text(.12,.01,'Training only. Family size = SibSp + Parch + 1; groups are unadjusted.',fontsize=9,color='#555');fig.tight_layout(rect=(0,.06,1,1));fig.savefig(a.output/'q5_04_family.png',dpi=180,bbox_inches='tight');plt.close(fig)

features=['Cabin','Age','Embarked','Fare']; x=np.arange(len(features)); width=.34
fig,(ax, cabin_ax)=plt.subplots(1,2,figsize=(14,5.5),gridspec_kw={'width_ratios':[1.4,1]})
for data,offset,color,label in [(train,-width/2,'#2a7580','Training (n=891)'),(test,width/2,'#d37a55','Test (n=418)')]:
 n=data[features].isna().sum(); vals=n/len(data)
 ax.bar(x+offset,vals,width,color=color,label=label)
 for xx,v,k in zip(x+offset,vals,n): ax.text(xx,v+.018,f'{v:.1%}\n({k})',ha='center',fontsize=9)
ax.set_xticks(x,features);ax.set_ylim(0,1);ax.yaxis.set_major_formatter(PercentFormatter(1));ax.set_ylabel('Missing / rows in dataset');ax.set_title('Feature availability differs across train and test',loc='left',fontsize=15);ax.legend(frameon=False,ncol=2,loc='upper right');ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True)
cabin=train.groupby(train['Cabin'].notna())['Survived'].agg(['sum','count','mean']).reindex([False,True])
assert cabin['count'].sum()==len(train)
bars=cabin_ax.bar(['Missing','Recorded'],cabin['mean'],color=['#d37a55','#2a7580'],width=.55)
for bar,(_,row) in zip(bars,cabin.iterrows()):
 cabin_ax.text(bar.get_x()+bar.get_width()/2,row['mean']+.03,f"{row['mean']:.1%}\n{int(row['sum'])}/{int(row['count'])}",ha='center',fontsize=10)
cabin_ax.set_ylim(0,1);cabin_ax.yaxis.set_major_formatter(PercentFormatter(1));cabin_ax.set_ylabel('Survived / training passengers');cabin_ax.set_xlabel('Cabin availability');cabin_ax.set_title('Survival by Cabin availability',loc='left',fontsize=15);cabin_ax.grid(axis='y',alpha=.18);cabin_ax.set_axisbelow(True)
fig.text(.08,.01,'Survival uses labelled training data only. Test is used only for input availability.',fontsize=9,color='#555');fig.tight_layout(rect=(0,.06,1,1));fig.savefig(a.output/'q5_05_missingness.png',dpi=180,bbox_inches='tight');plt.close(fig)
print('sex/class\n',summary);print('family\n',s);print('missing train\n',train[features].isna().sum());print('missing test\n',test[features].isna().sum())

# Age and fare plots adapted from B’s earlier part_b notebook.
df = train.copy()
# Age survival rates by age band, with approximate 95% binomial intervals.
age_bins = [0, 12, 18, 35, 60, 100]
age_labels = ['0–12', '13–18', '19–35', '36–60', '61+']
df['Age band'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, include_lowest=True)
age_stats = df.dropna(subset=['Age']).groupby('Age band', observed=False)['Survived'].agg(['mean', 'count'])
fig, ax = plt.subplots(figsize=(8.5, 4.6))
x = np.arange(len(age_stats)); rate = age_stats['mean'].to_numpy(); n = age_stats['count'].to_numpy()
se = np.sqrt(rate * (1-rate) / n)
ax.bar(x, rate, color='#4C78A8', width=.68)
ax.errorbar(x, rate, yerr=1.96*se, fmt='none', ecolor='#243746', capsize=4, lw=1.3)
for i, (v, count) in enumerate(zip(rate, n)):
    ax.text(i, min(v + 1.96*se[i] + .035, .97), f'n={count}', ha='center', va='bottom', fontsize=9)
ax.set_xticks(x, age_stats.index.astype(str)); ax.set_ylim(0, 1.08)
ax.set_ylabel('Observed survival rate'); ax.set_xlabel('Age (years)')
ax.set_title('Survival varied by age, especially for children', loc='left', weight='bold')
ax.text(0, -.23, 'Bars show survival proportion; whiskers show approximate 95% binomial intervals. Age missing for 19.9% of training rows.', transform=ax.transAxes, fontsize=8.5, color='#555')
fig.tight_layout(); fig.savefig(a.output / 'q5_03_age.png', dpi=180, bbox_inches='tight'); plt.close(fig)

# Fare quartiles calculated within Pclass to inspect the association beyond class mix.
fig, axes = plt.subplots(1, 3, figsize=(12, 4.3), sharey=True)
for cls, ax, color in zip([1, 2, 3], axes, ['#4C78A8', '#F58518', '#54A24B']):
    sub = df.loc[df['Pclass'] == cls].copy()
    sub['Fare quartile'] = pd.qcut(sub['Fare'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'], duplicates='drop')
    stats = sub.groupby('Fare quartile', observed=False)['Survived'].agg(['mean', 'count']).dropna()
    xx = np.arange(len(stats)); rr = stats['mean'].to_numpy(); nn = stats['count'].to_numpy()
    ss = np.sqrt(rr * (1-rr) / nn)
    ax.errorbar(xx, rr, yerr=1.96*ss, color=color, marker='o', lw=2, capsize=3)
    for i, (v, count) in enumerate(zip(rr, nn)):
        ax.annotate(f'n={count}', (i, v), xytext=(0, 8), textcoords='offset points', ha='center', fontsize=8)
    ax.set_xticks(xx, stats.index.astype(str)); ax.set_title(f'Pclass {cls}', weight='bold')
    ax.set_xlabel('Fare quartile within class'); ax.set_ylim(0, 1.08)
axes[0].set_ylabel('Observed survival rate')
fig.suptitle('Fare adds context, but its survival pattern depends on class', x=.08, ha='left', weight='bold', y=1.03)
fig.text(.08, -.03, 'Quartiles are calculated separately within each passenger class; whiskers show approximate 95% binomial intervals.', fontsize=8.5, color='#555')
fig.tight_layout(); fig.savefig(a.output / 'q5_02_fare_class.png', dpi=180, bbox_inches='tight'); plt.close(fig)
