import numpy as np
import socket

def PortList(numUavs):
    PORT = []
    for i in range(numUavs):
        PORT.append(8000 + i)
    
    return PORT

def AddrList(Client, Port, numUavs):
    ADDR = []
    for i in range(numUavs):
        ADDR.append((Client, Port[i]))
    
    return ADDR

def GetHostName():
    return socket.gethostbyname(socket.gethostname())

def SocketCreator():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def TimeExtractor(DataFrame):
    return DataFrame['t(s)']

def ColumnDropper(Dataframe):
    Dropped = Dataframe.drop(['t(s)', 'zRelative(m)', 'heading(rad)', 's(m/s)', 'a(m/s²)', 'Δd(m)', 'd(m)'], axis=1)
    return Dropped

def PreProcessor(df):
    Location1 = df.round(1)
    Location1 = Location1.drop_duplicates(subset=['x(m)'], keep='last')
    Location1 = Location1.drop_duplicates(subset=['y(m)'], keep='last')
    #Location1['x(m)'] = Location1['x(m)'] - 324167.13     #St George
    #Location1['y(m)'] = Location1['y(m)'] - 1282269.61
    
    Location1['x(m)'] = Location1['x(m)'] - 664011.13     #Treneto_1
    Location1['y(m)'] = Location1['y(m)'] - 5104328.61
    
    #Location1['x(m)'] = Location1['x(m)'] - 725516.45      #Valencia_1
    #Location1['y(m)'] = Location1['y(m)'] - 4370538.51

    #Location1['x(m)'] = Location1['x(m)'] - 324824.91      #Valencia_1
    #Location1['y(m)'] = Location1['y(m)'] - 1282292.25
    
    Location1 = Location1.drop_duplicates(subset=['x(m)'], keep='last')
    Location1 = Location1.drop_duplicates(subset=['y(m)'], keep='last')
    
    NumPyArray = Location1.to_numpy()

    numRows = np.shape(NumPyArray)[0]

    return NumPyArray, numRows

def LocationExtractor(NumPyArray, i):
    x = NumPyArray[i][0]
    y = NumPyArray[i][1]
    z = NumPyArray[i][2]

    return x, y, z