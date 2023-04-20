"""
    By Henok Gashaw 
"""
# Importing Libraries
import json
import time
import pandas as pd
import Methods

CLIENT = Methods.GetHostName()
FORMAT = 'utf-8'

#For Uavs

numUavs = 10     #Change the number as desired.

PORT = Methods.PortList(numUavs)
ADDR = Methods.AddrList(CLIENT, PORT, numUavs) 

#For Protocol Message
PORT_Protocol = 9000
ADDR_Protocol = (CLIENT, PORT_Protocol)  

#csv files
#csv_filename = ['StGeorge/Height_70m_0_path_test.csv', 'StGeorge/Height_70m_1_path_test.csv']
#csv_filename = ['Trento_1_20/Trento_1_20_0_path_test.csv', 'Trento_1_20/Trento_1_20_1_path_test.csv', 'Trento_1_20/Trento_1_20_2_path_test.csv']
#csv_filename = ['valencia_90_50/valencia_90_50_0_path_test.csv', 'valencia_90_50/valencia_90_50_1_path_test.csv', 'valencia_90_50/valencia_90_50_2_path_test.csv', 'valencia_90_50/valencia_90_50_3_path_test.csv']

csv_filename = ['10UAVs/UAV_10_0_path_test.csv', '10UAVs/UAV_10_1_path_test.csv', '10UAVs/UAV_10_2_path_test.csv', '10UAVs/UAV_10_3_path_test.csv', '10UAVs/UAV_10_4_path_test.csv', '10UAVs/UAV_10_5_path_test.csv', '10UAVs/UAV_10_6_path_test.csv', '10UAVs/UAV_10_7_path_test.csv', '10UAVs/UAV_10_8_path_test.csv', '10UAVs/UAV_10_9_path_test.csv']

ClientSocket = Methods.SocketCreator()

#for Protocol message
def SendProtocolMessage():
    #print("Sending protocol messages to UAV")
    for j in range(numUavs-1):
        message = {"senderID":0,"receiverID":j,"payload":"Hello"}
        ClientSocket.sendto(json.dumps(message).encode(FORMAT), ADDR_Protocol)

#For UAV
def Send():
        df = []
        Time = []
        XYZ_DataFrame = []
        XYZ_NumPyArray = []
        for index in range(numUavs):
            df.append(pd.read_csv(csv_filename[index]))
            Time.append(Methods.TimeExtractor(df))

            XYZ_DataFrame.append = Methods.ColumnDropper(df) 
            XYZ_NumPyArray, numRows = Methods.PreProcessor(XYZ_DataFrame)
            t = -1

            for i in range(numRows): 

                x, y, z = Methods.LocationExtractor(XYZ_NumPyArray, i) 

                toSend = "{X},{Y},{Z}".format(X = round(x, 1), Y = round(y, 1), Z = round(z, 1))

                print("UAV ", str(index))
                ClientSocket.sendto(toSend.encode(FORMAT), ADDR[index])
                t = t + 1
                print(toSend)
                time.sleep(Time[t+1] - Time[t])     

SendProtocolMessage()
Send()
