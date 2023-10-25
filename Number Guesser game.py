import random
import math

while True:
    # User inputs lowest number
    lower = int(input("Enter lowest number: "))

    # User inputs highest number
    higher = int(input("Enter highest number: "))

    # Randomizing selected number between lowest and highest input number
    x = random.randint(lower, higher)
    print("\n\tYou have ", round(math.log(higher - lower + 1, 2)), "chances to guess the number!\n")

 
    # Forming the number of guesses
    count = 0

    # Determining the number of guesses 
    while count < math.log(higher - lower + 1, 2):
        count += 1
    
    #Taking guessed number as input
        guess = int(input("Guess a number: "))

        #Testing the condition
        if x == guess:
            print(f"Congradulations, you did it in {count} tries!")
            
            #If/when user guesses the number correctly, the loop will break
            break
        
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You guessed too high!")


    #If user guesses more than the allowed guesses, this output will show
    if count > math.log(higher - lower + 1,2):
        print('\n\tThe number is %d' % x)
        print('\tBetter luck next time!')

    play_again = input("\n\tPress Enter to play again or type 'exit' to quit: ")
    if play_again.lower() == "exit":
        break