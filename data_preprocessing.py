import pandas as pd
from config import DATA_PATH, COUNTRY_CODE, LOAD_COLUMN, SOLAR_COLUMN, WIND_COLUMN, YEAR_FILTER

data = pd.read_csv(DATA_PATH, index_col=0, parse_dates=True)
print(data.columns)

# Filter for columns that start with 'AT_'
at_data = data[[col for col in data.columns if col.startswith(COUNTRY_CODE)]]
print(at_data.columns)

# Use only data where index year is 2020
at_data_year = at_data[at_data.index.year == YEAR_FILTER]

# Make index timezone-naive (needed for pypsa)
at_data_year.index = at_data_year.index.tz_localize(None)

# Prepare individual time series
load_at = at_data_year[LOAD_COLUMN].rename("load_MW").fillna(0)
solar_cf_at = at_data_year[SOLAR_COLUMN].rename("solar_cf").fillna(0)
wind_onshore_cf_at = at_data_year[WIND_COLUMN].rename("wind_cf").fillna(0)

# Save to CSV files
load_at.to_csv("data/load_at.csv")
solar_cf_at.to_csv("data/solar_cf_at.csv")
wind_onshore_cf_at.to_csv("data/wind_onshore_cf_at.csv")