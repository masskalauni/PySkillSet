lower=int(input("Enter the lower bound: "))
upper=int(input("Enter the upper bound: "))
import random
randomNumber=random.randint(lower,upper)
print("\n\tYou've only ",round((upper-lower)/20)," chances to guess the integer!\n")
count=0
while count<((upper-lower))/2:
    count=count+1
    guess=int(input("Guess a number between:"))
    if guess==randomNumber:
        print("Congratualtions! You've guessed the number in ",count," attempts.")
        break
    elif guess>randomNumber:
        print("You've guessed too high.")
    elif guess<randomNumber:
        print("You've guessed too low.")
if count>=((upper-lower)/2):
    print("\nThe number is ",randomNumber)
    print("\tBetter luck next time!")