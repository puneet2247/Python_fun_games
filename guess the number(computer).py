import random  #using ranodm library to generate random number

#Creating a function
def guess(x):
    random_number=random.randint(1,x)
    user_number=0
    while user_number != random_number:
        user_number=int(input(f"Guess the number between 1 and {x}: "))
        if user_number < random_number:
            print("you are too low, try again!")
        elif user_number > random_number:
            print("you are too high, try again!")    
    print(f"Bingo ! you guessed it right it is '{random_number}' correctly")

#function to  make the computer guess user secret number        
def computer_guess(x):
    low = 1
    high = x
    feedback= ''
    while feedback != 'c':
        if high != low :
            guess = random.randint(low,high)
            feedback = input(f"is the number {guess} too high {'H'}, too low {'L'} or correct {'C'} ?".lower())
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
        else:
            guess = low
        

    print(f"The computer guessed your number, {guess}, correctly!")



computer_guess(100)
#guess(10)
