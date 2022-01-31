import os

import matplotlib.pyplot as plt
import geopandas as gpd
import earthpy as et

def challenge_1():
    coastlines_path = os.path.join("data", "earthpy-downloads",
                                "ne_50m_coastline",
                                "ne_50m_coastline.shp")

    coastlines = gpd.read_file(coastlines_path)
    # print(coastlines.head())

    populated_places_path = os.path.join("data", "earthpy-downloads",
                                        "ne_50m_populated_places_simple",
                                        "ne_50m_populated_places_simple.shp")

    cities = gpd.read_file(populated_places_path)

    fig, ax = plt.subplots()

    coastlines.plot(ax=ax)
    cities.plot(ax=ax)

    plt.show()

def challenge_2():
    coastlines_path = os.path.join("data", "earthpy-downloads",
                                "ne_50m_coastline",
                                "ne_50m_coastline.shp")

    coastlines = gpd.read_file(coastlines_path)
    # print(coastlines.head())

    populated_places_path = os.path.join("data", "earthpy-downloads",
                                        "ne_50m_populated_places_simple",
                                        "ne_50m_populated_places_simple.shp")

    cities = gpd.read_file(populated_places_path)

    countries_path = os.path.join("data", "earthpy-downloads",
                              "ne_50m_admin_0_countries", 
                              "ne_50m_admin_0_countries.shp")
    
    countries = gpd.read_file(countries_path)

    fig, ax = plt.subplots()

    countries.plot(ax=ax, color='white',  edgecolor='red')
    coastlines.plot(ax=ax, color='darkblue')
    cities.plot(ax=ax, color='green')
    ax.set_title("Coaslines, cities and borders")
    plt.show()

def challenge_3():
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    coastlines_path = os.path.join("data", "earthpy-downloads",
                                "ne_50m_coastline",
                                "ne_50m_coastline.shp")

    coastlines = gpd.read_file(coastlines_path)
    # print(coastlines.head())

    populated_places_path = os.path.join("data", "earthpy-downloads",
                                        "ne_50m_populated_places_simple",
                                        "ne_50m_populated_places_simple.shp")

    cities = gpd.read_file(populated_places_path)

    countries_path = os.path.join("data", "earthpy-downloads",
                              "ne_50m_admin_0_countries", 
                              "ne_50m_admin_0_countries.shp")
    
    countries = gpd.read_file(countries_path)

    f, ax1 = plt.subplots(figsize=(10, 6))

    divider = make_axes_locatable(ax1)
    cax = divider.append_axes("right",
                            size="5%",
                            pad=0.1)

    countries.plot(ax=ax1, color='white',  edgecolor='red')
    coastlines.plot(ax=ax1, color='darkblue')
    
    cities.plot(column='pop_max',
                legend=True,
                ax=ax1,
                cax=cax, scheme='quantiles')
    
    plt.show()

def bonus_challenge():
    coastlines_path = os.path.join("data", "earthpy-downloads",
                                "ne_50m_coastline",
                                "ne_50m_coastline.shp")

    coastlines = gpd.read_file(coastlines_path)
    # print(coastlines.head())

    populated_places_path = os.path.join("data", "earthpy-downloads",
                                        "ne_50m_populated_places_simple",
                                        "ne_50m_populated_places_simple.shp")

    cities = gpd.read_file(populated_places_path)

    countries_path = os.path.join("data", "earthpy-downloads",
                              "ne_50m_admin_0_countries", 
                              "ne_50m_admin_0_countries.shp")
    
    countries = gpd.read_file(countries_path)

    f, ax1 = plt.subplots(figsize=(10, 6))

    french_boundary = countries.loc[countries["SOVEREIGNT"] == "United States of America"]
    french_boundary.plot(ax=ax1)
    plt.show()
    
    plt.show()
if __name__ == "__main__":
    bonus_challenge()