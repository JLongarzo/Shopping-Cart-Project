import datetime
import time
import os
from dotenv import load_dotenv 

load_dotenv()

#sets tax rate from env variable
taxRate = float(os.getenv("TAX_RATE", "0.0"))



products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#try and catch to catch an invalid string input
def checkValidity(uInput):
    validity = False
    try:
        if (int(uInput) in productIds):
            validity = True
    except:
        validity = False

    return validity


def to_usd(my_price):
    return f"${my_price:,.2f}"



productIds = []
i = 0

#get array of only product ids
while (i < len(products)):
    iProduct = products[i]
    productIds.append(iProduct["id"])
    i = i + 1


#array of product identifiers
userBought = []


#conditional for if user returned an incorrect value
#essential to catch edge case if user inputs invalid product identifier and prooceeds to input DONE
inputInvalid = False

#instantiate userInput as an empty string as it must exist before we enter the loop
userInput = ""



#open loop - while input != done
while (userInput != "DONE"):
    userInput = ""
    if (inputInvalid == True):
        userInput = input("incorrect product identifier, please try again: ")
    else:
        userInput = input("Please Input a Product Identifier: ")

    #reset conditional
    inputInvalid = False


    if (checkValidity(userInput) == True):
        #append to the product identifier to an array, we will format print value in print loop
        userBought.append(int(userInput))

    else:
        inputInvalid = True

#code for setting time found from: https://www.programiz.com/python-programming/datetime/current-datetime
t = time.localtime()
currentTime = time.strftime("%I:%m %p", t)

print("---------------------------------")
print("Big Brain Food Store")
print("---------------------------------")
print(f"CHECKOUT AT: {str(datetime.date.today())} {currentTime}") #how to print time?? ------
print("---------------------------------")

#enter loop to print contents of the user's inputs
subtotal = 0
i = 0
while (i < len(userBought)):
    purchasedProduct = products[userBought[i]]
    print(f" + {purchasedProduct['name']} ({to_usd(purchasedProduct['price'])})")
    subtotal = subtotal + purchasedProduct['price']


    i = i + 1


tax = subtotal*taxRate
total = subtotal + tax

print("---------------------------------")
#subtotal... etc goes here - calculate them in loop
print(f"Subtotal: {to_usd(subtotal)}")
print(f"Plus NYC Sales Tax ({str(taxRate*100)}%): {to_usd(tax)}")
print(f"Total: {to_usd(total)}")
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")





