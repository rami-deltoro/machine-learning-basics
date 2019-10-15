from pandas import read_csv
from matplotlib import pyplot
import numpy


file_name = "/Users/ramideltoro/ml/diabetes.csv"
raw_data = open(file_name, 'rt')
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(file_name,names=names)

correlations = data.corr()

fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations,vmin=-1,vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)

pyplot.show()
