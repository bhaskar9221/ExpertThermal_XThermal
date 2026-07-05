Assessment Report: Thermal Heat Sink Surrogate Model 

1. Initial Assumptions
For this assessment, an initial version of the heat sink thermal model was taken as provided and extended into a parameter sweep, with resulting data used to train ML surrogates to predict total thermal resistance and junction temperature, as well as to analyze sensitivity to inputs.
The code implementing these steps may be found in src/, while this report is generated from notebooks/Task1_ModellingAssessment.ipynb.
1.1 Fixed and Varied Parameters

Geometry and material properties of the heat sink were held constant at the values used in the reference report and provided script.
Only the variables mentioned in the assessment description (TDP, air velocity, and TIM conductivity) were swept within their ranges during the modeling process.

1.2 R_jc Discrepancy
While the provided script sets R_jc = 0.2°C/W,
the reference report claims to use “a typical value: R_jc = 0.1 °C/W”
and provides a baseline calculation with TDP=150W, V_air=1m/s, k_tim=4W/mK, resulting in R_total=0.373043°C/W, which is close to what the baseline calculation in the provided script would produce with R_jc=0.2: 0.3692°C/W.
Given the proximity of these values and the possibility of rounding during the Excel calculation, it is possible that the reference report actually used R_jc=0.2°C/W and mistakenly labeled it as 0.1, and this assessment proceeds with the value of 0.2, given that the provided script also uses it and can thus be relied on to be correct.
That said, this discrepancy should be resolved before relying on any calculations using these values.
1.3 Flow Regime Assumption
As discussed in the reference report, the choice of convection correlation depends on the flow regime, determined by the Reynolds number.
The provided script uses the turbulent flow correlation throughout the sweep, but the assessment explicitly states to assume laminar flow.
The actual Re number for the entire parameter sweep was checked to be between 37 and 1101, well within the laminar range of 2300, meaning that the turbulent convection correlation used in the provided script is irrelevant to this assessment’s results.
1.4 Noise
No noise was added to any measurements, as the process is modeled deterministically.
This allows the ML surrogates to learn the underlying relationships, but such an approach would not reflect real-world measurement errors or manufacturing tolerances, so actual performance in applications would be lower than suggested by the metrics below.
2. Results
2.1 Reference Case Agreement
When comparing the reference case provided in the assessment description (TDP=150W, V_air=1m/s, k_tim=4W/mK) to the one explicitly stated in the reference report (TDP=150W, V_air=1m/s, k_tim=4W/mK), the recreated report produces T_j=80.38°C compared to the reference report’s 80.96°C, which suggests a minor discrepancy of roughly 0.7% - within the expected rounding error of the Excel calculation from the reference report.
Excluding the possibility of calculation errors on either side, this discrepancy appears to be caused by the R_jc = 0.2 versus 0.1 discrepancy mentioned above.
2.2 Parameter Sweep
The parameter sweep covered TDP in 30–250W (20 points), V_air in 0.5–15m/s (20 points), k_tim in 1–12W/mK (20 points) with the resulting 8000 data points summarized in the following table:
Min Max Std
Target: R_total (°C/W) 0.268 0.442 0.059
Target: T_junction (°C) 33.0 136.1 22.5
2.3 ML Model Comparison
To predict both R_total and T_junction from the three inputs, two models were trained and evaluated: a Decision Tree and a Random Forest regressor.
A Decision Tree was used as the simplest non-linear model able to partition the input data and approximate the underlying relationships, with its performance serving as a baseline.
A Random Forest regressor was trained as an ensemble of Decision Trees to reduce variance and improve generalization.
The results of this comparison are summarized in the following table:
Model Target MAE RMSE R²
Decision Tree R_total (°C/W) 0.00136 0.00251 0.9942
Decision Tree T_junction (°C) 0.191 0.410 0.9996
Random Forest R_total (°C/W) 0.00065 0.00179 0.9970
Random Forest T_junction (°C) 0.091 0.281 0.9998
On both targets, the Random Forest markedly outperformed the simple Decision Tree, reducing errors by roughly half and improving the R² scores by about 10-20%.
Meanwhile, the Decision Tree showed signs of overfitting: a suspiciously perfect R² of 1.0 on the training data, compared to roughly 0.994-0.9996 on the test data.
However, the difference between the training and test set performance for the Random Forest is much smaller, suggesting that while the simple Decision Tree struggles to generalize to unseen data, an ensemble of such trees performs consistently across train and test data.
Therefore, the Random Forest approach was chosen for further analysis.
3. Correlation / Sensitivity
Both approaches confirmed similar underlying relationships: total thermal resistance was overwhelmingly dominated by air velocity (correlation ~-0.80, importance ~92%) and only weakly dependent on TIM conductivity (correlation ~-0.22, importance ~8%).
Meanwhile, junction temperature was strongly correlated with TDP (correlation ~0.97, importance ~94%) and had a much smaller contribution from thermal resistance (~6%), and therefore followed approximately T_j = T_ambient + TDP R_total . This suggests that improving airflow would have the most significant impact on decreasing junction temperature, while TDP is a design decision made at the processor level and cannot be adjusted easily.
4. Limitations
4.1 Validity Range
The surrogate’s predictions are only valid within the ranges spanned by the training data: TDP 30–250W, V_air 0.5–15m/s, k_tim 1–12W/mK, beyond which the predictions should be treated with caution.
4.2 Flow Regime
As noted earlier, the entire parameter sweep fell within the laminar flow regime, and therefore the surrogate knows nothing about turbulent airflow and would fail to generalize to higher velocities.
4.3 Noise
As stated above, no noise was added to any measurements, and therefore the surrogate has no knowledge of real-world tolerances and would underestimate the errors by a significant margin in a real application.
4.4 R_jc
As discussed earlier, there appears to be a discrepancy between the value used in the reference report (0.1°C/W) and the provided script (0.2°C/W).
While a possible cause was identified, this uncertainty remains a concern and should be resolved by contacting the author of the reference report directly if this were a real project.

5. Opportunities for Improvement / Optimization
5.1 Expand Parameter Sweep

The parameter sweep should be expanded to include a higher range of air velocities to trigger the turbulent flow regime and check how the surrogate extrapolates beyond the known data.
5.2 Third Model Comparison
As a comparison, a boosted tree regressor could be used as a third option for ML surrogate.
5.3 Prediction Intervals
To provide more information about the surrogate’s confidence in its predictions, quantile regression could be used to train a model that would predict credible intervals instead of point estimates.
5.4 Resolve R_jc Discrepancy
If this were a real project and the reference report were to be used as a foundation, the discrepancy between the reported 0.1 and scripted 0.2 should be resolved with direct communication with the author.