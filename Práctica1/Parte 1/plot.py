import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Python code to
# demonstrate readlines()


def get_most_frequent(file,k = 10):
	with open(file,'r') as f:
		lines = f.readlines()
		dict = {}
		for l in lines:
			elements = l.split("\t")
			dict[elements[0]] = int(elements[1])
			
		sorted_vals = sorted(dict.items(), key=lambda x : -x[1])[0:k]
		ret = {}
		for a in sorted_vals:
			ret[a[0]] = a[1]
			
		return ret
    
    
mf_t1 = get_most_frequent('test1')
mf_t2 = get_most_frequent('test2')

df = pd.DataFrame(mf_t1,index=['i',])
df = df.append(mf_t2,ignore_index = True).transpose()

ax = df.plot.bar(rot=0,alpha=0.8)

ax.legend(["Sin preprocesado","Con preprocesado"])
fig = ax.get_figure()
fig.savefig("barplot.pdf")
plt.show()



mf_t1 = get_most_frequent('test1',k=1000)
mf_t2 = get_most_frequent('test2',k=1000)

print("Número de veces que aparece la palabra")
print("\t el")
print("\t\t - Sin preprocesado {}".format(mf_t1['el']))
print("\t\t - Con preprocesado {}".format(mf_t2['el']))


print("\t dijo")
print("\t\t - Sin preprocesado {}".format(mf_t1['dijo']))
print("\t\t - Con preprocesado {}".format(mf_t2['dijo']))









