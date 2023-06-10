import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

files = ['UAVtoUAVDense/FSP.csv', 'UAVtoUAVDense/TRG.csv', 'UAVtoUAVDense/LNS.csv', 'UAVtoUAVDense/RF.csv', 'UAVtoUAVDense/NF.csv']
data = []
xlabel = ['FreeSpacePathLoss', 'TwoRayGroundReflection', 'LogNormalShadowing', 'RicianFading', 'NakagamiFading']

# Read the CSV file into a pandas DataFrame
for i in range(5):
    data.append(pd.read_csv(files[i]))

# Create a figure and axis object
fig, axs = plt.subplots(nrows=1, ncols=5, figsize=(15, 15))

# Extract the header row as a list
headers = list(data[0].columns)


# Create a box plot of the data
for i, ax in enumerate(axs):
    ax.boxplot(data[i])
    ax.set_xticklabels(headers)

# Add space between subplots
fig.subplots_adjust(wspace=0.4)

# Set the y-axis tick formatter to display values as percent
for i, ax in enumerate(axs):
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    ax.set_xlabel(xlabel[i]).set_color('blue')
    ax.set_ylabel('Packet Delivery Ratio ').set_color('blue')

#Super Title
plt.suptitle("UAV-to-UAV Performance in Urban Environment", fontsize=16).set_color('blue')

# Display the plot
plt.show()