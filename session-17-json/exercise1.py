import json
import termcolor

f = open("exercise1.json", 'r')

members = json.load(f)

print()

for people in members:
    termcolor.cprint("Name: ", 'green', end='')
    print(people['Firstname'], people['Lastname'])
    termcolor.cprint("Age: ", 'green', end='')
    print(people['age'])
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(people['phoneNumber']))
    for i, num in enumerate(people['phoneNumber']):
        termcolor.cprint("Phone {}: \n".format(i), 'blue', end='')

        termcolor.cprint("     Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("     Number: ", 'red', end='')
        print(num['number'])
    print()
