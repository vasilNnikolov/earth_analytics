import os
from traceback import print_tb
from matplotlib import tight_layout
from matplotlib.axes import Axes
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import rioxarray as rxr

# Earthpy is an earthlab package to work with spatial data
import earthpy as et
import earthpy.plot as ep


def challenge_2():
    lidar_dtm_path = os.path.join("data", "colorado-flood",
                                "spatial",
                                "boulder-leehill-rd",
                                "pre-flood",
                                "lidar",
                                "pre_DTM.tif")

    lidar_dtm = rxr.open_rasterio(lidar_dtm_path, masked=True)

    lidar_dtm_path_post_flood = os.path.join("data", "colorado-flood", "spatial",
                                            "boulder-leehill-rd", "post-flood", "lidar",
                                            "post_DTM.tif")

    lidar_dtm_post_flood = rxr.open_rasterio(lidar_dtm_path_post_flood, masked=True)

    def plot_before_flood():
        ep.plot_bands(lidar_dtm,
                    scale=False,
                    cmap='Greys',
                    title="Lidar Digital Terrain Model")


    def plot_after_flood():
        ep.plot_bands(lidar_dtm_post_flood,
                    scale=False,
                    cmap='Greys',
                    title="Lidar Digital Terrain Model post flood")
    
    plot_after_flood()
    
def challenge_3():
    # et.data.get_data(url="https://ndownloader.figshare.com/files/23070791")
    # os.chdir(os.path.join(et.io.HOME, 'earth_analytics', '1_intro', 'data'))

    naip_pre_fire_path = os.path.join("data", "earthpy-downloads",
                                  "naip-before-after",
                                  "pre-fire",
                                  "crop",
                                  "m_3910505_nw_13_1_20150919_crop.tif")
    

    naip_pre_fire = rxr.open_rasterio(naip_pre_fire_path)
    # ep.plot_bands(naip_pre_fire)
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, tight_layout=True)
    ep.plot_rgb(naip_pre_fire.values, ax=ax1)

    naip_post_fire_path = os.path.join("data", "earthpy-downloads",
                                   "naip-before-after",
                                   "post-fire",
                                   "crop",
                                   "m_3910505_nw_13_1_20170902_crop.tif")

    naip_post_fire = rxr.open_rasterio(naip_post_fire_path)
    ep.plot_rgb(naip_post_fire.values, ax=ax2)
    plt.show()

if __name__ == "__main__":
    challenge_3()