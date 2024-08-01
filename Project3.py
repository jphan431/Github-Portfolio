#!/user/bin/env python3

# Contact Management System Program

#Shows title of program at start.
print("Contact Management System")
print()

#Imports CSV Module
import csv

#Defines global constant for the file.
FILENAME = "contacts.csv"

#Displays menu options for user, called from main function.
def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()

#Defines write funtion for CSV file.
def write_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

#Defines read function for CSV file.
def read_contacts():
    contacts = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

#Lists the contacts in the list with the user inputs the "list" command.    
def list_contacts(contacts):
    for i in range(len(contacts)):
        contact = contacts[i]
        print(str(i+1) + ". " + contact[0])
    print()

#List a specific contacts information when the user inputs the "view" command.
def view_contact(number):
    contacts = read_contacts()
    specified_contact = contacts[number]
    print("Name: ", specified_contact[0])
    print("Email: ", specified_contact[1])
    print("Phone: ", specified_contact[2])

#Adds contact to the end of the list when user inputs the "add" command.
def add_contact(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)
    write_contacts(contacts)
    print(name + " was added.\n")

#Removes an item from the list.
def delete_contact(contacts):
    number = int(input("Number: "))
    if number < 1 or number > len(contacts):                         #Display an error message if the user enters an invalid number.
        print("Invalid contact number.\n")
    else:
        contact = contacts.pop(number-1)
        write_contacts(contacts)
        print(contact[0] + " was deleted.\n")

#Main function - list, view, add, and delete funtions run from here. 
def main():
    display_menu()
    contacts = read_contacts()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_contacts(contacts)
        elif command.lower() == "view":                                #Store the rest of the code that gets input and displays output in the main function. 
            view_contact(contacts)
        elif command.lower() =="add":
            add_contact(contacts)
        elif command.lower() == "del":
            delete_contact(contacts)
        elif command.lower() == "exit":                                
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("Bye!")

if __name__ == "__main__":
    main()