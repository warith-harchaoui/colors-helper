import colors_helper as ch
import pandas as pd

def test_hex_to_rgb():
    assert ch.hex_to_rgb("#FF0000") == (255, 0, 0), "Hex to RGB for red failed"
    assert ch.hex_to_rgb("#00FF00") == (0, 255, 0), "Hex to RGB for green failed"
    assert ch.hex_to_rgb("#0000FF") == (0, 0, 255), "Hex to RGB for blue failed"


def test_load_colors_csv():
    colors_df = ch.load_colors_csv()
    assert isinstance(colors_df, pd.DataFrame), "Colors CSV did not load as DataFrame"
    assert not colors_df.empty, "Loaded DataFrame is empty"

def test_name2rgb():
    rgb = ch.name2rgb("red")
    assert rgb == (255, 59, 48), "RGB values for 'red' did not match expected output"
    
def test_name2hexcode():
    hex_code = ch.name2hexcode("red")
    assert hex_code == "#FF3B30", "Hex code for 'Test Color' did not match expected output"

def test_colors():
    colors_list = ch.colors()
    assert isinstance(colors_list, list), "Colors function did not return a list"
    assert len(colors_list) > 0, "Colors list is empty"
