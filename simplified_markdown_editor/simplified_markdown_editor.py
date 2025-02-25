Markdown=['plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'unordered-list', 'ordered-list', 'new-line']

def helpmenu():
    print ("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n"
           "Special commands: !help !done")

def plain(text):
    return text + " "

def bold(text):
    return "**" + text + "** "

def italic(text):
    return "*" + text + "* "

def newline():
    return "\n\n"

def inlinecode(text):
    return "`" + text + "`"

def link(label, url):
    return "[" + label + "]" + "(" + url + ")"

def header(level, text):
    if level == 1:
        return "# " + text + "\n"
    elif level == 2:
        return "## " + text + "\n"
    elif level == 3:
        return "### " + text + "\n"
    elif level == 4:
        return "#### " + text + "\n"
    elif level == 5:
        return "##### " + text + "\n"
    elif level == 6:
        return "###### " + text + "\n"

def unorderedlist(item):
    return "\n" + "- " + item + "\n"

def orderedlist(item, number):
    return "\n" + f"{number}. " + item + "\n"

#Выполнение программы
helpmenu()
formatter=()
while input != "!done":
    formatter = input("Choose a formatter: >")
    if formatter == "!done":
        break
    if formatter not in Markdown:
        print("Unknown formatting type or command")
    file = open("output.md.", "a")
    if formatter == "!help":
        helpmenu()
    if formatter == "plain":
        text=input("text: >")
        file.write(plain(text))
        file.close()
    if formatter == "bold":
        text=input("text: >")
        file.write(bold(text))
        file.close()
    if formatter == "italic":
        text=input("text: >")
        file.write(italic(text))
        file.close()
    if formatter == "new-line":
        file.write(newline())
        file.close()
    if formatter == "inline-code":
        text = input("text: >")
        file.write(inlinecode(text))
        file.close()
    if formatter == "link":
        label = input("Label: >")
        url = input("URL: >")
        file.write(link(label, url))
        file.close()
    if formatter == "header":
        level = input("Level: >")
        while level.isdigit() == False:
            print("Please, type a number within the range of 1 to 6.")
            level = input("Level: >")
        level = int(level)
        while level < 1 or level > 6:
            print("The level should be within the range of 1 to 6.")
            level = int(input("Level: >"))
        text=input("Text: >")
        file.write(header(level, text))
        file.close()
    if formatter == "unordered-list":
        row_numbers = input("Number of rows: >")
        while row_numbers.isdigit() == False:
            print("Please, type a number.")
            row_numbers = input("Number of rows: >")
        row_numbers = int(row_numbers)
        while row_numbers <= 0:
            print("The number of rows should be greater than zero")
            row_numbers = int(input("Numbers of rows: >"))
        for i in range(row_numbers):
            i += 1
            item = input(f"Row #{i}: >")
            file.write(unorderedlist(item))
        file.write(newline())
        file.close()
    if formatter == "ordered-list":
        row_numbers = input("Number of rows: >")
        while row_numbers.isdigit() == False:
            print("Please, type a number.")
            row_numbers = input("Number of rows: >")
        row_numbers = int(row_numbers)
        while row_numbers <= 0:
            print("The number of rows should be greater than zero")
            row_numbers = int(input("Numbers of rows: >"))
        for number in range(row_numbers):
            number += 1
            item = input(f"Row #{number}: >")
            file.write(orderedlist(item, number))
        file.write(newline())
        file.close()

    readfile = open("output.md.", "r")
    print(readfile.read())
