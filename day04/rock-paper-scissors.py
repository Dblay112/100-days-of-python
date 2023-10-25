rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choice = [rock, paper, scissors]
user_choice = int(input("What do yo choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(game_choice[user_choice])

comp_choice = random.randint(0, 2)
print("Computer chose: ")
print(game_choice[comp_choice])
if user_choice >= 3 or user_choice < 0:
  print("Invalid Choice, You lose!")
elif comp_choice > user_choice:
  print("You Lose!!!")
elif user_choice == 2 and comp_choice == 0:
  print("You Lose")
elif comp_choice == 0 and comp_choice == 2:
  print("You Win!!!")
