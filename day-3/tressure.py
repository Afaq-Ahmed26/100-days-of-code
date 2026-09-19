print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')

print("Welcome to tressure island, your mission is to find tressure")
direction = input("You are at a cross road, where do you want to go? Type 'left' or 'right' \n").lower()

if direction == "left":
    print("Game Over! You fell into a hole.")
elif direction == "right":
    print("You have come to a lake. There is an island in the middle of the lake.  \n")
    action = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if action == "swim":
        print("Game over shark eat you")
    elif action == "wait":
        print("Inside boat you have 3 doors Red , Blue , Yellow, you have to chose 1  \n")
        door = input("Type 'red' for chosing red door , Type 'yellow' for chosing yellow door , Type 'blue' for chosing blue door.").lower()
        if door == "red":
            print("game over")
        elif door == "yellow":
            print("Game Over")
        elif door == "blue":
            print("Congratulation you won")
else:
    print("Invalid input. Please type 'left' or 'right'.")