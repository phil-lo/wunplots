from pathlib import Path

from wuncolors import ColorPalette, utils
from wunplots import Plotting

palpath = Path("/Users/Philippe/quant-scape/python-projects/dev/colors/palette_example.toml")
colors = ColorPalette.from_toml(palpath, "example")

p = Plotting()

n = 1000
p.cycler_colors = utils.gradient(colors.all_colors("blue"), colors.all_colors("red"), n=n)
fig, ax = p.new(width=3, nrows=3, ncols=3)

for x in range(0, n):
    ax[0, 0].plot([x/n, x/n], [0, 1], label=x)

p.show()
