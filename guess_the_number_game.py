import random

#easy difficulty
def foreasy (number):
    guesses = 10
    num = 0
    while guesses > 0:    
        print(f"({guesses} guesses left)")
        num = int (input("Your Guess: "))
        guesses = guesses -1        
        if num < number :
            print("Too low! 📉")
        elif num > number :
            print("Too high! 📈")
        else :
            print(f"🎉 Correct! {number} is the number.")
            return
                
    print(f"Oops! correct number is the {number}.")


#medium difficulty
def formedium(number):
    guesses = 7
    num = 0
    while guesses > 0:    
        print(f"({guesses} guesses left)")
        num = int (input("Your Guess: "))
        guesses = guesses -1        
        if num < number :
            print("Too low! 📉")
        elif num > number :
            print("Too high! 📈")
        else :
            print(f"🎉 Correct! {number} is the number.")
            return
                
    print(f"Opss! correct number is the {number}.")

#hard difficulty
def forhard(number):
    guesses = 5
    num = 0
    while guesses > 0:    
        print(f"({guesses} guesses left)")
        num = int (input("Your Guess: "))
        guesses = guesses -1        
        if num < number :
            print("Too low! 📉")
        elif num > number :
            print("Too high! 📈")
        else :
            print(f"🎉 Correct! {number} is the number.")
            return
                
    print(f"Opss! correct number is the {number}.")

#main function
print("=== Welcome to Guess the Number! ===\n")
play = "y"
while play.lower() == "y" :
    print("Choose difficulty:")
    
    print('''    1) Easy    – 10 guesses
      2) Medium  – 7  guesses
      3) Hard    – 5  guesses''')
    
    difficulty = int(input("Select 1-3: "))
    if difficulty < 1 or difficulty > 3 : 
        print("Not Valid!")
        break
    print("🔢 I’m thinking of a number between 1 and 100…")
    number = random.randint(1, 100)
    
    if difficulty == 1 :
        foreasy(number)
    elif difficulty == 2:
        formedium(number)
    elif difficulty == 3:
        forhard(number)
    else:
        print("Not valid!")

    play = input("Play again? (y/n): ")
    