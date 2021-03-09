import random

letter_count = [(chr(i)) for i in range(97, 123)]
uppercase_letters = [(chr(i)) for i in range(65, 91)]
special_count = [(chr(i)) for i in range(33, 48)]
numbers_count = [(chr(i)) for i in range(48, 58)]

password = []


def combination():
    length_letter_count = len(letter_count)
    length_uppercase_letters = len(uppercase_letters)
    length_special = len(special_count)
    length_numbers = len(numbers_count)

    for i in range(random.randint(3, 8)):
        password.append(letter_count[random.randint(0, length_letter_count - 1)])
        password.append(uppercase_letters[random.randint(0, length_uppercase_letters - 1)])
        password.append(special_count[random.randint(0, length_special - 1)])
        password.append(numbers_count[random.randint(0, length_numbers - 1)])
    random.shuffle(password)



def listtostrng(password):
    stringpassword = ""
    for i in password:
        stringpassword += i
    return stringpassword


combination()
listtostrng(password)

with open('passwords.txt', 'a') as f:
    x = int(input("How many passwords do you need?\n>>>"))
    for i in range(x):
        combination()
        listtostrng(password)
        password.clear()
        combination()
        f.write(f"{listtostrng(password)}\n")
    f.close()

