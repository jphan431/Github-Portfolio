# a file in the current directory
FILENAME = "monthly_sales.txt"

# set a default value
sales_default = {'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'Jun': 0, 'Jul': 0, 'Aug': 0, 'Sep': 0, 'Oct': 0, 'Nov': 0, 'Dec': 0}

# method for reading the monthly_sales file into a dictionary
def read_sales():  
  sales = {}
  with open(FILENAME, "r") as file:
    for line in file:
      line = line.replace("\n", "")
      row = line.split("\t")
      sales[row[0]] = int(row[1])
  return sales

# method for editing the value in a month and writing it to the file
def edit_month(sales):
  month = input("Three-letter Month: ")
  month = month.title()
  if month in sales.keys():
    amount = int(input("Sales Amount: "))
    sales[month] = amount
    print("Sales amount for {:s} is {:,.2f}.".format(month, amount))
    print()
  else:
    print("Invalid three-letter month.")
    print()
  return sales

# method for writing the file
def write_sales(sales):  
  with open(FILENAME, "w") as file:    
    for month, amount in sales.items():
      file.write(month + "\t" + str(amount) + "\n")

def compute_totals(sales):
    totals = 0.0
    for month, amount in sales.items():
        totals += amount
    return totals

def display_menu():
    print("Monthly Sales program")
    print()
    print("COMMAND MENU")
    print("load   - Load sales from file")
    print("view   - View sales for specified month")
    print("edit   - Edit sales for specified month")
    print("totals - View sales summary for year")
    print("write -  Write sales to file")
    print("exit   - Exit program")

def main():
    display_menu()
    sales = {}          
    while True:
        print()
        command = input("Command: ")
        command = command.lower()
        if command == "load":
            try:
                sales = read_sales()
                print(sales)
            except:
                print("Could not load from sales file; using defaults")
                sales = sales_default
        elif command == "view":
            print(sales)
        elif command == "edit":
            sales = edit_month(sales)            
        elif command == "totals":
            print( compute_totals(sales) )
        elif command == "write":
            write_sales(sales)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")            

if __name__ == "__main__":
    main()