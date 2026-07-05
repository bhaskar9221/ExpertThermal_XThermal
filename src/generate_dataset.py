import sys
sys.path.append('../src')
from heat_sink import calculate_heat_sink
import itertools
import numpy as np
import pandas as pd
import os

TDP_vals = np.linspace(30, 250, 20)
V_air_vals = np.linspace(0.5, 15, 20)
k_tim_vals = np.linspace(1, 12, 20)


data = []

for TDP, V_air, k_tim in itertools.product(TDP_vals, V_air_vals, k_tim_vals):
    R_Total, T_j = calculate_heat_sink(TDP, V_air, k_tim)
    data.append([TDP, V_air, k_tim, R_Total, T_j])


df = pd.DataFrame(data, columns=['TDP_W', 'V_air_ms', 'k_tim_WmK', 'R_total_CW', 'T_junction_C'])
os.makedirs('data/processed', exist_ok=True)
df.to_csv('data/processed/grid_sweep.csv', index=False)
print(f'Dataset saved with {len(df)} rows.')
print(df.describe())