import random
import sys
import re


def determine_the_winner (a, b):
    if b in weaker_list:
        print(f"Well done. The computer chose {b} and failed")
        return "Win"
    elif a == b:
        print(f"There is a draw ({b})")
        return "Draw"
    else:
        print(f"Sorry, but the computer chose {b}.")
        return "Lose"


def crediting_rating(arg):
    if result == "Draw":
        arg += 50
    elif result == "Win":
        arg += 100
    return arg


def show_rating(arg):
    print(f"Your rating: {arg}")


default_options = ['rock', 'paper', 'scissors']
user_rating = None
user_name = input("Enter your name: >")
print(f"Hello, {user_name}")
with open('rating.txt', 'r') as file:
    for line in file:
        if user_name in line:
            match = re.search(r"\d+", line)
            if match:
                user_rating = int(match.group())
            break
        else:
            user_rating = 0

while True:
    while True:
        options_choice = input("Default options is rock, paper, scissors\nEnter options: >")
        if options_choice == '' or re.search(r"[a-zA-Zа-яА-Я]", options_choice):
            break
        else: print("Invalid input")
    if options_choice == '':
        options = default_options
        break
    elif len(options_choice.split(',')) >= 3:
        options = re.split('[, ]', options_choice)
        break
    print("There are not enough options, enter at least 3.")
print("Okay, let's start")
while True:
    while True:
        user_choice = input(">")
        if user_choice == "!exit" or user_choice == "!rating" or user_choice in options:
            break
        print("Invalid input")
    if user_choice == "!exit":
        print("Bye!")
        sys.exit()
    if user_choice != "!rating":
        index = options.index(user_choice)
        temporary_list = options[index + 1:] + options[:index]
        weaker_list = temporary_list[len(temporary_list) // 2:]
        stronger_list = temporary_list[:len(temporary_list) // 2]
        option = random.choice(options)
        result = determine_the_winner(user_choice, option)
        user_rating = crediting_rating(user_rating)
    if user_choice == "!rating":
        show_rating(user_rating)
