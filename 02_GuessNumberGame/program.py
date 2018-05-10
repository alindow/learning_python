import random

print('-----------------------------')
print('         Zahlen raten')
print('-----------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

while guess != the_number:
    guess_text = input("Rate eine Zahl zwischen 0 und 100: ")
    guess = int(guess_text)

    if guess > the_number:
        print("Die geratene Zahl {} ist leider zu hoch".format(guess))
    elif guess < the_number:
        print("Die geratene Zahl {} ist leider zu niedrig".format(guess))
    else:
        print("Du hast gewonnen!!! Die Zahl war tatsächlich {}".format(the_number))
print("Done")