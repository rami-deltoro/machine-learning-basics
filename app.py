from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import Normalizer

file_name = "/Users/ramideltoro/ml/diabetes.csv"
raw_data = open(file_name, 'rt')
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(file_name,names=names)

data_array = data.values


#split array to input & output

input_array = data_array[:,0:8]
output_array = data_array[:,8]

scaler = Normalizer().fit(input_array)

rescaled_input_array = scaler.transform(input_array)

set_printoptions(precision=3)

print(rescaled_input_array[0:5,:])