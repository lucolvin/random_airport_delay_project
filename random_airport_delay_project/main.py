import random
import time
import os

# Clear the screen with support for Windows, Mac, and Linux
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def printMenu():
    clear()
    print("Welcome to the game!")
    print("1. Start Game")
    print("2. Settings")
    print("3. Exit")
    print("\n" * 3)
    choice = input("Enter a number: ")
    if choice == "1":
        startGame()
    elif choice == "2":
        settings()
    elif choice == "3":
        exit()

def changeName():
    clear()
    print("Change Name")
    print("1. Change First Name")
    print("2. Change Last Name")
    print("3. Back")

def startGame():
    clear()
    print("Starting Game...")
    time.sleep(2)
    print("Game Started!")
    time.sleep(2)
    lib = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    j = random.choice(lib)
    while True:
        print("DEBUG " + j) # DEBUG
        
        h = input("Guess a letter to continue...")
        if h == j:
            print(f"You Guessed the correct letter! The letter was {j}")
            time.sleep(2)
            return True
        elif h != j:
            clear()
            print(f"You guessed the wrong letter! It is not {h}")
            continue

def settings():
    clear()
    print("Settings")
    print("1. Change Name")
    # print("2. Change Color")
    print("3. Back")
    print("\n" * 3)
    choice = input("Enter a number: ")
    if choice == "1":
        changeName()
    # elif choice == "2":
    #     changeColor()
    if choice == "3":
        printMenu()


def exit():
    clear()
    print("Exiting...")
    time.sleep(2)
    print("Exited!")
    time.sleep(2)
    return


def main():
    # time.sleep(2)
    printMenu()


if __name__ == "__main__":
    main()



# TODO: Make game and tie into start game into printMenu()
# TODO: Make settings and tie into settings into printMenu()