
import os
from turtle import home

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import earthpy as et

def get_data():
    et.data.get_data(url="https://opendata.arcgis.com/datasets/955e7a0f52474b60a9866950daf10acb_0.geojson")

def main():
    # Creating a home directory
    home_dir = os.path.join(et.io.HOME,'earth-analytics-parent', 'earth-analytics',
                            'data', 'earthpy-downloads')
    if not os.path.isdir(home_dir):
        os.makedirs(home_dir)

    # Set your working directory
    os.chdir(os.path.join(et.io.HOME, 'earth-analytics-parent',
                        'earth-analytics',
                        'data',
                        'earthpy-downloads'))

    city_path = "City_of_Boulder_City_Limits.geojson" 
    city = gpd.read_file(city_path)
    f, ax = plt.subplots()
    city.boundary.plot(ax=ax)
    plt.show()
    


if __name__ == "__main__":
    main()