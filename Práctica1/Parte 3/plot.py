import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

def read_players(file="output-hadoop.txt"):
	with open(file, 'r') as f:
		lines = f.readlines()
		result = {}
		remove_elems = ["[", "]", ","]
		for line in lines:
			for elem in remove_elems:
				line = line.replace(elem, "")

			line = line.replace(" ", "\t")
			elements = line.split("\t")

			result[elements[0]] = [int(elements[1]), int(elements[2])]
			
		return result
    
def plot_normal(mu, var, color):
	sigma = math.sqrt(var)
	x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
	plt.plot(x, stats.norm.pdf(x, mu, sigma), color)


data = read_players()
colors = ["r", "b", "g", "y", "orange"]
for team, c in zip(data.values(), colors):
	print(team)
	plot_normal(team[0], team[1], c)
plt.show()
plt.savefig('foo.png')