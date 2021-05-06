import io


import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userlogin


"""	
		Student: Kim Truong
		Module: gladysUserInterface
		Description: This is module does ... 
"""

def runTests():
  
    """
        tests some module functions
  
    """
    print("running a few tests")

    average = compute.gpsAverage(4, 5)
    print("average =", average)
    print("Hello!")

def start():
   
    """
        logs the user in, and runs the app
    """
   
    userName = userlogin.login()
    runApp(userName)

def runApp(userName):
   
    """
        runs the app
   
    """
    #loop until user type q
    
    userQuit = False
    while(not userQuit):

        print("--Welcome to the Gladys West Map App--")
        print("Type t to run tests or q to quit")
        print()

        # get first character of input
        
        userInput = input("Enter a command:")
        lowerInput = userInput.lower()
        firstChar = lowerInput[0:1]
        
        # menu choices , use a switch-like -if-elif control structure
        # quit
        
        if firstChar == 'q':
        	userQuit = True
        
        #run some tests (this is part 1 of 2)
        
        elif firstChar == 't':
        	runTests()
	
	#set current position
	
	elif firstChar == 'c':
		print("You are now entering your current position.")
		xCurrent = -1
		while 0 > xCurrent or 99 < xCurrent:
			print("Please input a valid x-coordinate (0-99)")
			xCurrent = int(input("Enter x-coordinate: "))
		yCurrent = -1
		while 0 > yCurrent or 99 < yCurrent:
			print("Please input a valid y-coordinate (0-99)")
			yCurrent = int(input("Enter y-coordinate: "))
		print("Current position has been set.")
		return xCurrent and yCurrent
	
	#set destination position
	
	elif firstChar == 'd':
		print("You are now entering your destination position.")
		xDestination = -1
		while 0 > xDestination or 99 < xDestination:
			print("Please input a valid x-coordinate (0-99)")
			xDestination = int(input("Enter x-coordinate: "))
		yCurrent = -1
		while 0 > yDestination or 99 < yDestination:
			print("Please input a valid y-coordinate (0-99)")
			yDestination = int(input("Enter y-coordinate: "))
		print("Destination position has been set.")
		return xDestination and yDestination
	
	#map route
	
	elif firstChar == 'm':
		distance(xCurrent, yCurrent, xDestination , yDestination)
		print("Distance: " + distance)
		
        else:
            print("ERROR:" + firstChar + "is not a valid command")

print("\n")
print("Thank you for using the Gladys West Map App!")
print("\n")
