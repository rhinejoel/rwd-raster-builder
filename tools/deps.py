try:
    # Force GeoPandas to use Shapely instead of PyGEOS
    # In a future release, GeoPandas will switch to using Shapely by default.
    import os, glob, warnings, datacube, rasterio, folium, json
    import numpy as np
    import xarray as xr
    import geopandas as gpd
    import matplotlib.pyplot as plt
    import rioxarray as rio
    import pandas as pd

    from rasterio.merge import merge
    from rasterio.plot import show
    from shapely.geometry import Point
    from shapely.geometry import Polygon

    from scipy.ndimage import uniform_filter
    from scipy.ndimage import variance
    from skimage.filters import threshold_minimum
    from datacube.utils.geometry import Geometry

    from deafrica_tools.spatial import xr_rasterize
    from deafrica_tools.datahandling import load_ard
    from deafrica_tools.plotting import display_map, rgb
    from deafrica_tools.areaofinterest import define_area

    from typing import Literal

    from IPython.display import clear_output
    from IPython.display import display

    from tools.gdrive import GDrive

    gd = GDrive()

    from tools.mosaic import CreateMosaic

    cm = CreateMosaic()

    print("\033[32m" + "Dependencies Import Successful" + "\033[0m")
except ImportError:
    raise ImportError(
        "\033[31m"
        + "Dependencies Not Imported Successfully, Please Check New Packages Introduced And Install Manually"
        + "\033[0m"
    )