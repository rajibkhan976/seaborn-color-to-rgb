import seaborn as sns
from matplotlib import colormaps


def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


def convert_seaborn_color_to_rgb(paletteName):
  color_pal = None
  color_pal_hex = None
  color_pal_rgb = []
  if paletteName in list(colormaps):
    try:
      color_pal = sns.color_palette(paletteName)
    except:
      print("Palette Name is not correct")
  if color_pal:
    try:
      color_pal_hex = color_pal.as_hex()
    except:
      print("Color Palette is empty")
  if color_pal_hex:
    try:
      for color in color_pal_hex:
        color_pal_rgb.append(hex_to_rgb(color.lstrip('#')))
    except:
      print("Color Palette is empty")
  return color_pal_rgb


if __name__ == "__main__":
  convert_seaborn_color_to_rgb(paletteName="")
