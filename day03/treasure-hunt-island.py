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
                                               _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._
                                               /_______________|_______
                                               |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                                               |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-;
                                               ;___|___________________
                                               ____/______/______/___|o;._    "      `".o|o_.--"
                                               ;o;____/______/______/____
                                               /______/______/______/_"=._o--._        ; | ;        ;
                                               ;/______/______/______/_
                                               ____/______/______/______/__"=._o--._   ;o|o;
                                               _._;o;____/______/______/____
                                               /______/______/______/______/____"=._o._; |
                                               ;_.--"o.--"_/______/______/______/_
                                               ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                                               /______/______/______/______/______/______/______/______/______/______/_____
                                               /
                                               *******************************************************************************''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
crossroad = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"').lower()
if crossroad == "left":
    swim_choice = input('You\'ve come to a lake. There is an island in the middle of the lake Type "wait" to wait for a
    boat or type "swim" to swim accross.').lower()
    if swim_choice == "wait":
        door_choice = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and
        one blue. Which colour do you choose?').lower()
        if door_choice == "yellow":
            print("You Win!!!")
        elif door_choice == "red" or "blue":
                        print("You entered a room of beast. Game Over!!!")
    elif swim_choice == "swim":
        print("Game Over!!!")
else:
    print("Game Over!!!")
