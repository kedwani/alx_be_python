import random
seceret_number = random.randint(1, 10)
print("Welcome to the Number Guessing Game!")   
def run (number_of_attempts = 1):
    global seceret_number
    guess = int(input("Guess a number between 1 and 10: "))
    match guess:
        case _ if guess == seceret_number:
                print("Congratulations, you guessed it!")
                print(f"You found the number in {number_of_attempts} attempts.")
                if input("Do you want to play again? (yes/no): ").lower() == "yes":
                        seceret_number = random.randint(1, 10)
                        number_of_attempts = 0
                        run(number_of_attempts)
                else :
                        print("Thank you for playing! Goodbye!")
                        exit()
              
        case _ if guess < seceret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
        case _ if guess > seceret_number:
            print("Oops, your guess is a bit high. Try again!")
        case _:
            print("Something went wrong. Please try again.")

    number_of_attempts +=1
    run(number_of_attempts)
run()