"""
    By Henok Gashaw 
"""
import numpy as np
import pandas as pd
import socket
df = []
XYZ_NumPyArray = []

# csv_filename = ['_20m/_20m_0_path_test.csv', \
#                 '_20m/_20m_1_path_test.csv', \
#                 '_20m/_20m_2_path_test.csv', \
#                 '_20m/_ 20m_3_path_test.csv', \
#                 '_20m/_20m_4_path_test.csv', \
#                 '_20m/_20m_5_path_test.csv', \
#                 '_20m/_20m_6_path_test.csv', \
#                 '_20m/_20m_7_path_test.csv', \
#                 '_20m/_20m_8_path_test.csv', \
#                 '_20m/_20m_9_path_test.csv']

# csv_filename = ['_60m/_60m_0_path_test.csv', \
#                 '_60m/_60m_1_path_test.csv', \
#                 '_60m/_60m_2_path_test.csv', \
#                 '_60m/_60m_3_path_test.csv', \
#                 '_60m/_60m_4_path_test.csv', \
#                 '_60m/_60m_5_path_test.csv', \
#                 '_60m/_60m_6_path_test.csv', \
#                 '_60m/_60m_7_path_test.csv', \
#                 '_60m/_60m_8_path_test.csv', \
#                 '_60m/_60m_9_path_test.csv']

csv_filename = ['_120m/_120m_0_path_test.csv', \
                '_120m/_120m_1_path_test.csv', \
                '_120m/_120m_2_path_test.csv', \
                '_120m/_120m_3_path_test.csv', \
                '_120m/_120m_4_path_test.csv', \
                '_120m/_120m_5_path_test.csv', \
                '_120m/_120m_6_path_test.csv', \
                '_120m/_120m_7_path_test.csv', \
                '_120m/_120m_8_path_test.csv', \
                '_120m/_120m_9_path_test.csv']

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

def ColumnDropper(Dataframe):
    Dropped = Dataframe.drop(['t(s)', 'zRelative(m)', 'heading(rad)', 's(m/s)', 'a(m/s²)', 'Δd(m)', 'd(m)'], axis=1)
    return Dropped

def DataFrameListMaker(numUavs):
    for i in range(numUavs):
        temp = pd.read_csv(csv_filename[i])
        temp = ColumnDropper(temp)
        df.append(temp)
    return df

def TimeExtractor(DataFrame):
    return DataFrame['t(s)']

def PreProcessor(df):
    Location1 = df.round(1)
    Location1 = Location1.drop_duplicates(subset=['x(m)'], keep='last')
    Location1 = Location1.drop_duplicates(subset=['y(m)'], keep='last')

    Location1['x(m)'] = Location1['x(m)'] - 430100.89
    Location1['y(m)'] = Location1['y(m)'] - 4580573.60    

    Location1 = Location1.drop_duplicates(subset=['x(m)'], keep='last')
    Location1 = Location1.drop_duplicates(subset=['y(m)'], keep='last')
    
    NumPyArray = Location1.to_numpy()

    return NumPyArray

def NumPyArrayMaker(XYZ_Dataframe, numUavs):
    for i in range(numUavs):
        temp = PreProcessor(XYZ_Dataframe[i])
        XYZ_NumPyArray.append(temp)
    return XYZ_NumPyArray

def numRows(NumPyArray):
    return np.shape(NumPyArray)[0]

def LocationExtractor(NumPyArray, i):
    List = []
    List.append(NumPyArray[i][0])
    List.append(NumPyArray[i][1])
    List.append(NumPyArray[i][2])

    return List
