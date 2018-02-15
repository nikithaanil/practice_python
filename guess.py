'''Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.'''

import random

a = random.randint(1,9)
ch = 'y'
count = 0

while ch == 'y':
    guess = int(input("enter the user guess:"))

    if guess < a:
        print("\nthe number guessed is too low !!! ")

    if guess > a:
        print("\nthe number guessed is too high !!! ")

    if guess == a:
        print("\nthe guess made is exact !!! ")

    count=count+1
    print("do you want to continue ?(y/n)")
    ch=input()

print("the number of guesses made is : {}".format(count))
