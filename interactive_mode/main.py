from random import randint

min_number = int(input("Please enter a min number: "))
max_number = int(input("Please enter a max number: "))

if min_number > max_number:
    print('Invalid Input - Shutting Down')
else:
    rnd_number = randint(min_number, max_number)
    print(rnd_number)
