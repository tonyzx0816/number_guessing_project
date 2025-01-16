import art, random
print(art.logo)

random_num = random.randint(1,100)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {random_num}")

choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if choice == "easy":
    count = 10
else:
    count = 5

for i in range(count, 0, -1):
    if i != 1:
        print(f"You have {i} attempts remaining to guess the number.")
    else:
        print(f"You have {i} attempt remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess < random_num:
        print("Too low.")
    elif guess > random_num:
        print("Too high.")
    else:
        print(f"You got it! The answer was {random_num}")
        break

    if i != 1:
        print("Guess again.\n")
    else:
        print("You've run out of guesses, you lose.")