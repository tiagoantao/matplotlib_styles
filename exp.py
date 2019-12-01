from functools import partial
from math import pow
import sys

import numpy as np
from matplotlib import style
from matplotlib.pyplot import subplots

sys.path.insert(0, '')

from my_styles import apply_style

style.use('bmh')
apply_style('low_info')

TIME = 120

moore_growth = list(map(partial(pow, 2), np.arange(TIME) / 24))
edholm_growth = list(map(partial(pow, 2), np.arange(TIME) / 18))
growth_ratio = list(map(lambda x: x[0]/x[1], zip(edholm_growth, moore_growth)))
fig, axs = subplots(1, 1, squeeze=False, figsize=(8, 4))


ax = axs[0, 0]
ax.plot(moore_growth, label="Moore's law")
ax.plot(edholm_growth, label="Edholm's law")

ax.set_title("Comparing Moore and Edholm's laws")
ax.set_xlabel('Month')
ax.set_xlim(left=0, right=TIME)
ax.set_ylabel('Proportion to month 0', fontsize='xx-large')
ax.set_ylim(bottom=1)
ax.legend(loc='center left')

ax2 = ax.twinx()

ax2.plot(growth_ratio, 'k-.', label="Ratio between Edholm and Moore's laws", lw=1)
ax2.set_ylabel('Ratio')
ax2.legend()

fig.tight_layout(pad=0.5)
fig.savefig('edholm_moore_ratio.png')
