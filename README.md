# D100 Problem Set 2, Exercise 5 · Titanic feature selection

[Read the final report](report.ipynb) · [Browse the exported figures](figures/)

Which passenger characteristics are worth considering for survival prediction? We reviewed the PS1 exploratory notebook and chose five figures to justify which features to keep, how to represent them, and where missing data limit their use.

## What the figures show

| Figure | What it tells us about feature selection |
| --- | --- |
| [Sex and passenger class](figures/q5_01_sex_class.png) | Survival differs across sex and class groups. Both are baseline candidates, and the contrasts motivate testing their interaction. |
| [Fare](figures/q5_02_fare_class.png) | The overall fare gradient and the separately calculated within-class quartiles answer different questions. Evaluate whether `Fare` adds predictive value alongside `Pclass`. |
| [Age](figures/q5_03_age.png) | Children had the highest observed survival. Consider a flexible age effect and handle missing ages explicitly. |
| [Family size](figures/q5_04_family.png) | Passengers in recorded family groups of two to four had the highest observed survival. The grouped feature is a candidate, with greater uncertainty in the smaller large-family group. |
| [Missingness and cabin availability](figures/q5_05_missingness.png) | `Cabin` is missing for about 77% of training rows. An indicator for recorded cabin information is worth evaluating alongside `Pclass`, since cabin availability varies by class. |

Survival comparisons use the 891 labelled rows in `data/train.csv`. The 418 unlabelled rows in `data/test.csv` are used only to compare input availability. The figures show observed associations. Any incremental predictive value should be evaluated on held-out data.

## Clone and reproduce

The commands below use Conda and a POSIX shell. The clean-clone check used macOS on Apple Silicon with Python 3.13.16 and pandas 2.3.3. The CSV files are included in the repository.

```sh
git clone https://github.com/starries-creator/ps1_ex4_nb_to_repo_forked.git
cd ps1_ex4_nb_to_repo_forked

setup_dir=$(mktemp -d)
sed '/^prefix:/d' environment.yml > "$setup_dir/environment.yml"
conda env create --prefix "$setup_dir/titanic" --file "$setup_dir/environment.yml"
conda install --yes --prefix "$setup_dir/titanic" nbconvert
conda run --prefix "$setup_dir/titanic" python -m ipykernel install \
  --prefix "$setup_dir/titanic" --name titanic-ex5

MPLBACKEND=Agg conda run --prefix "$setup_dir/titanic" \
  python -m scripts.render_q5_figures --output figures
conda run --prefix "$setup_dir/titanic" python -m nbconvert \
  --to notebook --execute --ExecutePreprocessor.kernel_name=titanic-ex5 \
  --output-dir "$setup_dir" report.ipynb
```

The setup uses a temporary copy of `environment.yml` without its machine-specific `prefix`. `nbconvert` is added for command-line execution. The plotting command regenerates the five PNGs under `figures/`, and the final command writes an executed copy to `$setup_dir/report.ipynb`. For interactive use, open `report.ipynb` in a Jupyter-compatible editor and select the Python interpreter from `$setup_dir/titanic`.

## PS1 project and repository layout

- [Titanic_Data_Journey.ipynb](Titanic_Data_Journey.ipynb) is the original exploratory workflow refactored in PS1. It reads the supplied CSVs and uses the reusable modules in [`functions/`](functions/).
- [scripts/render_q5_figures.py](scripts/render_q5_figures.py) reads the repository data and exports the five PS2 figures used by `report.ipynb`.
- [`docs/readme-history/`](docs/readme-history/) preserves the [original PS1 README](docs/readme-history/README_PS1_original.md) and the earlier setup documentation. [CONTRIBUTING.md](CONTRIBUTING.md) describes the team's Git workflow.
