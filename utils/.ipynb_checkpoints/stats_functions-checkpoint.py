"""
Statistics functions for Antarctic sea ice lead/floe density analysis.

Contains functions for:
- RMSD
- Correlation
- Absolute Difference
"""

import numpy as np
import pandas as pd
import scipy

def absdiff(df_input1,df_input2):
    """
    Calculate absolute difference between two datasets
    
    Parameters
    ----------
    df_input1,df_input2: pd dataframe columns
        dataframe columns must have the same length
    
    Returns
    -------
    Value:
        The mean absolute difference between the two dataframe columns

    """
    mask = (~np.isnan(df_input1)) & (~np.isnan(df_input2))

    abs_diff = np.abs(df_input1[mask] - df_input2[mask])
    
    mean_abs_diff = np.nanmean(abs_diff)
    return(mean_abs_diff)

def corr_squared(df_input1,df_input2):
    """
    Calculate r squared of two datasets
    
    Parameters
    ----------
    df_input1,df_input2: pd dataframe columns
        dataframe columns must have the same length
    
    Returns
    -------
    Value:
        The r squared value of the two dataframe columns

    """
    mask = (~np.isnan(df_input1)) & (~np.isnan(df_input2))

    x = df_input1[mask]
    y = df_input2[mask]

    r = np.corrcoef(x, y)[0, 1]

    r2 = r**2
    return(r2)

def corr(df_input1,df_input2):
    """
    Calculate r of two datasets
    
    Parameters
    ----------
    df_input1,df_input2: pd dataframe columns
        dataframe columns must have the same length
    
    Returns
    -------
    Value:
        The r value of the two dataframe columns

    """
    mask = (~np.isnan(df_input1)) & (~np.isnan(df_input2))

    x = df_input1[mask]
    y = df_input2[mask]

    r = np.corrcoef(x, y)[0, 1]
    return(r)

def rmsd(df_input1,df_input2):
    """
    Calculate rmsd of two datasets
    
    Parameters
    ----------
    df_input1,df_input2: pd dataframe columns
        dataframe columns must have the same length
    
    Returns
    -------
    Value:
        The rmsd value of the two dataframe columns

    """
    mask = (~np.isnan(df_input1)) & (~np.isnan(df_input2))

    diff_squared = (df_input1[mask] - df_input2[mask])**2

    rmsd = np.sqrt(np.mean(diff_squared))
    return(rmsd)