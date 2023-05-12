import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pyproj import Proj
import math 
import random

def init_df():
	#filename = getFileName()
	filename = "BarcelonaPart2.csv"
	print("reading shapeFile")
	df = pd.read_csv(filename, delimiter=';')
	df = df.sort_values(by=['osm_id'])
	return df

def getFileName():
	Tk().withdraw() 
	return askopenfilename()


def print_header(f):
	f.write("<environment>\n")
	f.write("<material id=\"1\" resistivity=\"100\" relativePermittivity=\"4.5\" relativePermeability=\"1\" /> <!-- concrete-->\n")

def print_footer(f):
	f.write("\n</environment>")
	

def get_building(buildingId):
	building = df.loc[df['osm_id'] == buildingId]

	duplicatedRows = building[building.duplicated(['startX','startY','endX','endY'])]
	building = building[~building.isin(duplicatedRows)].dropna()
	building = building.reset_index(drop=True)
	return building

def make_wall(wall, Height):
	# in omnet a wall is rotated in its center
	# so starting from the start and end point
	# we must calculate its length (widht always 1)
	# the angle of rotation
	# and the displacement (offset) due to the rotation to correct
	start_UTMx, start_UTMy = converter(wall['startX'], wall['startY'])
	end_UTMx, end_UTMy = converter(wall['endX'], wall['endY'])

	x1 = start_UTMx - centerX
	y1 = start_UTMy - centerY
	x2 = end_UTMx - centerX
	y2 = end_UTMy - centerY

	dx = x2 -x1
	dy = y2 - y1
	length= math.sqrt(dx**2 + dy**2)
	angle = -math.atan2(dy,dx) #omnet rotation is clockwise, normaly counter clockwise

	offsetX = -(1-math.cos(angle))*length/2
	offsetY = -math.sin(angle)*length/2  #up in omnet is a smaller Y coordinate

	posx = round((x1+ offsetX)*100)/100
	posy = round((y1+ offsetY)*100)/100
	angle = -round(math.degrees(angle)*100)/100 #in omnet positive angle is clockwise
	length = round((length)*100)/100

	print_wall(posx,posy,angle,length,1,Height)




def print_wall(posx,posy,angle,length,width,height):
	f.write("<object ")
	f.write("position=\"min " + str(-posx) + " " + str(-posy) + " 0\" ")
	f.write("orientation=\" " + str(angle) + " 0 0\" ")
	f.write("shape=\"cuboid ")
	f.write(" " + str(-length) + " " + str(width) + " " + str(height))
	f.write("\" material=\"1\" /> \n")




if __name__ == "__main__":

	df = init_df()
	converter = Proj(proj='utm', zone=31, ellps='WGS84', preserve_units=False)
	centerX = 431054.33
	centerY = 4583290.85
	f = open("BarcelonaPart2.xml", "w")
	print_header(f)
	3
	buildingIds = df['osm_id'].drop_duplicates()
	for buildingId in buildingIds:
		building = get_building(buildingId)
		Height = random.randint(20, 140)
		for index, wall in building.iterrows():
			make_wall(wall, Height)

	print_footer(f)
	f.close()
	print("done!\n")
