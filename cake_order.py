def cake():
    receipt=open("receipt.txt","w")
    receipt.write("--------------LE CAFE RECEIPT--------------\n")
    receipt.write("\tSPECIAL CAKE ORDER\n")

    size=input("If you want a 6-inch cake, enter '6'\nIf you want a 10-inch cake, enter '10'\nIf you want a 12-inch cake, enter '12'\n")
    if size == '6' or size == '10' or size == '12':
        receipt.write("\n\tSize: ")
        receipt.write(size)
    else:
        print("Sorry! We don't have that size cake. Enter the options we have below.")
    flavor=input("Enter the flavor you would like you cake to be: Chocolate, Vanilla, or Red Velvet\n").lower()
    if flavor == "chocolate" or flavor == "vanilla" or flavor == "red velvet":
       receipt.write("\n\tCake flavor: ")
       receipt.write(flavor) 
    else:
        print("Sorry! We don't have that cake flavor here. Enter the options we have below.")
    frosting=input("Enter the flavor you would like for your frosting to be: Chocolate, Vanilla, or Cream Cheese\n").lower()
    if frosting == "chocolate" or frosting == "vanilla" or frosting == "cream cheese":
        receipt.write("\n\tFrosting: ")
        receipt.write(frosting)
    else:
        print("Sorry! We don't have that cake flavor here. Enter the options we have below.")
    design=input("Enter the design you would like on your cake: Flowers, Hearts, Stars, Balloons, or None \n").lower()
    if design == "flowers" or design == "hearts" or design == "stars" or design =="balloons" or design=="none":
        receipt.write("\n\tDesign: ")
        receipt.write(design)
    else:
        print("Sorry! We don't have that cake flavor here. Enter the options we have below.")
        
    writing=input("What would you like the cake to say?\n")
    receipt.write("\n\tWriting: ")
    receipt.write(writing)
    special_instructions=input("What special instructions you would like the baker to know?\nEnter 'none' if you have no special instructions\n")
    receipt.write("\n\tSpecial instructions: ")
    receipt.write(special_instructions)

    if size== '6':
        total= '$85'
    if size== '10':
        total= '$100'
    if size=='12':
        total='$120'
    

    confirm=input("Do you like what you ordered?\nEnter 'yes' or 'no'\n").lower()
    if confirm == "no":
        cake()
    if confirm == "yes":
        print("Enter the date and time you will be picking up the cake:\n")
        date=input("Pickup Date(MM/DD/YYYY): ")
        receipt.write("\n\tPickup Date:")
        receipt.write(date)
        time=input("Pickup Time(8am-9pm): ")
        receipt.write("\n\tPickup Time:")
        receipt.write(time)
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
        receipt.write(total)
        receipt.close()

        print("Thank you for ordering a cake from us! We hope you have a good day :)")

    
        
cake()
