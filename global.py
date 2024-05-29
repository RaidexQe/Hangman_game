#def my():
   # global himal
    #himal = input("enter your name ")

# my()
# print ("my name is " + himal )   

himal = "apple"
a = len(himal)
display = '_' * a
print (a)
print (display)
guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
guess = guess.strip()