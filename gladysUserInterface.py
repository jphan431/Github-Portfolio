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
	    print("Thank you for using the app. Goodbye!")
            userQuit = True
        
        #run some tests (this is part 1 of 2)
        
        elif firstChar == 't':
            runTests()
        else:
            print("ERROR:" + firstChar + "is not a valid command")

print("\n")
print("Thank you for using the Gladys West Map App!")
print("\n")
