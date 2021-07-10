from random import *
num = randint(1,9)
attempts = 0
print("Guess a number from 1 to 9")
userNum = int(input("Enter your guess"))

while attempts < 3:
    attempts+=1
    if userNum > num:
        print("Try again your number was too high!")
        userNum = int(input("Enter your guess"))
    if userNum < num:
        print("Try again your number was too low!")
        userNum = int(input("Enter your guess"))
    if userNum == num:
        print("Congrats you guessed correctly")
        break
    if not attempts < 3:
        print("You lose!!!!!!! The number is ", num)
        break