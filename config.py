# Config file for hardcoding parameters

import pandas as pd
import numpy as np

# Data preprocessing parameters
DATA_PATH = "data/time_series_60min_singleindex.csv"
COUNTRY_CODE = "AT"
LOAD_COLUMN = f"{COUNTRY_CODE}_load_actual_entsoe_transparency"
SOLAR_COLUMN = f"{COUNTRY_CODE}_solar_generation_actual"
WIND_COLUMN = f"{COUNTRY_CODE}_wind_onshore_generation_actual"
YEAR_FILTER = 2020

# Techno-economic parameters
techno_eco_df = pd.DataFrame({
    "capex_eur_per_mw": {"solar": 50000, "wind_onshore": 70000, "gas": 80000, "battery_power": 40000, "battery_energy": 20000},
    "marginal_cost_eur_per_mwh": {"solar": 0, "wind_onshore": 0, "gas": 50, "battery_power": 0, "battery_energy": np.nan},
    "efficiency": {"solar": 1, "wind_onshore": 1, "gas": 0.39, "battery_power": np.nan, "battery_energy": 0.9}
})