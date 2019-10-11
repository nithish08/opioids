# coding: utf-8
"""
This module contains helper functions for data wrangling.
"""

def series2float(series):
    """Strip commas from a series' elements and casts them to floats,
    e.g. casts '1,532' to 1532.0"""

    # Want to return a new data frame, not modify original
    seriesC = series.copy()

    seriesC = seriesC.str.replace(",", "")
    seriesC = seriesC.astype(float)

    return seriesC
