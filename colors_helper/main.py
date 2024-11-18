"""
color_helper.py

This module provides utilities for color manipulation and managing a centralized color palette CSV file ('good_colors.csv').

If 'good_colors.csv' is missing, it will automatically be downloaded from a specified URL.

Dependencies:
    - numpy, pandas: for numerical and data management

Functions:
    - hex_to_rgb: Converts hexadecimal color code to an RGB tuple.
    - load_colors_csv: Loads and returns the color data from 'good_colors.csv', downloading it if missing.
    - save_colors_csv: Saves updated color data back to 'good_colors.csv'.
    - add_color_with_light_counterpart: Adds a color and its light counterpart to the CSV.
    - name2rgb: Retrieves the RGB values for a color by its name.
    - name2hexcode: Retrieves the hexadecimal code for a color by its name.
    - colors: Lists all true colors in the CSV.

Authors:
- Warith Harchaoui, https://harchaoui.org/warith
- Laurent Pantanacce, https://www.linkedin.com/in/pantanacce
"""

import numpy as np
import pandas as pd
import os_helper as osh
from typing import Tuple, Union, List

# Path and URL for the color CSV file
CSV_PATH = 'good_colors.csv'
CSV_URL = 'https://harchaoui.org/warith/colors/good_colors.csv'

DF_COLORS = None


def load_colors_csv() -> pd.DataFrame:
    """
    Loads the 'good_colors.csv' file, downloading it if it does not exist.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the color data.
    """
    global DF_COLORS, CSV_URL
    if DF_COLORS is not None:
        return DF_COLORS

    with osh.temporary_filename(suffix=".csv") as temp_file:
        osh.download_file(CSV_URL, temp_file)
        DF_COLORS = pd.read_csv(temp_file)

    return DF_COLORS


def save_colors_csv(colors_df: pd.DataFrame) -> str:
    """
    Saves the given DataFrame to the 'good_colors.csv' file.

    Parameters
    ----------
    colors_df : pd.DataFrame
        DataFrame containing the color data to be saved.

    Returns
    -------
    str
        Absolute path to the saved CSV file.
    """
    global DF_COLORS, CSV_PATH
    DF_COLORS = colors_df
    DF_COLORS.to_csv(CSV_PATH, index=False)
    f = osh.relative2absolute_path(CSV_PATH)
    osh.info(f"Color data saved to {f}")
    return f


def hex_to_rgb(hex_code: str) -> Tuple[int, int, int]:
    """
    Converts a hexadecimal color code to an RGB tuple.

    Parameters
    ----------
    hex_code : str
        Hexadecimal color code in the format '#RRGGBB'.

    Returns
    -------
    Tuple[int, int, int]
        A tuple representing the RGB values of the color.
    """
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))


def add_color_with_light_counterpart(color_name: str, color_value: Union[Tuple[int, int, int], str], position: int) -> None:
    """
    Adds a color and its light counterpart to the color palette in 'good_colors.csv'.

    Parameters
    ----------
    color_name : str
        Name of the color.
    color_value : Union[Tuple[int, int, int], str]
        RGB tuple or hexadecimal color code of the color.
    position : int
        Position in the CSV where the color and its light counterpart should be inserted.
    """
    colors_df = load_colors_csv()
    r, g, b = hex_to_rgb(color_value) if isinstance(color_value, str) and color_value.startswith('#') else color_value
    light_rgb = np.clip(np.array([r, g, b]) + 70, 0, 255)  # Simple lightening effect
    hex_code = f"#{r:02X}{g:02X}{b:02X}"
    light_hex_code = f"#{light_rgb[0]:02X}{light_rgb[1]:02X}{light_rgb[2]:02X}"
    new_rows = [{"Name": color_name, "R": r, "G": g, "B": b, "Hex Code": hex_code},
                {"Name": f"Light {color_name}", "R": light_rgb[0], "G": light_rgb[1], "B": light_rgb[2], "Hex Code": light_hex_code}]
    colors_df = pd.concat([colors_df.iloc[:position], pd.DataFrame(new_rows), colors_df.iloc[position:]], ignore_index=True)
    save_colors_csv(colors_df)


def name2rgb(color_name: str) -> Tuple[int, int, int]:
    """
    Retrieves the RGB values for a color by its name.

    Parameters
    ----------
    color_name : str
        Name of the color.

    Returns
    -------
    Tuple[int, int, int]
        RGB values as a tuple.

    Raises
    ------
    ValueError
        If the color name is not found in 'good_colors.csv'.
    """
    colors_df = load_colors_csv()
    color_row = colors_df[colors_df['Name'].str.lower() == color_name.lower()]
    if color_row.empty:
        raise ValueError(f"Color '{color_name}' not found in 'good_colors.csv'.")
    return int(color_row['R'].values[0]), int(color_row['G'].values[0]), int(color_row['B'].values[0])


def name2hexcode(color_name: str) -> str:
    """
    Retrieves the hexadecimal code for a color by its name.

    Parameters
    ----------
    color_name : str
        Name of the color.

    Returns
    -------
    str
        Hexadecimal color code as a string.

    Raises
    ------
    ValueError
        If the color name is not found in 'good_colors.csv'.
    """
    colors_df = load_colors_csv()
    color_row = colors_df[colors_df['Name'].str.lower() == color_name.lower()]
    if color_row.empty:
        raise ValueError(f"Color '{color_name}' not found in 'good_colors.csv'.")
    return color_row['Hex Code'].values[0]


def colors() -> List[str]:
    """
    Lists all true colors (excluding light counterparts) in 'good_colors.csv'.

    Returns
    -------
    List[str]
        List of color names.
    """
    colors_df = load_colors_csv()
    true_colors_df = colors_df[~colors_df['Name'].str.lower().str.contains('light ')]
    return true_colors_df['Name'].tolist()
