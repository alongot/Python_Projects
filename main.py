
## Simple Python Calculator Application
# ************************************
# 1. Add
# 2. Substract 
# 3. Multipy 
# 4. Divide

# Import the operators, from operators.py
from Operators import * 

if __name__ == '__main__':
	
	while True:
		# Get user input
		user_input = input("Pick an arithmetic operator: ")
		if user_input not in ('+', '-', '*', '/'):
			print("Try again, pick an operator")
			continue

		if user_input in ('+', '-', '*', '/'):
			try:
				num1 = float(input("Enter first number: "))
				num2 = float(input("Enter second number: "))
			except ValueError:
				print("Invalid input, please enter a number")
				continue
		
		# Match operator that user requested
		if user_input == '+':
			print(num1, "+", num2, "=", add(num1, num2))
		elif user_input == '-':
			print(num1, "-", num2, "=", subtract(num1, num2))
		elif user_input == '*':
			print(num1, "+", num2, "=", multiply(num1, num2))
		elif user_input == '/':
			print(num1, "/", num2, "=", divide(num1, num2))

		# Check if user want to continue

		user_input_new = input("Do you want to continue (yes/no)? ")
		if user_input_new == "no":
			break
	else:
		print("Try again, invalid input")