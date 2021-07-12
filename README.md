# Caf-Login-and-Ordering-System
Python based program with a built-in login system that gathers user input response to result in a receipt of the selected items.

An ordering system based off of a cafe. Please take the following steps to ensure the code runs smoothly!
Files needed:
cake_order.py
login system.py
main.py
menu.py
recommendation.py
menu.txt
recipt.txt
user_database.txt

This ordering system starts off by asking the user to input their login information. Users can create their account and then log in to ensure the account it correct. If the username or password is wrong the user will not be able to go forth the next step and will continually have to input their login information. 
From there, the user is able to order off the menu, receive a recommendation or create a special cake order.
Users are able to type the items they want and once they are dont they enter 'end' which will then create a receipt for them with all of the items they wanted including the total cost.
Users can recieve a recommendation by answering a series of questions based on their response they will be suggested to buy an item from the menu that best suits their taste. Users can buy the item suggested and get a receipt of the item they were suggested, or they can decline the recommendation for a new suggestion or order off from the menu. Both of these results will end in a transaction and a recipt in the receipt.txt
Users can order a custom cake. They are given a series of questions on what they want in their cake. Once they have finished answering the questions they'll be asked if they like what they chose. If they like it it will proceed with the transaction along with the pickup date and time. If they do not like their custom order it will loop back to beginning of the function and the process starts over again.
