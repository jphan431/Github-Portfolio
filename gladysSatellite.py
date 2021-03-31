import io
import json

"""
	Student: Nethan Tiu
	Module: gladysSatellite
	Description: This module works with the underlying data structures and file read operations …
"""


def readSat(sat, pathToJSONDataFiles):
	"""
		reads satellite data from a json file
		Students do NOT need to change the readSat function.
	"""
	
	# data file path
	fileName = sat + "-satellite.json"
	filePath = pathToJSONDataFiles + "/" + fileName

	# open the file
	try:
		fileHandle = open(filePath)
	except IOError:
		print("ERROR: Unable to open the file " + filePath)
		raise IOError

	# print("filePath = ", filePath)

	# read the file
	data = json.load(fileHandle)

	return data


def gpsValue(x, y, sat):
	"""
		determines gps value depending on x and y
	"""

	pathToJSONDataFiles = "C:/Users/netha/GitHub/gladys-map-project-1/json-files"

	# read the satellite data
	data = readSat(sat, pathToJSONDataFiles)

	"""
		delete the remaining code *in this function* and replace it with
		your own code. add more code to do what the assignment asks of you.

		tip: here is where students need to look through the data variable
		read from the satellites and find a matching x,y to return the value.
		to understand better, open and look at the json satellite data in
		vs code.
	"""
	value = 473

	return value
