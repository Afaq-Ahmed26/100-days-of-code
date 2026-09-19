print("Welcome to python pizza!")
size =input("What size pizza do you want? S, M, or L: ")
bill = 0
topping = input("Do you want pepperoni? Y or N: ")
if topping == "Y":
    bill = 100
else:
    bill = 0
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 100
else:
    bill += 0    
if size == "S":
    bill += 150
elif size == "M":
    bill += 500
else:
    bill += 800

print(f"Thankyou for chosing python pizza, Your final bill is: {bill}")