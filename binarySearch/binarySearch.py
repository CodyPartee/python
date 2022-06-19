from random import randint
answer = randint(1, 10000000)
low = 1
high = 10000000
guess = None
tries = 0
print(f'The number to find is {answer}')

while guess != answer:
    tries += 1
    binarySearch = low + (high - low) // 2
    guess = int(binarySearch)

    if guess > answer:
        print(f"{guess} is too high!")
        high = guess-1
    elif guess < answer:
        print(f"{guess} is too low!")
        low = guess+1

print(f"The computer won! {guess} is the answer!!!")
print(f"It only took {tries} guesses!")
