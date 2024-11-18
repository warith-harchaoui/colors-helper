"""
Colors Helper

This module provides utilities for color manipulation, including conversions between RGB and wavelength,
generating light counterparts of colors, and managing a centralized color palette CSV file ('good_colors.csv').

If 'good_colors.csv' is missing, it will automatically be downloaded from a specified URL.

Functions:
    - hex_to_rgb: Converts hexadecimal color code to an RGB tuple.
    - load_colors_csv: Loads and returns the color data from 'good_colors.csv', downloading it if missing.
    - save_colors_csv: Saves updated color data back to 'good_colors.csv'.
    - add_color_with_light_counterpart: Adds a color and its light counterpart to the CSV.
    - name2rgb: Retrieves the RGB values for a color by its name.
    - name2hexcode: Retrieves the hexadecimal code for a color by its name.
    - colors: Lists all true colors in the CSV in increasing order of wavelength.

Authors:
- Warith Harchaoui, https://harchaoui.org/warith
"""

from .main import (
    hex_to_rgb,
    load_colors_csv,
    save_colors_csv,
    add_color_with_light_counterpart,
    name2rgb,
    name2hexcode,
    colors
)

__all__ = [
    "hex_to_rgb",
    "load_colors_csv",
    "save_colors_csv",
    "add_color_with_light_counterpart",
    "name2rgb",
    "name2hexcode",
    "colors"
]
