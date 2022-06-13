# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 23:33:50 2022

@author: ISAAC AJAYI
"""
import random
possible_actions = ["R", "P", "S"]
user_action = input("Enter a choice (R - rock, P - paper, S - scissors): ")
if user_action == "R":
    user_action = "rock"
elif user_action == "P":
    user_action = "paper"
elif user_action == "S":
    user_action = "scissors"
    
computer_action = random.choice(possible_actions)
if computer_action == "R":
    computer_action = "rock"
elif computer_action == "P":
    computer_action = "paper"
elif computer_action == "S":
    computer_action = "scissors"
    
print(f"Player({user_action}): CPU({computer_action})")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
    
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

