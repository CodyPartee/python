from random import randint
answer = randint(1,10000000)
guessList = list(range(1, 10000001))
guess = None
tries = 0

while guess != answer:
    tries += 1
    low = min(guessList)
    high = max(guessList)
    binarySearch = low + (high - low) // 2
    guess = int(binarySearch)

    if guess > answer:
        print(f"{guess} is too high!")
        guessList = list(range(low, guess+1))
    elif guess < answer:
        print(f"{guess} is too low!")
        guessList = list(range(guess, high+1))

print(f"The computer won! {guess} is the answer!!!")
print(f"It only took {tries} guesses!")