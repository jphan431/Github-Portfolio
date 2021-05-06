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
	for row in data
		if row[0] == x and row[1] == y
			return row[2]
	value = row[2]

	return value
