import random #This is used to randomly choose an item from a list [] or basically a sequence.
import time  #it is used to import actual time from pc to use in program

# Initiate steps to invite in games:
print("\n Welcome to Hangman game by raidexQe\n")
name = input("enter your name: ")
print("hello " + name + "! best of luck!")

#This is the time that game starts at
time.sleep(2)
print("the game is about to start! \n Let's play the game")
time.sleep(3)


#define the main function 
def main():
    global count 
    global display
    global word 
    global already_guessed 
    global length 
    global play_game 
    word_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(word_to_guess)
    length = (len(word))
    count = 0
    display = '_' * length 
    already_guessed = []
    play_game = ""
    
    
# A loop to execute the game when the first round ends:
#function for looping

def play_loop(): #this function takes in the argument of play_game 
    global play_game #using this we decide wether the player wants to play again or not 
    play_game =input("do you want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y","N"]: #if user does not enters any of this option
        play_game.lower =input("do you want to play again? y = yes, n = no \n")
    if play_game == "y": # if user inputs y the function main is called
        main()
    elif play_game == "n": #if user inputs n the whole program exits 
        print("thanks For playing!")
        exit()
        
# Initialize all the condition required for the game:
#crating a function for conditions
def hangman():
    # calling all the argument again under hangman() func 
    global count 
    global display 
    global word
    global already_guessed
    global play_game    
    limit = 5
    guess = input("This is the hangman word: " + display + "enter your guess: \n")
    guess = guess.strip() #replaces the _ with the right guessed word from the user 
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, try a letter\n") #checks wether the user have enter right input(no number, no two words at same time)
        hangman()
        
        
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index+ 1:]
        print(display + "\n")
        
        
    elif guess in already_guessed:
        print("Try another letter. \n")
        
    else:
        count += 1 
        
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")          
            print("wrong guess. " + str(limit - count)+ "guesses reamining\n")
        
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")          
            print("wrong guess. " + str(limit - count)+ "guesses reamining\n")
        
        
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")          
            print("wrong guess. " + str(limit - count)+ "guesses reamining\n")
        
        
        if count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     |\n"
                  "  |     o \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")          
            print("wrong guess. " + str(limit - count)+ "guesses reamining\n")
        
        
        if count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     o \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")          
            print("wrong guess. You are hanged!!! \n")
            print("the word was:",already_guessed,word)
            play_loop()
    if word == '_' * length:
        print ("congrats! You have guessed the word correctly!")
        play_loop()
    
    elif count != limit:
        hangman()
        
main()

hangman()
       