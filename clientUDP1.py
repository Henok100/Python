"""
    By Henok Gashaw 
"""
# Importing Libraries
import Methods1
import json
import time
import pandas as pd

CLIENT = Methods1.GetHostName()
FORMAT = 'utf-8'

#For Uavs

numUavs = 10     #Change the number as desired.
numRows = []
LocationList = []

PORT = Methods1.PortList(numUavs)
ADDR = Methods1.AddrList(CLIENT, PORT, numUavs) 

#For Protocol Message
PORT_Protocol = 9000
ADDR_Protocol = (CLIENT, PORT_Protocol)  

csv_filename = ['Path2/Path2_0_path_test.csv', \
                'Path2/Path2_1_path_test.csv', \
                'Path2/Path2_2_path_test.csv', \
                'Path2/Path2_3_path_test.csv', \
                'Path2/Path2_4_path_test.csv', \
                'Path2/Path2_5_path_test.csv', \
                'Path2/Path2_6_path_test.csv', \
                'Path2/Path2_7_path_test.csv', \
                'Path2/Path2_8_path_test.csv', \
                'Path2/Path2_9_path_test.csv']

ClientSocket = Methods1.SocketCreator()

XYZ_Dataframe = Methods1.DataFrameListMaker(numUavs)

Time = Methods1.TimeExtractor(pd.read_csv(csv_filename[0]))
XYZ_NumPyArray= Methods1.NumPyArrayMaker(XYZ_Dataframe, numUavs)

for i in range(numUavs):
     numRows.append(Methods1.numRows(XYZ_NumPyArray[i])) 

NUMRows = min(numRows)  #

#for Protocol message
def SendProtocolMessage():
    for j in range(numUavs-1):
        message = {"senderID":0,"receiverID":j,"payload":"Hello"}
        ClientSocket.sendto(json.dumps(message).encode(FORMAT), ADDR_Protocol)
        print("Random Message Sent")

#For UAV
def Send():
    t = -1
    for Rowindex in range(NUMRows):
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
        t = t + 1
        time.sleep(Time[t+1] - Time[t])    
Send()