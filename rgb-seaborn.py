import seaborn as sns

color_pal = sns.color_palette()
color_pal_hex = color_pal.as_hex()
color_pal_rgb = []


def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


for color in color_pal_hex:
    color_pal_rgb.append(hex_to_rgb(color.lstrip('#')))

print(color_pal_rgb)
