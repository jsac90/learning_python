# SPACE LAUNCH GAME
#------------------------
#to do:
#add a timer 
# add a leaderboard
#add a UI
#-------------------------

import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    print("You are stranded on a strange planet and need to calculate the right amount of boost to leave orbit. Hurry though - If you don't get it right in 10 cycles, you will be eaten by aliens!")
    turn = 0
    grav = random.randint(1, 10)
    print("gravity is", grav)

    req_boost_var = random.randint(1, 10)
    random_val = random.randint(1, 100)
    total_req_boost = req_boost_var * grav + random_val

    while turn < 10:
        while True:
            user_input = input("Enter boost: ")
            try:
                user_boost = int(user_input)
                break
            except ValueError:
                print("please only enter numbers")
        if user_boost > total_req_boost:
            print("Too much boost")
        elif user_boost < total_req_boost:
            print("Not enough boost")
        else:
            print("You have the exact amount of boost to launch the rocket, you win!")
            return  # Win  and end this game
        
        turn += 1
        print ("You have used "+ str(turn) + " turns!\n") 

    print("you lose! - Aliens Got you!")

if __name__ == "__main__": #this is the main function that runs the game
    while True:
        clear_console()
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
