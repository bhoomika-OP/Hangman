import random

WIN_ASCII="""         
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠙⠋⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠫⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⠉⡀⠆⡡⢒⠰⣜⢧⣻⢴⣤⡤⣤⣀⡄⠀⠀⠀⠺⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢁⠂⠤⠑⡤⣩⢞⡭⢿⡹⣞⢧⢿⣱⣏⢾⡱⢂⠔⡀⠊⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠂⠌⡀⢏⡴⢣⡞⣽⣧⣿⣞⣯⣷⣳⣎⡧⣝⡬⢒⠠⢁⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠈⡔⡘⠀⣈⠁⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⢮⠳⡍⠂⠄⠂⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠀⢁⢒⡠⠙⠘⠛⠆⠀⠠⢟⣿⡿⡿⠏⠁⠀⣤⣤⠄⠁⠈⠄⠀⠈⠪⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡯⠃⠁⠀⠀⠀⠀⠀⠀⢮⠐⡀⠘⣄⣠⣆⡳⢈⣿⡇⢡⢔⡌⠁⢠⠈⠘⡄⠀⠂⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⡿⠿⣿⡏⠁⠀⠀⠀⠀⠀⠀⠀⠸⠸⡎⣰⢿⣸⣇⣶⢁⠾⣷⣉⠀⣎⢷⡱⣏⠀⢆⡸⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⡿⠁⠀⠀⠙⠃⠀⠀⠀⠀⣰⢟⣖⠀⢂⠱⣭⢻⣿⣿⣿⡿⢌⣹⣷⣯⡘⣬⣷⣷⡽⣚⢬⠓⡀⠀⢀⡀⠀⠀⠀⠀⠈⠙⢻⣿⣿⣿
⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣸⣟⡀⠠⢓⡌⣿⣿⣿⣿⢣⡜⣿⣿⣿⡇⡸⣿⣿⣿⡙⢎⡁⠀⣿⣿⣿⡆⠀⠀⠀⠀⢘⣿⣿⣿⣿
⣷⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠨⠿⣿⡁⠐⣡⠚⡵⣿⣿⣿⣀⣂⠻⠿⠟⡁⢢⣿⣿⡷⣍⠲⠀⣼⣮⣿⣿⠏⣠⣤⣤⣰⣿⣿⣿⣿⣿
⣿⣧⣠⣀⣀⡀⠀⠀⢠⣹⣿⣦⡲⠬⠷⠀⡜⡇⢹⡿⣛⢲⡹⣾⢿⣷⣿⡹⢏⣿⣿⡝⢢⡑⢀⣿⣿⢿⠍⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣿⣿⣷⠀⢸⢳⢰⡓⣇⠈⠛⠉⠛⣛⠙⠧⢣⣸⢿⠘⢠⠇⠘⣻⠖⣈⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⢫⠘⣽⣟⣎⠱⣞⣷⣶⢆⡄⣲⣾⡣⢨⡟⢀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⠆⠀⠃⢼⣻⣾⣷⣖⣦⣙⣮⡶⣿⢯⠁⠚⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⡐⢎⡄⡀⠈⢿⣻⣿⣿⣿⣿⣿⣿⡝⠂⢀⠄⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠠⣙⠦⡜⡤⣁⠈⠓⠛⠿⡿⢿⡻⠌⢁⠰⣈⠒⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣛⣿⠟⠡⣑⢮⡻⣵⣓⢦⡱⢌⠲⣤⢐⠠⢄⠒⣬⠳⠄⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠟⣭⣾⣿⣿⣿⠀⡜⡰⣭⢾⣽⣷⣿⢧⣛⣮⢷⣹⣎⢱⢪⡝⡶⣍⠌⡛⢺⣟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⣫⣵⣶⣿⣿⣿⣿⣿⣿⡜⣵⣹⢮⣟⣾⣿⣿⣿⡽⣮⣳⠻⣌⢷⣫⢞⡷⣌⠢⢵⢸⣿⣿⣷⣾⣭⣛⣻⢿⣿⣿⣿⣿⣿⣿⣿⡿
⡧⠾⠿⠿⠿⠿⠿⠿⠿⠿⡿⠿⠞⠵⠻⠞⠯⠿⠿⠿⠿⠷⠯⠟⠮⠷⠏⠿⠰⠢⠱⠎⠾⠿⠿⣿⠿⣿⠿⠿⠿⠶⠽⢻⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀
"""                                                                  #this ASCII art appears when the player guesses the correct letters within 6 attempts.

def hangman():
    word = "hakla"
    guessed_letters = []
    attempts = 6

    print("""Welcome to Hangman! Are you ready to play the world's best game EVER?
So without any delay, here are a few instructions on How To Play:

- There's a secret word already provided to the game.
- You have to guess it - one letter at a time.
- If your letter is in the word, it will be revealed in its correct position.
- If your letter is wrong, you lose one attempt.
- You have 6 attempts in total — guess the word before they run out!!!
- Good luck, Champ!
""")

    while attempts > 0:
        display = "".join(letter + " " if letter in guessed_letters else "_ " for letter in word)
        print("\nWord: " + display)

        if "_" not in display:
            print("YOOOOOOOOO!! YOU WON! The word was:", word)      #the player wins the game
            print(WIN_ASCII)
            return True

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():                  #the length of the guess should not exceed 1 character
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")               #the player can not enter the already guessed letter
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    print("OUUU SHIIII! GAME OVER!!!")                              #the player loses the game
    return False, word


def Play_Again():                                                   #if the player wishes to play again, they can select yes
    while True:
        result = hangman()

        if result is True:
            choice = input("\nDo you want to play again? (yes/no): ").lower()
        else:
            _, word = result
            choice = input("\nDo you want to play again? (yes/no): ").lower()
            if choice != "yes":
                print("The word was:", word)

        if choice != "yes":                                         #if the olayer does not wish to play again, they can select no
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    Play_Again()