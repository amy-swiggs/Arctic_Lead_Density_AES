"""
Map functions for Antarctic altimetry analysis.

Contains functions for:
- creating a grid-cell array for polar maps
- masking land 
"""


import numpy as np
import regionmask
from pyproj import Transformer
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


def defining_grids(map_projection,map_extent,grid_spacing,grid_type):
    """
    Define centre or edge grids for polar maps.
    """

    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection=map_projection)
    ax.set_extent(map_extent, ccrs.PlateCarree())
    x_min, x_max, y_min, y_max = ax.get_extent()

    if grid_type == 'centre':
        x_grid_centre = np.arange(x_min-grid_spacing/2,x_max + grid_spacing/2, grid_spacing)
        y_grid_centre = np.arange(y_min-grid_spacing/2,y_max + grid_spacing/2, grid_spacing)
        new_x_centre, new_y_centre = np.meshgrid(x_grid_centre, y_grid_centre)
        plt.close(fig)
        return(x_grid_centre,y_grid_centre,new_x_centre,new_y_centre)
        
    elif grid_type == 'edge':
        x_grid_edge = np.arange(x_min-grid_spacing,x_max + grid_spacing, grid_spacing)
        y_grid_edge = np.arange(y_min-grid_spacing,y_max + grid_spacing, grid_spacing)
        new_x_edge, new_y_edge= np.meshgrid(x_grid_edge, y_grid_edge)
        plt.close(fig)
        return(x_grid_edge,y_grid_edge,new_x_edge,new_y_edge)

    else:
            raise ValueError(f'grid_type must be centre or edge')


def land_masking(x, y, projection):
    """
    Create boolean land mask from projected x/y coordinates.

    Parameters
    ----------
    x, y : 2D arrays
        Grid coordinates in projected CRS.
    projection : str or CRS
        Projection definition compatible with pyproj.

    Returns
    -------
    land_mask : 2D boolean array
        True where land exists.
    """

    land = regionmask.defined_regions.natural_earth_v5_0_0.land_110

    # transform x and y coordinates to lat lon
    transformer = Transformer.from_crs(projection, "EPSG:4326", always_xy=True)
    lon0, lat0 = transformer.transform(x.ravel(), y.ravel())
    # reshape back into array shape
    lon = lon0.reshape(x.shape)
    lat = lat0.reshape(x.shape)
    
    # create mask where land is nan
    mask = land.mask(lon,lat)
    land_mask = ~np.isnan(mask)
    
    # land mask can now be applied to arrays
    return(land_mask)

