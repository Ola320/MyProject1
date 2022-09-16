import random

my_number = random.randint(0, 20)
guess = -1
trials = 0

print('Guess my number')

while guess != my_number:

    guess = int(input())

    if guess == my_number:
        print('great u guessed my number',my_number)
    elif guess > my_number:
        print("your number is too big",guess)
    else:
        print('your number is too small')
