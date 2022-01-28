import os
import pandas as pd
import matplotlib.pyplot as plt

def temperatures():
    def plot_temperature(df: pd.DataFrame, location):
        fig, axis = plt.subplots(1, 1)
        fig.suptitle(f"{location} max temperature, F")
        df["Year"] = pd.Series([int(date/100) for date in df["Date"]])
        df.plot(x="Year", y="Value", ax=axis)
        axis.set_ylabel("Max temperature, F")
        
        plt.show()

    miami_data_url = "https://www.ncdc.noaa.gov/cag/city/time-series/USW00012839-tmax-12-12-1895-2020.csv"
    seattle_data_url = "https://www.ncdc.noaa.gov/cag/city/time-series/USW00013895-tmax-1-5-1895-2020.csv"

    miami_data = pd.read_csv(miami_data_url, skiprows=3, na_values=-99)
    seattle_data = pd.read_csv(seattle_data_url, skiprows=3, na_values=-99)

    plot_temperature(miami_data, "Miami")
    plot_temperature(seattle_data, "Seattle")

def co2_data():
    # import urllib.request
    filename = "co2-emissions-barrow.csv"
    # greenhouse_gas_url = "ftp://aftp.cmdl.noaa.gov/data/trace_gases/co2/in-situ/surface/brw/co2_brw_surface-insitu_1_ccgg_MonthlyData.txt"

    # urllib.request.urlretrieve(url=greenhouse_gas_url, filename=filename)
    brw_data = pd.read_csv(filename, delimiter=" ", skiprows=149, na_values=-99.99)
    brw_data_clean = brw_data[brw_data["value"] > 0]
    fig, ax = plt.subplots()
    fig.suptitle("CO2 levels in Barrow, AK")
    brw_data_clean.plot(x="time_decimal", y="value", ax=ax)

    plt.show()


if __name__ == "__main__":
    co2_data()



