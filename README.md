# PS2 Exercise 5 — collaboration setup

<!-- PS2_FINAL_TEAM_PLAN_START -->
## PS2 最终分工与前置顺序

本组完成第1、2、3、5题，A-E为成员占位。第1、5题沿用PS1的Conda；第2、3题使用Pixi。每人按表完成自己的分析、工程或报告部分；第2、3、5题在PR阶段统一审核和整合，不预先指定人员。最终验收均不指定人员。

### 仓库与环境

| 题目 | 小组仓库 | 环境安排 |
| --- | --- | --- |
| 第1题 | [first_repo](https://github.com/zcyMary/first_repo) | 沿用PS1的Conda，补充检查工具 |
| 第2题 | [Smoking](https://github.com/starries-creator/ps_2_ex2_smoking_is_bad) | Pixi，环境名 smoke；B先配置并验证，A-E各自安装/确认 |
| 第3题 | [NBA](https://github.com/starries-creator/ps_2_ex3_database) | 老师的Pixi，Python 3.12，nba；C先验证，A-E各自安装/确认 |
| 第5题 | [Titanic](https://github.com/starries-creator/ps1_ex4_nb_to_repo_forked) | 沿用Conda，Python 3.13.16、pandas 2.3；A-E各自激活/确认 |

### 成员分工

| 成员 | 第1题 | 第2题 | 第3题 | 第5题 |
| --- | --- | --- | --- | --- |
| A | 工具配置、全文件检查、跟进工具PR；审查忽略及类型PR | 变量分布图与解释 | 洞见①；数据库结构小题 | 筛选最终图表，撰写≤500词报告正文 |
| B | 忽略规则、CSV验证、跟进忽略PR；审查工具PR | 优先完成Pixi smoke环境、锁文件、nbstripout及环境README | 洞见②；表清单小题 | 年龄/票价分析；完善README内容并保留原项目介绍 |
| C | data_cleaner.py类型标注；协调类型PR | 年龄分组敏感性分析 | 先验证老师的nba环境、准备数据入口；打包、loader说明及安装/导入验证 | 家庭变量分析 |
| D | data_loader.py、visualizer.py类型标注；审查忽略及工具PR | 数据准备、基础统计与总体生存率（基础TODO） | 洞见③；字段小题 | 性别/舱位分析 |
| E | 验证mypy依赖、完成两问说明；审查类型PR | 按年龄分组比较吸烟与生存率，解释混杂关系 | 洞见④；日期范围小题 | 缺失值与特征可用性分析 |

### 工作边界

- NBA四个洞见选择相近复杂度；A/B/D/E各自交付SQL、分析/绘图函数、图和解释。C负责数据入口、打包及安装/导入验证。
- 第5题优先复用已有分析和图；B/C/D/E各交图及简短解释，供A筛选和写作。报告正文≤500词，不含图；B完善README并保留原项目说明及备份。
- 每人负责自己部分的代码、图和解释，并自行修正。第2、3、5题提交PR后统一审核、整合和完整复跑，不预先指定审核或整合人员。
- 环境需各自在本机安装/激活并确认可用：第2题B先配置验证，第3题C先验证教师配置，第5题沿用各自原Conda。开工前划清函数、文件及notebook修改范围；PR合并后删除对应已合并的远程和本地分支，未合并分支保留。

### 前置顺序

箭头表示先后；【并行】内的工作可同时开展。各题最后的“最终验收”不指定人员。以下为组员后续完成作业的流程。

#### 第1题：沿用Conda，三个主要PR，工具PR最后

**【并行：A工具配置｜B忽略规则｜C/D类型标注｜E依赖验证、两问初稿】→【并行：B忽略PR，由A/D审查、B跟进合并｜C/D类型PR，由A/E审查、C跟进合并】→ A同步两项结果并做全文件检查，B/C/D修复所属部分，E补全两问并交A收录 → A提交工具PR，B/D审查，A跟进合并 → 最终验收**

每条PR均需两名非作者批准。C标注data_cleaner.py；D标注data_loader.py和visualizer.py。E结合B的CSV结果与依赖验证完成两问，随A的工具PR提交。A/B/C分别负责工具/忽略/类型PR的合并跟进和已合并来源分支清理；按仓库权限执行。各人在合并后同步并安装hooks。

#### 第2题：B准备环境，各自完成分析

**B配置并验证Pixi smoke环境，A-E各自安装并确认可用 →【各自完成：A变量分布图与解释｜B锁文件、nbstripout及环境README｜C年龄分组敏感性｜D数据准备、基础统计与总体生存率｜E按年龄分组比较吸烟与生存率】 → A-E分别提交各自PR → 审核、整合并完整复跑 → 合并PR并删除已合并的远程和本地分支 → 最终验收**

D先共享准备好的数据，A/C/E再基于同一数据分析；可并行的部分同时开展。C/E先约定基础年龄分组和生存率口径。各成员在自己的clone安装hook；B负责环境配置和使用说明，每个人确认自己的本机环境。

#### 第3题NBA：C验证环境与数据，各自完成小题和洞见

**C先验证老师的Pixi nba配置，A-E各自安装并确认环境 →【各自完成：A洞见①、数据库结构小题｜B洞见②、表清单小题｜C数据入口、打包、loader说明及安装/导入验证｜D洞见③、字段小题｜E洞见④、日期范围小题】 → A-E分别提交各自PR → 审核、整合并完整复跑 → 合并PR并删除已合并的远程和本地分支 → 最终验收**

C先提供可复现的下载/建库步骤和数据库入口；A-E在本机确认数据可读后即可开展各自部分，无须等待整份warm-up或打包完成。C负责warm-up路径/连接，四位洞见作者的其余小题见流程；最终整合前完成安装/导入验证。

#### 第5题：各自确认Conda，分析后完成报告

**A-E各自激活并确认原Conda环境（缺少时安装） →【各自完成：A筛图、撰写≤500词报告｜B年龄/票价分析、完善README｜C家庭变量分析｜D性别/舱位分析｜E缺失值与特征可用性分析】 → A-E分别提交各自PR → 审核、整合并完整复跑 → 合并PR并删除已合并的远程和本地分支 → 最终验收**

优先复用已有图表，可并行的分析同时开展；B/C/D/E交齐图和简短解释后，A定稿选图与报告。B保留原项目介绍及docs/readme-history中的README备份；沿用Python 3.13.16、pandas 2.3，不另设新环境。

### 作业占位

作业占位文件和原notebook中的TODO留给对应成员完成；本次只同步分工和流程，不预填分析、答案或报告。
<!-- PS2_FINAL_TEAM_PLAN_END -->

## Start here

For PS2, use the existing PS1 Conda environment described by `environment.yml`:
`titanic`, Python 3.13.16, and pandas 2.3. Keep the original file unchanged;
remove or adapt its machine-specific `prefix` in a personal copy before using it
on another machine. Activate the environment and select its corresponding
notebook kernel. See [CONTRIBUTING.md](CONTRIBUTING.md) for collaboration rules.
The Conda setup has not been retested as part of this preparation.

<details>
<summary>Optional historical Pixi setup</summary>

The PS2 setup uses Python 3.13.16, pandas 2.3 series, and a committed
conda-forge Pixi lock file. Four platforms are
resolved: macOS Apple Silicon, macOS Intel, Linux x86-64, and Windows x86-64.
Runtime validation is performed on macOS Apple Silicon; other platforms are
dependency-resolved, not runtime-tested. Install Pixi from https://pixi.sh/ .

From the repository root:

```bash
pixi install --locked -e titanic
pixi run -e titanic jupyter
```

Use the Python kernel from that environment. Do not use a global Python or a
teammate's absolute environment path. Other CPU architectures require a team
manifest/lock update first. See [CONTRIBUTING.md](CONTRIBUTING.md) for branches,
reviews, notebook editing, and local-file rules.

</details>

## PS2 Exercise 5 — focused feature analysis

This branch (`part_b`) contributes the age and fare analysis. The concise report is in [`report.ipynb`](report.ipynb), and exported visualisations are tracked in `figures/`. It reviews the existing age/fare survival plots and adds age-band survival rates with Wilson intervals and a fare-quartile comparison stratified by passenger class.

- **Age:** survival differs across age bands, with the highest observed rate among children; 177 of 891 training passengers have missing age. Keep age as a candidate, handle missingness explicitly, and avoid overly fine age bins.
- **Fare:** survival rises across overall fare quartiles, but fare is strongly associated with passenger class (median fares: £60.29, £14.25, and £8.05 for classes 1–3). Consider fare alongside `Pclass`, then use validation to check whether it adds predictive value.
- The plots describe associations in `data/train.csv`, not causal effects. Small age/class/fare subgroups have uncertain rates.

Open `report.ipynb` with the PS1 Conda environment and select its Python kernel to read the report. The exported PNGs are already included; the original exploratory notebook remains [`Titanic_Data_Journey.ipynb`](Titanic_Data_Journey.ipynb).

## Files

- `Titanic_Data_Journey.ipynb`, `functions/`, and supplied `data/`: preserved from the PS1 repository.
- `report.ipynb`: focused report on age and fare feature selection.
- `figures/age_survival.png` and `figures/fare_survival_by_class.png`: exported report figures, tracked by Git.
- `pixi.toml` + `pixi.lock`: retained optional Pixi environment and lock file.
- `environment.yml`: the PS1 Conda environment specification used for PS2; it is not the same dependency snapshot as the optional Pixi lock.

Keep the report at 500 words or fewer, excluding graphs. Each chosen visualisation
must justify a feature-selection decision. Review existing figures and favour a
small useful selection. This branch records the age/fare contribution; integrate
other contributors’ selected analyses in the final report as the team completes them.


## Setup verification (Pixi only)

The following records the earlier Pixi setup, not a verification of the
default Conda workflow.

Verified on 2026-11-03 with Python **3.13.16** and pandas **2.3.3** on
macOS Apple Silicon, using the committed lock file.

- Both notebooks validate; `report.ipynb` remains empty.
- All existing function modules import, and the existing loader reads the supplied CSVs.
- Both existing plotting helpers render PNGs from disposable synthetic data.
- A fresh Jupyter kernel runs a temporary cell and confirms Python 3.13.16 and pandas 2.3.
- Both lock-file environments resolve Python 3.13.16 and pandas 2.3 for all four platforms.

Other platforms were dependency-resolved only, not runtime-tested. No coursework
analysis, answers, model training, or Kaggle data download was performed.

## README maintenance

The original PS1 README is preserved in
[`docs/readme-history/README_PS1_original.md`](docs/readme-history/README_PS1_original.md)
from commit `3929a5a959b1576fabbf3b3257b8367df71711ba`. The README before
Python alignment is preserved in
[`docs/readme-history/README_before_python_alignment.md`](docs/readme-history/README_before_python_alignment.md)
from commit `efdc0d4ea8642c7083a5da975142224445951c03`. Keep these backups unchanged.

The README now summarises the selected age/fare visualisations and their feature-selection implications. Preserve the original PS1 project overview, structure, usage instructions, and collaboration guidelines below. The formal report remains `report.ipynb` (at most 500 words, excluding graphs); the README does not replace it.

## Original repository instructions (retained)

The following PS1 instructions are preserved unchanged. For PS2 environment
setup, use the Conda guidance above.

# Titanic Data Journey — D100 Exercise 4

## Project Overview

This project refactors a Jupyter Notebook based on the Kaggle Titanic dataset into a more structured and maintainable Python repository.

The Jupyter Notebook remains the main entry point for presenting the analysis, while reusable functions are organised into separate Python modules.

## Repository Structure

- `Titanic_Data_Journey.ipynb` — Main notebook containing the analysis workflow.
- `functions/` — Reusable Python modules and functions.
- `data/` — Input datasets used in the analysis.
- `configs/` — Project configuration files.
- `outputs/` — Directory for generated outputs.
- `environment.yml` — Conda environment specification.
- `.github/` — GitHub-related project configuration.

## Getting Started

1. Clone the repository to your local computer.
2. Set up a compatible Python environment using the dependencies specified in `environment.yml`. The environment file contains a machine-specific `prefix` path, which may need to be removed or adjusted for your system.
3. Open `Titanic_Data_Journey.ipynb` in VS Code or Jupyter.
4. Select the appropriate Python kernel.
5. Check the dataset paths and run the notebook cells in order.

## Development and Collaboration

The project follows a modular development workflow. Reusable code is organised into Python modules, while the notebook is retained for presenting the analysis.

Contributors should create separate Git branches for their changes, open Pull Requests for review, and merge approved changes into the main branch.
