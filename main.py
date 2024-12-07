import random
n = random.randint(1,100)

guesses = 0

guessed_num = 0

while(guessed_num != n):
    guesses+=1
    guessed_num = int(input("Guess the number :"))

    if(guessed_num>n):
        print("Lower number")
    else:
        print("Higher number")

print(f"You guess the number in {guesses} guesses")
