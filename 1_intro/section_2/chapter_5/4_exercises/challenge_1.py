import os
from turtle import home

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import earthpy as et

def get_data():
    et.data.get_data(url="https://opendata.arcgis.com/datasets/175425c25d8849b58feb89483ef02961_1.csv")

def main():
    # Creating a home directory
    home_dir = os.path.join(et.io.HOME, 'earth-analytics',
                            'data', 'earthpy-downloads')
    if not os.path.isdir(home_dir):
        os.makedirs(home_dir)

    # Set your working directory
    os.chdir(os.path.join(et.io.HOME,
                        'earth-analytics',
                        'data',
                        'earthpy-downloads'))

    print(home_dir)

if __name__ == "__main__":
    # wont do this challenge, dataset is not available online
    get_data()
