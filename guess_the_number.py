import random

title = "Number Guessing game!"
print(title)


class NumberGamePlaylist:

    def number_guess(self):
        random_number = random.randint(1, 20)
        random_guess = random_number * 2
        guess = 0

        while guess != random_number:
            guess = int(input(f"Guess a number between 1 and {random_guess}: "))
            if guess < random_number:
                print("Guess again. Too low.")
            elif guess > random_number:
                print("Guess again. Too high")
            elif guess == random_number:
                print(f"Good job! you have guessed the correct number: {random_number}.")
                break

    def computer_guess(self):
        num_min = 1
        num_maximum = random.randint(1, 100)
        player_num = int(input(f"Pick a number for the computer to guess between {num_min} and {num_maximum}: "))
        low = num_min
        high = num_maximum
        feedback = ""
        while feedback != "c":
            if player_num <= num_maximum:
                if low != high:
                    guess = random.randint(low, high)
                else:
                    guess = low
                feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
                if feedback == "h":
                    high = guess - 1
                elif feedback == "l":
                    low = guess + 1
                else:
                    print(f"Nice! the computer guessed your number, {guess} correctly!")
                    break
            else:
                if player_num > num_maximum:
                    print(f"Pick a number between {num_min} and {num_maximum}!")
                    break
        else:
            print(f"Nice! the computer guessed your number, {guess} correctly!")
