# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 11:47:27 2025

@author: 97156
"""
# Dictionaries categorize by food and beverage types
snacks = {
    '1' : {'menu': 'Chicken Sandwich', 'price': 4.00, 'stock': 5},
    '2' : {'menu': 'Beef Cheeseburger', 'price': 5.00, 'stock': 5},
    '3' : {'menu': 'Hot Dog', 'price': 5.00, 'stock': 5},
    '4' : {'menu': 'Hawaiian Pizza', 'price': 6.00, 'stock': 5},
    '5' : {'menu': 'Spicy Chicken Shawarma', 'price': 7.00, 'stock': 5},
    '6' : {'menu': 'Samyang Buldak Ramen', 'price': 9.00, 'stock': 5},
    }

sweets = {
    '7' : {'menu': 'Glazed Donut', 'price': 3.00, 'stock': 5},
    '8' : {'menu': 'Chocolate Cake', 'price': 6.00, 'stock': 5},
    '9' : {'menu': 'Red Velvet Cake', 'price': 6.00, 'stock': 5},
    '10' : {'menu': 'Ube Cake', 'price': 6.00, 'stock': 5},
    '11' : {'menu': 'Mochi', 'price': 7.00, 'stock': 5},
    '12' : {'menu': 'Chocolate Croissant', 'price': 8.00, 'stock': 5}
    }

hot_drinks = {
    '13' : {'menu': 'Chai', 'price': 2.00, 'stock': 5},
    '14' : {'menu': 'Black Coffee', 'price': 4.00, 'stock': 5},
    '15' : {'menu': 'Espresso', 'price': 4.00, 'stock': 5},
    '16' : {'menu': 'Hot Chocolate', 'price': 5.00, 'stock': 5},
    '17' : {'menu': 'Green Tea', 'price': 7.00, 'stock': 5},
    '18' : {'menu': 'Matcha Tea', 'price': 8.00, 'stock': 5}
    }

cold_drinks = {
    '19' : {'menu': 'Water', 'price': 1.00, 'stock': 5},
    '20' : {'menu': 'Coca Cola', 'price': 2.00, 'stock': 5},
    '21' : {'menu': 'Sprite', 'price': 2.00, 'stock': 5},
    '22' : {'menu': 'Iced Tea', 'price': 4.00, 'stock': 5},
    '23' : {'menu': 'Iced Latte', 'price': 4.00, 'stock': 5},
    '24' : {'menu': 'Dalgona Coffee', 'price': 6.00, 'stock': 5}
    }

name = input("Please Enter Your Name: ") #User input for name
age = input("Please Enter Your Age: ") #User input for age

while True: #While Loop that keeps on going until user has entered a valid numerical value
    if age.isdigit(): #If "age" is valid numerical value
        age=int(age) #Convert string "age" to integer
        break #Exits loop
        
    else: #Otherwise, if age is non-numerical value
        print("Invalid Input. Please Enter A Numerical Value.") #Print to the console

print ("\n") #Print newline character
greeting = ("Welcome to Huriya's Mini Restaurant and Cafe, " + name + "😊😊") #Variable for welcoming greetings, as well as adding user's name within it 
print(greeting.center(75)) #Print variable in center-alignment and width of 75
print("\n") #Print newline character

order = [] #Stores list of items ordered
total_amount = 0 #Stores the price of items ordered

while True: #Main While Loop that keeps on going until user has finalized their order
    
    print ("***Please Choose Your Menu***".center(75)) #Print in center-alignment and width of 75
    print ("""
           1. Snacks
           2. Sweets
           3. Hot Drinks
           4. Cold Drinks
           """) #Print to the console
           
    menu_number=int(input("Please Enter The Menu Number: ")) #User input for selecting menu number
    
    print("\n") #Print newline character
    print("***Please Select Your Order***".center(75)) #Print in center-alignment and width of 75
    print("\n") #Print newline character
    
    if menu_number == 1: #If menu number is equal to 1
        for key,item in snacks.items(): #Iterate through dictionary
            print(f"{key}. {item['menu']} - {item['price']} AED") #Print to the console
        dict=snacks #Stores dictionary's information
        
    elif menu_number == 2: #If menu number is equal to 2
        for key,item in sweets.items(): #Iterate through dictionary
            print(f"{key}. {item['menu']} - {item['price']} AED") #Print to the console
        dict=sweets #Stores dictionary's information
        
    elif menu_number == 3: #If menu number is equal to 3
        for key,item in hot_drinks.items(): #Iterate through dictionary
            print(f"{key}. {item['menu']} - {item['price']} AED") #Print to the console
        dict=hot_drinks #Stores dictionary's information
        
    elif menu_number == 4: #If menu number is equal to 4
        for key,item in cold_drinks.items(): #Iterate through dictionary
            print(f"{key}. {item['menu']} - {item['price']} AED") #Print to the console
        dict=cold_drinks #Stores dictionary's information
        
    else: #Otherwise, if menu number is invalid
        print("Invalid Option. Please Try Again.") #Print to the console
        continue #Continue Loop

    print("\n") #Print newline character
    
    while True: #Mini While Loop within Main While Loop that keeps on going until user has typed "done"
        
        order_number=input("Please Enter The Item's Number or Type Done To Finalize Your Order: ") #User input for selecting item number
        
        if order_number.lower() == 'done': #If user types "done". Also, user input will be converted to lowercase to prevent case sensitivity
            break #Exit loop
        
        if order_number in dict: #If order number exist in variable "dict"
            selected_item_number = dict[order_number] #Retrieve information and stores it
            
            if selected_item_number['stock'] > 0: #Checks for stocks and if the selected item number is greater than 0
                order.append(selected_item_number) #Add item to the order list
                total_amount += selected_item_number['price'] #Add item price to the total amount
                selected_item_number['stock'] -=1 #Decrements item stock by 1
                print(f"{selected_item_number['menu']} Has Been Added To Your Order.") #Print to the console
                print(f"There Are/Is {selected_item_number['stock']} Stock/s Left.") #Print to the console
                
            else: #Otherwise, if stock is less than or equal to 0
                print("Sorry. This Item Is Out of Stock.") #Print to the console

        else: #Otherwise, if order number is invalid
            print("Invalid Selection. Please Try Again.") #Print to the console
            continue #Continue loop
        
    different_menu=input("Would You Like To Select Items From Different Menu? Type Yes or No: ") #User input to select items from different menu
    
    if different_menu.lower() == 'no': #If user types "no". Also, the user input will be converted to lowercase to prevent case sensivitiy
       break #Exit Loop
   
    else: #Otherwise, if user types "yes"
       print("\n") #Print newline character
       continue #Repeat main While Loop


total_discount_amount = 0 #Stores discount amount based on age and items ordered
discount_percentage = 10 #Stores discount percentage to be applied depending on user's age
print("\n") #Print newline character

if order: #If user have items listed in variable "order"
    print("***Order Summary***".center(75)) #Print to the console in center-alignment and width of 75
    print("\n") #Print newline character
    for item in order: #Iterate through the list
        print(f"- {item['menu']} - {item['price']} AED") #Print to the console

else: #Otherwise, if user has no items listed in the variables "order"
    print("You Have Not Ordered Anything. Please Try Again") #Print to the console
    
if age <= 18: #If age is lesser than or equal to 18
   total_discount_amount = (total_amount * discount_percentage) / 100 #Calculate total price with discount and stores it
   print (f"Total Discounted Price: {total_discount_amount:.2f} AED") #Print to the console
   print(f"Total Amount Due: {total_amount:.2f} AED") #Print to the console

elif age >= 60: #If age is greater than or equal to 60
   total_discount_amount = (total_amount * discount_percentage) / 100 #Calculate total price with discount and stores it
   print (f"Total Discounted Price: {total_discount_amount:.2f} AED") #Print to the console
   print(f"Total Amount Due: {total_amount:.2f} AED") #Print to the console

else: #Otherwise
   print("No Discount") #Print to the console
   print(f"Total Amount Due: {total_amount:.2f} AED") #Print to the console
      
pay = total_amount - total_discount_amount #Subtracts total amount and total discount amount, then stores it

while total_amount > 0: #While Loop that keeps on going until total amount is atleast greater than 0
    
    try: #Detect potential errors
        payment = float(input(f"Your Total Amount Will Be {pay:.2f} AED: ")) #User input for their payment
        
        if payment == pay: #If payment is equal to pay
            print("Change: 0.00 AED.") #Print to the console
            print("\n") #Print newline character
            print("Your Order Has Been Dispensed. Please Enjoy Your Foods and/or Drinks.".center(75)) #Print to the console in center-alignment and width of 75
            print("Thank You For Your Purchase! Please Have A Nice Day😊😊".center(75)) #Print to the console in center-alignment and width of 75
            break
        
        elif payment >= pay: #If payment is greater than pay
            change = payment - pay #Calculate change
            print(f"Change: {change:.2f} AED.") #Print to the console
            print("\n") #Print newline character
            print("Your Order Has Been Dispensed. Please Enjoy Your Foods and/or Drinks.".center(75)) #Print to the console in center-alignment and width of 75
            print("Thank You For Your Purchase! Please Have A Nice Day😊😊".center(75)) #Print to the console in center-alignment and width of 75
            break
        
        else: #Otherwise, if payment is less than pay
            print("Insufficient Payment. Please Insert More Money.") #Print to the console
            pay -= payment #Calculate remaining balance
   
    except ValueError: #If user entered invalid input
        print("Invalid Payment Amount. Please Enter A Valid Input.") #Print to the console



