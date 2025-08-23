friends = {}
total_amount = int
part_amount = float
friends_number = int(input("Enter the number of friends joining (including you):\n>"))
if friends_number <= 0:
    print("No one is joining for the party.")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range (friends_number):
        name = input(">")
        friends[name] = 0
    total_amount = int(input("Enter the total amount:\n>"))
    part_amount = round(total_amount / friends_number, 2)
    for key in friends:
        friends[key] = part_amount
    print(friends)
    import random
    random_friend = random.choice(list(friends.keys()))
    is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n>')
    is_lucky_lower = is_lucky.lower()
    if is_lucky_lower == 'yes':
        print(f"{random_friend} is the lucky one!")
        part_amount = round(total_amount / (friends_number - 1), 2)
        for key in friends:
            friends[key] = part_amount
        friends[random_friend] = 0
        print(friends)
    else: print("No one is going to be lucky.")