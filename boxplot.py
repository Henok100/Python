import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

files = ['UAVtoUAVDense/FSP.csv', 'UAVtoUAVDense/TRG.csv', 'UAVtoUAVDense/LNS.csv', 'UAVtoUAVDense/RF.csv', 'UAVtoUAVDense/NF.csv']

# Read the CSV file into a pandas DataFrame
for i in range(5):
    data = pd.read_csv(files[i])


    # Extract the header row as a list
    headers = list(data.columns)

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Create a box plot of the data
    ax.boxplot(data)

    # Set the y-axis tick formatter to display values as percent
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
    plt.xticks(range(1, len(headers) + 1), headers)

    # Add axis labels and a title to the plot
    plt.xlabel('FreeSpacePropagation')
    plt.ylabel('PDR(%)')
    plt.title('Packet Delivery Ratio')

    # Display the plot
    plt.show()