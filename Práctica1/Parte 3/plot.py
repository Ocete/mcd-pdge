import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
import pylab

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
    
def plot_normal(mu, std, color):
	x = np.linspace(10, 40, 100)
	plt.plot(x, stats.norm.pdf(x, mu, std))

def color_generator(n_colors):
	cm = pylab.get_cmap('gist_rainbow')
	return (cm(1.*i/n_colors) for i in range(n_colors))

data = read_players()
color_gen = color_generator(len(data))

plt.figure(figsize=(18, 10))
for team_stats in data.values():
	plot_normal(team_stats[0], team_stats[1], next(color_gen))
plt.legend(data.keys())
plt.title("Comparativa de edades en los distintos equipos")
plt.savefig('spark.png')
plt.show()