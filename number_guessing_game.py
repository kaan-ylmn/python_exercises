import random
def game(): # You can use this code without using function method
    tries = 4
    level = 1
    while level < 9:
        print(f"----- Level {level} -----")
        guess = random.randint(1,10 ** level)
        tries = 4 ** level
        while tries > 0:
            guess_number = int(input(f"Please enter your guess: "))
            tries -= 1
            print(f"\nYou have {tries} tries left!!!")
            if guess_number == guess:
                print(f"\nPlayer wins the game, the number is {guess}")
                level += 1
                break
            elif guess_number > guess:
                print("Pick smaller one!\n")
            else:
                print("Pick larger one!\n")
        else:
            print(f"You lose! Here is your number {guess}")
            break   
game()
