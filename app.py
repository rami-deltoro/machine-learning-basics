import csv
import numpy
from numpy import loadtxt
from pandas import read_csv


#Open via Python Standard library
file_name = "/Users/ramideltoro/ml/diabetes.csv"

raw_data = open(file_name, 'rt')

reader = csv.reader(raw_data, delimiter=',',quoting = csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)

#Open with Numpy

raw_data_2 = open(file_name, 'rb')
data_2 = loadtxt(raw_data_2,delimiter=",")
print(data_2.shape)

#Open with Pandas - recommended

names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data_3 = read_csv(file_name,names=names)
print(data_3.shape)
