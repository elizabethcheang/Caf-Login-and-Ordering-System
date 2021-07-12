def menu():
    menu_file= open("menu.txt","r")
    items = menu_file.readlines()     
    print("\tʕ•ᴥ•ʔ☆~LE CAFE MENU~✿ʕ•ᴥ•ʔ\n")

    for line in items:
        print("\t",line)
    menu_file.close
menu()

def menu_ordering():
    print("Enter exactly how the item is spelled \nIf you do not want to buy anything anymore, enter 'end'\n")
    order=input("What would you like to order?\n")
    
    menu_file=open("menu.txt","r")
    items = menu_file.readlines()

    receipt=open("receipt.txt","w")
    receipt.write("--------------LE CAFE RECEIPT--------------\n")
    receipt.write("\tITEM\tPRICE\n")

    total=0
    while (order !="end"):
        for line in items:
            line=line.split(',')
            item=line[0]
            price=float(line[1])
            if item==order:
                total= total + price
                receipt.write("\n")
                receipt.write("\t")
                receipt.write(order)
                receipt.write("\t")
                receipt.write(str(price))
        order=input("What would you like to order?\n")
        
        
    
    payment=input("Enter type of payment (Debit/Credit): ")

    cashier=input("Enter the cashier's name: ")

    receipt.write("\n")
    receipt.write("-------------------------------------------------------")
    receipt.write("\n")
    receipt.write("Cashier: ")
    receipt.write(cashier)
    receipt.write("\n")
    receipt.write("Payment: ")
    receipt.write(payment)
    receipt.write("\n")
    receipt.write("\n")
    receipt.write("-------------------------------------------------------")
    receipt.write("\n")
    receipt.write("Total Cost: ")
    receipt.write(str(total))
    menu_file.close()
    receipt.close()

    print("Thank you for ordering at Le Cafe! Enjoy!")
    
menu_ordering()


