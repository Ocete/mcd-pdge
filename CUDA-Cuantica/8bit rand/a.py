import numpy as np
import matplotlib.pyplot as plt
import random
from collections import defaultdict

light_blue = '#4EFFEF'
light_orange = '#F6AE2D'

x = np.arange(start=1, stop=257)
y = []
with open("output.txt") as f:
    for line in f.readlines():
        y.append(int(line))

y = np.array(y) / 8000
expected = 1/256

def plot_numbers(x, y, title, file_name):
    plt.bar(x, y, color=light_blue)
    plt.axhline(expected, color=light_orange)

    plt.xlim(1, 256)
    plt.ylabel('Probability of measure')
    plt.xlabel('Number')
    plt.title(title)
    plt.savefig(file_name)
    #plt.show()

plot_numbers(x, y, '8bit randomizer using a quantum computer', '../figures/barplot_quantum.png')

random.seed(123)
nums = [ random.randrange(1, 257) for _ in range(8000) ]
ys_map = defaultdict(int)
for i in nums:
    ys_map[i] += 1
y = np.array([ ys_map[i] for i in range(1, 257) ]) / 8000
plot_numbers(x, y, '8bit randomizer using scipy', '../figures/barplot_scipy.png')
   

