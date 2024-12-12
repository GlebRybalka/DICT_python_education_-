print ("HANGMAN\nThe game will be available soon")

game_menu = input("""Type "play" to play the game, "exit" to quit:""")
if game_menu == "play":

    import random
    words =['python', 'java', 'javascript', 'php']
    random_word = random.choice(words)
    try_count = 8
    help_word = '-' * len(random_word)
    guessed=[]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while help_word != random_word and try_count >0:
        if game_menu == "exit":
            break
        answer = input(f"Guess the word\n{help_word}")
        if answer in guessed:
            print("You've already guessed this letter")
        if answer.isupper() or answer not in alphabet:
            print("Please enter a lowercase English letter")
        if len(answer) != 1:
            print("You should input a single letter")
        if answer in random_word:
            letter = ''
            for i in range(len(random_word)):
                if answer == random_word[i]:
                    letter += answer
                else: letter += help_word[i]
            help_word = letter
        else:
            if answer.islower() and answer in alphabet and len(answer) == 1:
                try_count -= 1
            print("That letter doesn't appear in the word")
        guessed.append(answer)
    if help_word == random_word:
        print(f"{help_word}\nYou win!")
    else: print("Thanks for playing!\nWe'll see how well you did in the next stage")
