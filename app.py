from pandas import read_csv
from matplotlib import pyplot
from pandas.plotting import scatter_matrix

file_name = "/Users/ramideltoro/ml/diabetes.csv"
raw_data = open(file_name, 'rt')
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(file_name,names=names)

scatter_matrix(data)
pyplot.show()