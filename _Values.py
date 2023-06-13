import pandas as pd
import numpy as np

# Load the CSV data
data = pd.read_csv('UAVtoUAVDense/FSP.csv')
data1 = data[' 120m']

# Calculate quartiles, median and interquartile range
quartiles = np.percentile(data1, [25, 50, 75])
#iqr = quartiles[2] - quartiles[0]

# Calculate the upper and lower bounds
#upper_bound = quartiles[2] + 1.5 * iqr
#lower_bound = quartiles[0] - 1.5 * iqr

# Print the 5 values for boxplot
print("Minimum value: ", data1.min())
print("Lower quartile: ", quartiles[0])
print("Median: ", quartiles[1])
print("Upper quartile: ", quartiles[2])
print("Maximum value: ", data1.max())
# print("Interquartile range: ", iqr)
# print("Upper bound: ", upper_bound)
# print("Lower bound: ", lower_bound)