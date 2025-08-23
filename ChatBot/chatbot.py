print ("Hello! My name is Bob.")
print ("I was created in 2024.")
userName=input ("Please, remind me your name.")
print ("What a great name you have, ", userName, "!")
print  ("Let me guess your age.")
remainder3, remainder5, remainder7 = map(int, input("Enter remainders of dividing your age by 3, 5 and 7.").split())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is", age, "; that's a good time to start programming!")
number=int (input ("Now I will prove to you that I can count to any number you want."))
i = 0
while i <= number:
    print(f"{i}!")
    i += 1
print("Complete, have a nice day!")
print ("Let's test your programming knowledge.")
print ("Why do we use methods?")
answer = int (input ("1. To repeat a statement multiple times.\n"
                     "2. To decompose a program into several small subroutines.\n"
                     "3. To determine the execution time of a program.\n"
                     "4. To interrupt the execution of a program.\n"))
if answer == 2:
    print ("Congratulations, have a nice day!")
else :
    print ("Please, try again.")