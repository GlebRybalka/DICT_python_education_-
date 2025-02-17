Markdown=['plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'unordered-list', 'ordered-list', 'new-line']

def helpmenu():
    print ("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n"
           "Special commands: !help !done")

def plain(str):
    return str + " "

def bold(str):
    return "**" + str + "** "


def italic(str):
    return "*" + str + "* "


def newline():
    return "\n"


def inlinecode(str):
    return "`" + str + "`"


def link(str,url):
    return "[" + label + "]" + "(" + url + ")"


def header(level, str):
    if level == 1:
        return "# " + str + "\n"

    elif level == 2:
        return "## " + str + "\n"

    elif level == 3:
        return "### " + str + "\n"

    elif level == 4:
        return "#### " + str + "\n"

    elif level == 5:
        return "##### " + str + "\n"

    elif level == 6:
        return "###### " + str + "\n"


def unorderedlist(item):
    return "- " + item + "\n"


def orderedlist(item, number):
    return f"{number}. " + item + "\n"



#Выполнение программы
helpmenu()

formatter=(str)


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
        level = int(input("Level: >"))
        while level < 1 or level > 6:
            print("The level should be within the range of 1 to 6.")
            level = int(input("Level: >"))
        text=input("Text: >")
        file.write(header(level, text))
        file.close()

    if formatter == "unordered-list":
        row_numbers = int(input("Number of rows: >"))
        while row_numbers <= 0:
            print("The number of rows should be greater than zero")
            row_numbers = int(input("Numbers of rows: >"))
        for i in range(row_numbers):
            i += 1
            item = input(f"Row #{i}: >")
            file.write(unorderedlist(item))
        file.close()

    if formatter == "ordered-list":
        row_numbers = int(input("Number of rows: >"))
        while row_numbers <= 0:
            print("The number of rows should be greater than zero")
            row_numbers = int(input("Numbers of rows: >"))
        for number in range(row_numbers):
            number += 1
            item = input(f"Row #{number}: >")
            file.write(orderedlist(item, number))
        file.close()

    readfile = open("output.md.", "r")
    print(readfile.read())
