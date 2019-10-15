import csv
import numpy
from numpy import loadtxt
from pandas import read_csv
from pandas import set_option

file_name = "/Users/ramideltoro/ml/diabetes.csv"
raw_data = open(file_name, 'rt')
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(file_name,names=names)
print(data.shape)

peek = data.head(20)
print(peek)

shape = data.shape
print(shape)

types = data.dtypes
print(types)

set_option('display.width',100)
set_option('display.max_columns',10)
set_option('precision',3)
description = data.describe()
print(description)

class_counts = data.groupby('class').size()
print(class_counts)

correlations = data.corr(method='pearson')
print(correlations)

skew = data.skew()
print(skew)
