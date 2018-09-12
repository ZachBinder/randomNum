import random

def main():
		#variables
		attempts = 1
		randomNum = random.randint(1,10)

		#tuples
		HIGH = 10
		LOW = 1
		
		#prompts the user for their guess
		guess = int(input("Guess a number between " + str(LOW) + " and " + str(HIGH) + ": "))
		
		#while loop for if the users guess is not correct
		while(guess != randomNum):
			if(guess < randomNum):
				print("Your guess was too low...")
			else:
				print("Your guess was too high...")
			attempts += 1
			guess = int(input("Guess a number between " + str(LOW) + " and " + str(HIGH) + ": "))

		#informs the user they are correct and in how many attempts it took them
		print("CONGRATULATIONS, YOU GUESSED THE NUMBER CORRECTLY! \nIt only took you " + str(attempts) + " attempt(s)")

#runs the program
main()