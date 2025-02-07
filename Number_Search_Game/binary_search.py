############
#Function to implement number search
############

def binary_search_game():
	print("Think of a number between 1-100, and I'll try to guess it")

	low = 1
	high = 100

	attempts = 0

	while low <= high:
		attempts += 1
		guess = (low + high) // 2

		print(f"Is your number {guess}?")
		user_guess = input("Enter h if higher, enter l if lower, c if correct: ")

		if user_guess not in ['h', 'l', 'c']:
			print("Invalid input try again! ")
			user_guess = input("Enter h if higher, enter l if lower, c if correct: ")

		if user_guess == "h":
			low = guess + 1
		elif user_guess == "l":
			high = guess - 1
		else:
			print (f"Guessed after {attempts} attempts. Your number is {guess}.")
			return 
	
		

		
