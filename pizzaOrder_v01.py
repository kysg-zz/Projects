#script for ordering food.

#global vars
name = ""
nameInput = "Drake"
loc = ""
locInput = ""

#pizza
sizeInput = ""
sSize = "Small"
mSize = "Medium"
lSize = "Large"
xSize = "X-Large"
topInput = ""

#cost
totalCost = 12.50

print("Welcome to Dave's Pizza, Let's get your order started.")

while sizeInput not in (sSize, mSize, lSize, xSize):
    print("Choose a size, we have: Small, Medium, Large, X-Large. Also, you can only pick 1 size.")
    sizeInput = input()
print("Thanks for choosing the size")
    

while topInput not in ("Pepperoni" , "Salami" , "Ham", "Pineapple", "Peppers", "Bacon", "Sausage"):
    print("Now what about the topping? You can only pick one. We have Pepperoni, Sausage, Salami, Ham, Pineapple, Peppers, and Bacon")
    topInput = input()
print("Thanks for choosing the topping.")

while True:
    print("So we have a " + sizeInput + " with " + topInput)
    print("Is that right?")
    costAnswer = input()
    if costAnswer == "Yes":
        print("Great")
        break
    else:
        print("I'm sorry about that, I apologize we got the order wrong. Have a nice day")
        exit()
        
while True:
    print("Your cost comes out to be " + str(totalCost))
    print("Is that ok?")
    costAnswer = input()
    if costAnswer == "Yes":
        print("Great")
        break
    else:
        print("I'm sorry about that, I apologize we got the order wrong. Have a nice day")
        exit()

while nameInput != name:
    print("Can I get your name?")
    nameInput = input()
    if nameInput == name:
        print("OK")
        break
        
while locInput not in("House", "Apartment", "Condo"):
    print("Are you located in a House, Apartment, or Condo?")
    locInput = input()
print("Good, we have the location") 
print("We will have that out in 15 minutes. Thank you.")
print("Closing Order...")


