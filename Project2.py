import Project2Functions 

def main(): 
    Project2Functions.display_title()
    while True: 
        all_items_total = Project2Functions.get_all_items_total()

        discount = Project2Functions.get_discount(all_items_total) 
        Subtotal = round(all_items_total - discount, 2)
        
        sales_tax_amount = Project2Functions.get_sales_tax(Subtotal)
        
        Grandtotal = round(Subtotal + sales_tax_amount, 2)
        
        print()
        
        print('All items total: ${:.2f}'.format(all_items_total))
        print('Discount amount: ${:.2f}'.format(discount))
        print('Subtotal: ${:.2f}'.format(Subtotal))
        print('Tax: ${:.2f}'.format(sales_tax_amount))
        print('Grand total: ${:.2f}'.format(Grandtotal))
        print()
        
        choice = input('Continue? y/Y/n/N: ')
        
        if choice.lower() == 'n': #If the user enters n, terminate this program
            break
        print()
    
    print()
    print('Program is terminated')

if __name__ == "__main__":
    main() #Call the main function to start the project


