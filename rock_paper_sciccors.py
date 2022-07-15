import random

choice=["rock","paper","scissors"]
computer_choice=choice[random.randint(0,2)]
user_choice=input("Enter your choice: ")
print("computer choice: {}".format(computer_choice))
if (user_choice=="rock" and computer_choice=="scissors"):
    print("You Win")
elif (user_choice=="paper" and computer_choice=="rock"):
    print("You Win")
elif (user_choice=="scissors" and computer_choice=="paper"):
    print("You Win")
elif user_choice==computer_choice:
    print("You Tie")
else:
    print("You lose computer wins")