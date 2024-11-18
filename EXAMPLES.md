# Examples

## List Colors and their RGB Values
```python
import colors_helper as ch

# List colors with their RGB values
for color in ch.colors():
    r, g, b = ch.name2rgb(color)
    print(f"{color}: R={r}, G={g}, B={b}")
```

_Example Output:_

```
Red: R=255, G=59, B=48
Orange: R=255, G=149, B=0
...
```


## Get Hex Code for Colors
```python
import colors_helper as ch

# List colors with their hex codes
for color in ch.colors():
    hex_code = ch.name2hexcode(color)
    print(f"{color}: {hex_code}")
```

_Example Output:_
```
Red: #FF3B30
Orange: #FF9500
...
```



## Convert Hexadecimal to RGB
```python
import colors_helper as ch

# Convert a hex code to RGB
hex_code = "#FFCC00"
rgb_tuple = ch.hex_to_rgb(hex_code)
print(f"RGB values for {hex_code}: {rgb_tuple}")
```

_Example Output:_
```
RGB values for #FFCC00: (255, 204, 0)
```



## Add a Color with its Light Counterpart
```python
import colors_helper as ch

# Add a new color and its lighter counterpart
ch.add_color_with_light_counterpart("MyBlue", "#0044CC", 5)
```

_Functionality:_
- Adds "MyBlue" and "Light MyBlue" to the color palette.


## Load and Save Colors Palette
```python
import colors_helper as ch

# Load the current color palette
colors_df = ch.load_colors_csv()
print(colors_df.head())

# Save modifications back to the CSV
colors_file = ch.save_colors_csv(colors_df)
```



## Test Integration with DataFrames
```python
import pandas as pd
import colors_helper as ch

# Create a DataFrame with color names and RGB values
colors = ch.colors()
data = [{"Color Name": color, "RGB": ch.name2rgb(color)} for color in colors]
df = pd.DataFrame(data)
print(df.head())
```



## Generate a Light Palette
```python
import colors_helper as ch

# Generate a palette of lighter colors
colors = ch.colors()
light_palette = {
        f"Light {color}": ch.hex_to_rgb(f"#{hex(r+70)[2:].zfill(2)}{hex(g+70)[2:].zfill(2)}{hex(b+70)[2:].zfill(2)}") 
        for color in colors for r, g, b in [ch.name2rgb(color)]
}

print(light_palette)
```

_Example Output:_
```
{
    'Light Red': (20, 88, 23),
    'Light Orange': (20, 93, 180),
    ...
}
```
