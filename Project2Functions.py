def display_title():
    print("Department Store Sales Tax and Grand Total Application")
    print()
    
def get_all_items_total():
    counter = 0
    all_items_total = 0.00 #Declare an all items total 
    print('Data Entries: Enter 0 to end your input')
    while True: #Endless loop
        cost = float(input('Cost of item: ')) #Get cost of item
        if cost > 0 and cost < 200:
            all_items_total += cost
            counter += 1
        else:
            cost == 0
            break
    print('All items total: ${:.2f}'.format(all_items_total)) #Print the total in a two-decimal format
    print()
    return(all_items_total)
    
def get_discount(all_items_total): 
    if(all_items_total >= 100.00):
        discount = all_items_total * 0.10
    else:
        while True: #Use if/else to check the all items total to get correct discounts 
            pro_code = int(input('Promotion code: '))
            discount = 0
            if pro_code == 123:
                discount = 1.00
                break
            elif pro_code == 456:
                discount = 2.00
                break
            elif pro_code == 999:
                print("Invalid promotion code. Try Again")
                pro_code = int(input('Promotion code: '))
                break
            elif pro_code == 789:
                discount = 3.00
                break
            elif all_items_total >= 100.00:
                discount_percent = .1
                discount = discount_percent * all_items_total
                break
        return(discount)

def get_sales_tax(subtotal):
    
    while True:
        sales_tax_rate = int(input('Sales tax rate (%): '))
        
        if sales_tax_rate >= 6 and sales_tax_rate <= 10: #Check the sales tax rate to see if it is in the range (6 - 10)
            sales_tax_rate = float(sales_tax_rate / 100) #Calculate the sales tax             
            sales_tax_amount = round(subtotal * sales_tax_rate, 2)
            break #Get out of the endless loop and return the sales tax amount
        else:
            print("Error: The the tax rate is less than 6 or greater than 10")
    return(sales_tax_amount)               
#===============================================
