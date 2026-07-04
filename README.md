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
Correlation & Sensitivity Analysis
            │
            ▼
Train ML Surrogate Models
            │
            ▼
Model Evaluation
(MAE • RMSE • R²)
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

At least two regression models are trained and compared using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

A comparative evaluation is provided in the accompanying report.

---


## Notes

This repository is intended solely for the Expert Thermal / XThermal AI/ML Hiring Assessment.

The provided heat sink calculation model and supporting documents remain the intellectual property of Expert Thermal / XThermal.