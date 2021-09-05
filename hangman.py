import random
def hangman():
    word = random.choice(["pugger","little","tiger","superman","pokemon","avengers","water","thor","earth","girl"])
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main =  ""
        for letter in word:
            if letter in guessmade:
                main += letter
            else:
                main = main + "_"  + ""
        if main == word:
            print(main.upper() +" was the right word!")
            print("You win!")
            break
        print("Guess the letter ",main)
        guess = input().lower()#The letter that the user has entered.

        if guess in valid_letters:
            guessmade += guess
        else :
            print("Enter a valid character!")
        if guess not in word:
            turns -= 1
            if(turns == 9):
                print("9 turns left")
                print(" --------  ")
                print(letter)
                print(word)
                print(main)
                print(guess)
            if(turns == 8):
                print("8 turns left")
                print(" ---------  ")
                print("     O      ")
            if(turns == 7):
                print("7 turns left")
                print(" ---------  ")
                print("     O      ")
                print("     |      ")
            if(turns == 6):
                print("6 turns left")
                print(" ---------  ")
                print("     O      ")
                print("     |      ")
                print("    /      ")
            if(turns == 5):
                print("5 turns left")
                print(" ---------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if(turns == 4):
                print("4 turns left")
                print(" ---------  ")
                print("    \       ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if(turns == 3):
                print("3 turns left")
                print(" ---------  ")
                print("    \ /     ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if(turns == 2):
                print("2 turns left")
                print(" ---------  ")
                print("    \O/|    ")
                print("     |      ")
                print("    / \     ")
            if(turns == 1):
                print("1 turns left")
                print(" ---------  ")
                print("    \O_|/   ")
                print("     |      ")
                print("    / \     ")
            if(turns == 0):
                print("You loose!")
                print("You let a kind man die!")
                print(" ---------  ")
                print("     O_/    ")
                print("    /|\     ")
                print("    / \     ")
                print(word.upper() + "  was the correct word !")
                break
                
#print("                   Welcome              ")
print(".................HANGMAN GAME...................")
name = input("Enter you name! ")
print("Welcome ",name)
print("-----------------------")
print("Try to guess the word in less than 10 turns!")
hangman()
print()