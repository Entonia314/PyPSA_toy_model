import pandas as pd
import matplotlib.pyplot as plt

def plot_time_series(time_series, title, ylabel, filename):
    if isinstance(time_series, list):
        plt.figure(figsize=(10, 5))
        for series in time_series:
            plt.plot(series.index, series.values)
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
    elif isinstance(time_series, pd.Series):
        plt.figure(figsize=(10, 5))
        plt.plot(time_series.index, time_series.values)
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
    else:
        raise ValueError("time_series must be a pandas Series or a list of Series")
    