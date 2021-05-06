import io
import gladysSatellite as satellite

"""
        Student: Anvita Kisara
        Module: gladysCompute
        Description: This module calculates the distance between the current and the destination positions given by the user.
"""

def gpsAverage(x, y):
    """

    This function will calculate the average of the coordinate's corresponding values using the gpsValue function from the 
    userInterface module. It will read the json files to find the value of the coordinate for latitude, longitude, altitude, 
    and time. Then it will compute the average of those values, which will be used to calculate the distance.

    """

    value = satellite.gpsValue(x,y,"latitude") + satellite.gpsValue(x,y,"longitude") + satellite.gpsValue(x,y,"altitude") + satellite.gpsValue(x,y,"time")

    average = value / 4
    return average

def distance(xCurrent, yCurrent, xDestination , yDestination):
    
    """

    This function will calculate the distance between the current and the destination coordinates. It calls the average function 
    from the satellite module.
    
    UserInterface module should print this out:

    print("Current       :  x=", xCurrent, "y=", yCurrent)
    print("Destination   :  x=", xDestination, "y=", yDestination)
    print("Distance      :", distance)
    
    """
    distance = (((gpsAverage(xCurrent, yCurrent))**2) + (gpsAverage(xDestination, yDestination))**2)**0.5
    return distance
