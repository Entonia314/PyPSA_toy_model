# Simple PyPSA Model to test and play with

Structure:

PYPSA_TOY_MODEL/
├── data/
│   ├── time_series_60min_singleindex.csv # from OPSD
│   ├── load_at.csv
│   ├── solar_cf_at.csv
│   └── wind_onshore_cf_at.csv
├── model.py
├── data_preprocessing.py
├── config.py
└── environment.yml / pyproject.toml

## Get started

Set up venv according to pyproject.toml. Download time series data from OPSD: https://data.open-power-system-data.org/time_series/.

Run data_preprocessing.py to get separate csv files.
Check and configure techno-economic parameters in config.py.
Run model.py to build and optimize model.