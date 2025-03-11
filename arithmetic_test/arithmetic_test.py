import random
import re
import sys

def random_arithmetic():
    operator = random.choice(["+", "-", "*"])
    task = f"{random.randint(2, 9)} {operator} {random.randint(2, 9)}"
    u_a = input(f"{task}\n>")
    c_a = eval(task)
    return u_a, c_a


def random_squaring():
    x = random.randint(11, 29)
    task = f"{x} * {x}"
    u_a = input(f"{task}\n>")
    c_a = eval(task)
    return u_a, c_a


def make_result_message(name, num1, num2, text):
    message = f"{name}: {num1}/5 in level {num2} {text}.\n"
    return message


def save_result_to_file(message):
    result_file = open("results.txt", "a")
    result_file.write(message)


user_answer = None
correct_answer = None
level_description = None
level = input("Which level do you want? Enter a number:\n"
              "1 - simple operations with numbers 2-9\n"
              "2 - integral squares of 11-29\n>")
while level != '1' and level != '2':
    print("Incorrect format.")
    level = input(">")
task_counter = 5
right_answer_counter = 0
while task_counter > 0:
    if level == '1':
        level_description = "simple operations with numbers 2-9"
        user_answer, correct_answer = random_arithmetic()
    elif level == '2':
        level_description = "integral squares of 11-29"
        user_answer, correct_answer = random_squaring()
    while re.match('[a-zA-Z`~!@#$%^&*()+=,./;<>?:]', user_answer) or user_answer == '':
        print("Incorrect format.")
        user_answer = input(">")
    else: user_answer_int = int(user_answer)
    if user_answer_int == correct_answer:
        right_answer_counter += 1
        print("Right!")
    else:
        print("Wrong!")
    task_counter -= 1
save_result = input(f"Your mark is {right_answer_counter}/5."
                    f"Would you like to save your result to the file? Enter yes or no.\n>")
if save_result == 'yes' or save_result == 'Yes' or save_result == 'YES' or save_result == 'y' or save_result == 'Y':
    user_name = input("What is your name?\n>")
    result_message = make_result_message(user_name, right_answer_counter, level, level_description)
    print("The results are saved in 'results.txt'.")
    save_result_to_file(result_message)
else:
    sys.exit()
