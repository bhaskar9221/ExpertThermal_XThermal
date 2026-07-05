Hiring Assingment For AI/ML Intern Role at ExpertThermal_XThermal

# Expert Thermal / XThermal AI/ML Assessment

This repository contains my submission for the **Expert Thermal / XThermal AI/ML Hiring Assessment**.
The objective of this assessment is to generate simulation data from a physics-based heat sink model, develop machine learning surrogate models for thermal prediction, analyze parameter sensitivity, and propose AI-driven features for engineering software workflows.

---

## Project Objectives
- Understand and extend the provided heat sink thermal model.
- Generate a dataset through parameter sweeps.
- Train machine learning surrogate models to predict:
  - Total Thermal Resistance
  - Junction Temperature
- Compare multiple regression models using standard evaluation metrics.
- Perform correlation and sensitivity analysis.
- Discuss potential AI/ML applications within an engineering software platform.

---

## Repository Structure

```
.
├── assets/                    # Original assessment files (PDFs, base script)
├── data/
│   ├── raw/                   # (reserved for raw/unprocessed data)
│   └── processed/             # Generated sweep dataset + analysis outputs
│       ├── grid_sweep.csv
│       ├── model_evaluation.csv
│       └── correlation_matrix.csv
├── models/                    # (reserved for saved model artifacts)
├── notebooks/
│   └── Task1_ModellingAssessment.ipynb   # Main analysis notebook
├── reports/
│   ├── answers.md             # Written responses (Tasks 2-4)
│   ├── assessment_report.md   # Summary report
│   └── figures/
├── src/
│   ├── heat_sink.py           # Core physics model (refactored into a function)
│   ├── generate_dataset.py    # Parameter sweep -> CSV
│   ├── train_models.py        # Model training + evaluation
│   ├── analysis.py            # Correlation / sensitivity analysis
│   └── utils.py
├── requirements.txt
└── README.md
```

---

## How to Run

1. Create the environment and install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Generate the dataset:
   ```
   python src/generate_dataset.py
   ```
   This writes `data/processed/grid_sweep.csv`.
3. Open and run `notebooks/Task1_ModellingAssessment.ipynb` top to bottom. It loads the generated CSV, trains both models, and reproduces all evaluation metrics, correlation analysis, and plots.

Note: the notebook uses relative paths (`../data/processed/...`) and expects to be run from inside the `notebooks/` folder, as launched by Jupyter.

---

## Workflow

```
Physics-Based Heat Sink Model
            │
            ▼
Parameter Sweep
(TDP, Air Velocity, TIM Conductivity)
            │
            ▼
Generated Dataset (CSV)
            │
            ▼
Exploratory Data Analysis
            │
            ▼
Train ML Surrogate Models
            │
            ▼
Model Evaluation
(MAE • RMSE • R²)
            │
            ▼
Correlation & Sensitivity Analysis
            │
            ▼
Final Report & Discussion
```

---

## Input Parameters

The following parameters are varied during the parameter sweep:

| Parameter | Range |
|-----------|------:|
| Thermal Design Power (TDP) | 30 – 250 W |
| Air Velocity | 0.5 – 15 m/s |
| TIM Thermal Conductivity | 1 – 12 W/m·K |

All remaining heat sink geometry and material properties are kept constant unless otherwise specified.

---

## Predicted Outputs

The surrogate models predict:
- Total Thermal Resistance (°C/W)
- Junction Temperature (°C)

---

## Machine Learning

Two regression models are trained and compared:

- **Decision Tree** — used as a baseline. Captures the nonlinear relationships in the underlying physics (cube-root Nusselt term, 1/k_tim term) without manual feature engineering, but is prone to overfitting on its own.
- **Random Forest** — an ensemble of decision trees that averages over many trees to reduce the overfitting seen in a single tree, while retaining the ability to model nonlinear, non-additive relationships.

Both are evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Results Summary

| Model | Target | MAE | RMSE | R² |
|---|---|---:|---:|---:|
| Decision Tree | R_total | 0.00136 | 0.00251 | 0.9942 |
| Decision Tree | T_junction | 0.191 | 0.410 | 0.9996 |
| Random Forest | R_total | 0.00065 | 0.00179 | 0.9970 |
| Random Forest | T_junction | 0.091 | 0.281 | 0.9998 |

Random Forest outperforms the single Decision Tree on both targets across every metric. The Decision Tree shows a small overfitting gap (train R²=1.0 vs. test R²≈0.994–0.9996) that Random Forest reduces by averaging over many trees.

### Sensitivity Analysis

Both the correlation analysis and Random Forest feature importances agree on the dominant drivers:
- **Total Thermal Resistance** is driven almost entirely by **Air Velocity** (correlation ≈ -0.80, RF importance ≈ 92%).
- **Junction Temperature** is driven almost entirely by **TDP** (correlation ≈ 0.97, RF importance ≈ 94%).
- **TIM Thermal Conductivity** has a secondary but real effect on Total Thermal Resistance (~8–22%), and negligible direct effect on Junction Temperature.

A full discussion, including assumptions and limitations, is provided in `reports/assessment_report.md`.

---

## Notes

This repository is intended solely for the Expert Thermal / XThermal AI/ML Hiring Assessment.
The provided heat sink calculation model and supporting documents remain the intellectual property of Expert Thermal / XThermal.