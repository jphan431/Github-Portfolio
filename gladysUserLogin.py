import io

"""
	Student: Jim Phan
	Module: gladysUserLogin
	Description: This module does …
"""


def login():
	username="JimPhan@yahoo.com"
	password="test1" 

	
	success= 0
	while success !=  1:
		userInput = input("Enter a Login: ")
	
	

		userPassword = input("Enter a Password: ")


	
	

	
	
		if userInput != username:
			print("ERROR: Userlogin is not valid email address")
			success = 0
		else:
		
			success = 1
	emailAddress = "JimPhan@yahoo.com"

	print("User = JimPhan@yahoo.com")
	return emailAddress 
