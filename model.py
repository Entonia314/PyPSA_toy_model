import pypsa
import pandas as pd
from config import techno_eco_df

# ---------------------------
# Load time series
# ---------------------------
load = pd.read_csv("data/load_at.csv", index_col=0, parse_dates=True)
solar_cf = pd.read_csv("data/solar_cf_at.csv", index_col=0, parse_dates=True)
wind_cf = pd.read_csv("data/wind_onshore_cf_at.csv", index_col=0, parse_dates=True)

print(load.head())
print(solar_cf.head())
print(wind_cf.head())

snapshots = load.index

# ---------------------------
# Create network
# ---------------------------
n = pypsa.Network()
n.set_snapshots(snapshots)

n.add(
    "Bus",
    "AT",
    carrier="AC"
)
n.add(
    "Load",
    "AT_load",
    bus="AT",
    p_set=load["load_MW"]
)

# Add Generators and Storage
n.add(
    "Generator",
    "AT_solar",
    bus="AT",
    carrier="solar",
    p_nom_extendable=True,
    capital_cost=techno_eco_df.loc["solar", "capex_eur_per_mw"],
    marginal_cost=techno_eco_df.loc["solar", "marginal_cost_eur_per_mwh"],
    efficiency=techno_eco_df.loc["solar", "efficiency"],
    p_max_pu=solar_cf["solar_cf"]
)
n.add(
    "Generator",
    "AT_wind_onshore",
    bus="AT",
    carrier="wind_onshore",
    p_nom_extendable=True,
    capital_cost=techno_eco_df.loc["wind_onshore", "capex_eur_per_mw"],
    marginal_cost=techno_eco_df.loc["wind_onshore", "marginal_cost_eur_per_mwh"],
    efficiency=techno_eco_df.loc["wind_onshore", "efficiency"],
    p_max_pu=wind_cf["wind_cf"]
)
n.add(
    "Generator",
    "AT_gas",
    bus="AT",
    carrier="gas",
    p_nom_extendable=True,
    capital_cost=techno_eco_df.loc["gas", "capex_eur_per_mw"],
    marginal_cost=techno_eco_df.loc["gas", "marginal_cost_eur_per_mwh"],
    efficiency=techno_eco_df.loc["gas", "efficiency"]
)
n.add(
    "Store",
    "AT_battery_energy",
    bus="AT",
    carrier="battery",
    e_nom_extendable=True,
    capital_cost=techno_eco_df.loc["battery_energy", "capex_eur_per_mw"],
    e_cyclic=True
)

# Add Charge/Discharge components for the battery
n.add(
    "Link",
    "AT_battery_charge",
    bus0="AT",
    bus1="AT",
    carrier="battery",
    p_nom_extendable=True,
    capital_cost=techno_eco_df.loc["battery_power", "capex_eur_per_mw"],
    efficiency=techno_eco_df.loc["battery_power", "efficiency"]
)
n.add(
    "Link",
    "AT_battery_discharge",
    bus0="AT",
    bus1="AT",
    carrier="battery",
    p_nom_extendable=True,
    capital_cost=0,
    efficiency=techno_eco_df.loc["battery_power", "efficiency"]
)

# Add CO2 constraint
n.add(
    "GlobalConstraint",
    "co2_limit",
    sense="<=",
    constant=5e6, # tCO2/a
)
n.carriers.loc["gas", "co2_emissions"] = 0.19 # tCO2/MWh_th

# Solve the optimization problem
n.optimize(
    n.snapshots,
    solver_name="highs",
)

# Print results
print(n.generators.p_nom_opt)
print(n.stores.e_nom_opt)

n.generators_t.p.plot()
