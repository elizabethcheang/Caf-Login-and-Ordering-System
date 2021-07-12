def recommendation():
    receipt=open("receipt.txt","w")
    receipt.write("--------------LE CAFE RECEIPT--------------\n")
    receipt.write("\tITEM\tPRICE\n")
    q1=input("Enter 'beverage' if you would like a beverage or 'pastry' if you want a pastry?\n").lower()
    if q1=="beverage":
        beverage=input("Enter 'refresher' if you like refeshers or 'coffee' if you prefer coffee\n").lower()
        
        if beverage =="coffee":
            coffee=input("Enter 'hot' if you like hot coffee or enter 'cold' if you prefer cold coffee\n").lower()
            if coffee=="hot":
               sweetness=input("If you prefer your hot coffee to be strong and less sweet, enter 'strong'.\nIf you like sweet hot coffee, enter 'sweet'\n")
               if sweetness=="strong":
                   purchase=input("We reccomend you try the 'Signature Drip Coffee'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                   if purchase=="yes":
                       total="3.50"
                       receipt.write("\t\nSignature Drip Coffee\t")
                       receipt.write(total)
               if sweetness=="sweet":
                   purchase=input("We reccomend you try the 'Caramel Macchiato'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                   if purchase=="yes":
                       total="4.50"
                       receipt.write("\t\nCaramel Macchiato\t")
                       receipt.write(total)
            if coffee=="cold":
                sweetness=input("If you prefer your iced coffee to be strong and less sweet, enter 'strong'.\nIf you like sweet iced coffee, enter 'sweet'\n").lower()
                if sweetness=="strong":
                    purchase=input("We reccomend you try the 'Iced Americano'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                    if purchase=="yes":
                        total="4.25"
                        receipt.write("\t\nIced Americano\t")
                        receipt.write(total)
                if sweetness=="sweet":
                    purchase=input("We reccomend you try the 'Sweet Cream Caramel Drizzle Iced Coffee'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                    if purchase=="yes":
                        total="5.00"
                        receipt.write("\t\nSweet Cream Caramel Drizzle Iced Coffee\t")
                        receipt.write(total)
                    
        if beverage=="refresher":
            refresher=int(input("Enter '1' if you like carbonated drinks or '2' if you prefer non-carbonated drinks\n"))
            if refresher==1:
                purchase=input("We reccomend you try the 'House Specialty Sparkling Lemonade'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                if purchase=="yes":
                    total="3.25"
                    receipt.write("\t\nHouse Specialty Sparkling Lemonade\t")
                    receipt.write(total)
            if refresher== 2:
                purchase=input("We reccomend you try the 'Passion Fruit and Guava Sweet Iced Tea'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                if purchase=="yes":
                    total="3.25"
                    receipt.write("\t\nPassion Fruit and Guava Sweet Iced Tea\t")
                    receipt.write(total)
    if q1=="pastry":
        pastry=input("Enter 'savory' for a savory pastry.\nEnter 'sweet' for a sweet pastry\n").lower()
        if pastry=="savory":
            filling=input("Enter 'meat' if you like a meant filling pastry\nEnter 'veggie' for a vegetable filling pastry\n").lower()
            if filling=="meat":
                purchase=input("We reccomend you try the 'Croquette'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                if purchase=="yes":
                    total="3.50"
                    receipt.write("\t\nCrpquette\t")
                    receipt.write(total)
            if filling=="veggie":
                purchase=input("We reccomend you try the 'Feta Garden Puff Pastry'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                if purchase=="yes":
                    total="4.00"
                    receipt.write("\t\nFeta Garden Puff Pastry\t")
                    receipt.write(total)
                    rec_result(purchase)
        if pastry=="sweet":
            texture=input("Enter 'crunchy' if you like a crunchy pastry\nEnter 'creamy' for a soft and creamy pastry\n").lower()
            if texture=="crunchy":
                forc=input("Enter 'chocolate' if you like chocolate pastries\nEnter 'fruit' for fruity pastries\n").lower()
                if forc=="chocolate":
                    purchase=input("We reccomend you try the 'Chocolate Croissant'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                    if purchase=="yes":
                        total="3.50"
                        receipt.write("\t\nChocolate Croissant\t")
                        receipt.write(total)
                if forc=="fruit":
                    purchase=input("We reccomend you try the 'Strawberry and Raspberry Danish'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                    if purchase=="yes":
                        total="2.75"
                        receipt.write("\t\nStrawberry and Raspberry Danish\t")
                        receipt.write(total)
            if texture=="creamy":
                flavor=input("Enter 'chocolate' if you like chocolate flavored pastries\nEnter 'vanilla' for vanilla flavored pastries\n").lower()
                if flavor=="chocolate":
                    purchase=input("We reccomend you try the 'Chocolate Creme Patisserie'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                    if purchase=="yes":
                        total="3.50"
                        receipt.write("\t\nChocolate Creme Patisserie\t")
                        receipt.write(total)
                if flavor=="vanilla":
                    purchase=input("We reccomend you try the 'Vanilla Cream Layered Puff Pastry'. Would you like to purchase this item? Enter 'yes' or 'no'\n").lower()
                    if purchase=="yes":
                        total="2.75"
                        receipt.write("\t\nVanilla Cream Layered Puff Pastry\t")
                        receipt.write(total)
                    
    if purchase=="yes":
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

        print("Thank you for ordering at Le Cafe! Enjoy!")
    if purchase=="no":
        alternative=input("No problem!\nEnter '1' if you would like to be recommended something else\nEnter '2' if you would rather order off the menu\nIf you do not want to order anything, enter 'end'\n").lower()
        if alternative=="1":
            recommendation()
        elif alternative=="2":
            import menu as m
            m
        else:
            print("Thank you for stopping by, we hope to see you again!")

recommendation()

