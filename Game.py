import random

randomizer = random.randint(1,9)
chances = 5

print(randomizer)

while chances > 0:

    guess = int(input("Take a guess! "))

    if (guess == randomizer):
        print("Good guessing, you won! You deserve a reward! Go to https://www.youtube.com/watch?v=O91DT1pR1ew for your reward!")
        break

    if (guess < randomizer):
        print("Not quite! Try something higher! (Remember, numbers are generated 1-9")
        chances = chances - 1

    if (guess > randomizer):
        print("Not quite! Try something lower! (Remember, numbers are generated 1-9")
        chances = chances - 1

    if (chances == 0):
        print("Aww man! You didn't guess ", randomizer, "!")
        break