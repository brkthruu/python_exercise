import random

guide = """
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good Luck!
"""

print(guide)

answer = random.randint(1, 99)
cnt = 0
guess = 0

while(int(guess) != answer):
    guess = input("What's your guess between 1 and 99?\n>> ")
    if guess == 'exit':
        print("Goodbye!")
        break
    cnt += 1
    if int(guess) > answer:
        print("Too high!")
    elif int(guess) < answer:
        print("Too Low!")
    else:
        if answer == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if cnt == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in %d attempts!" % cnt)
