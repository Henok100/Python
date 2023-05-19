"""
    By Henok Gashaw 
"""
# Importing Libraries
import Method
import json
import time
import pandas as pd

CLIENT = Method.GetHostName()
FORMAT = 'utf-8'

#For UAVs

numUavs = 10     #Change the number as desired.
numRows = []
LocationList = []

PORT = Method.PortList(numUavs)
ADDR = Method.AddrList(CLIENT, PORT, numUavs) 

#For Protocol Message
PORT_Protocol = 9000
ADDR_Protocol = (CLIENT, PORT_Protocol)  

csv_filename = ['_20m/_20m_0_path_test.csv', \
                '_20m/_20m_1_path_test.csv', \
                '_20m/_20m_2_path_test.csv', \
                '_20m/_20m_3_path_test.csv', \
                '_20m/_20m_4_path_test.csv', \
                '_20m/_20m_5_path_test.csv', \
                '_20m/_20m_6_path_test.csv', \
                '_20m/_20m_7_path_test.csv', \
                '_20m/_20m_8_path_test.csv', \
                '_20m/_20m_9_path_test.csv']

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

# csv_filename = ['_120m/_120m_0_path_test.csv', \
#                 '_120m/_120m_1_path_test.csv', \
#                 '_120m/_120m_2_path_test.csv', \
#                 '_120m/_120m_3_path_test.csv', \
#                 '_120m/_120m_4_path_test.csv', \
#                 '_120m/_120m_5_path_test.csv', \
#                 '_120m/_120m_6_path_test.csv', \
#                 '_120m/_120m_7_path_test.csv', \
#                 '_120m/_120m_8_path_test.csv', \
#                 '_120m/_120m_9_path_test.csv']

ClientSocket = Method.SocketCreator()

XYZ_Dataframe = Method.DataFrameListMaker(numUavs)

Time = Method.TimeExtractor(pd.read_csv(csv_filename[0]))
XYZ_NumPyArray= Method.NumPyArrayMaker(XYZ_Dataframe, numUavs)

for i in range(numUavs):
     numRows.append(Method.numRows(XYZ_NumPyArray[i])) 

NUMRows = min(numRows)  #

#for Protocol message
def SendProtocolMessage():
    for j in range(numUavs-1):
        message = {"senderID":0,"receiverID":j,"payload":"Hello"}
        ClientSocket.sendto(json.dumps(message).encode(FORMAT), ADDR_Protocol)
        #print("Random Message Sent")

#For UAV
def Send():
    t = -1
    counter = 1;
    for Rowindex in range(NUMRows):
        if(counter % 3 == 0):
            SendProtocolMessage()
        
        for UAVindex in range(numUavs):
            temp = XYZ_NumPyArray[UAVindex] 
            x = temp[Rowindex][0]
            y = temp[Rowindex][1]
            z = temp[Rowindex][2]

            toSend = "{X},{Y},{Z}".format(X = round(x, 1), Y = round(y, 1), Z = round(z, 1))
            print(toSend)
            print("UAV ", str(UAVindex))
            ClientSocket.sendto(toSend.encode(FORMAT), ADDR[UAVindex])
        counter = counter + 1
        t = t + 1
        time.sleep(Time[t+1] - Time[t])    
Send()