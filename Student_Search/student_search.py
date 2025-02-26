########################################
# Algorithm to find students, and retrieve name and ID
#######################################

# Import pprint library
import pprint

# Create a dictionary with students information
students = [
    {"name": "Jane Smith", "id": "S002", "age": 22, "major": "Biology", "GPA": 3.5},
    {"name": "Mark Lee", "id": "S003", "age": 21, "major": "Physics", "GPA": 3.9},
    {"name": "Emily Davis", "id": "S004", "age": 23, "major": "Mathematics", "GPA": 3.8},
    {"name": "Michael Brown", "id": "S005", "age": 24, "major": "Computer Science", "GPA": 3.7},
    {"name": "Sarah Johnson", "id": "S006", "age": 20, "major": "Chemistry", "GPA": 3.6},
    {"name": "David Wilson", "id": "S007", "age": 22, "major": "Electrical Engineering", "GPA": 3.4},
    {"name": "Laura Martinez", "id": "S008", "age": 25, "major": "Mechanical Engineering", "GPA": 3.9},
    {"name": "James Anderson", "id": "S009", "age": 21, "major": "Political Science", "GPA": 3.3},
    {"name": "Olivia Taylor", "id": "S010", "age": 22, "major": "Economics", "GPA": 3.8},
    {"name": "Daniel White", "id": "S011", "age": 23, "major": "History", "GPA": 3.2},
    {"name": "Sophia Harris", "id": "S012", "age": 20, "major": "Environmental Science", "GPA": 3.7},
    {"name": "Ethan Clark", "id": "S013", "age": 24, "major": "Software Engineering", "GPA": 3.5},
    {"name": "Isabella Lewis", "id": "S014", "age": 21, "major": "Philosophy", "GPA": 3.6},
    {"name": "Benjamin Walker", "id": "S015", "age": 22, "major": "Data Science", "GPA": 3.9},
    {"name": "Ava Hall", "id": "S016", "age": 23, "major": "Art History", "GPA": 3.3}
]


# Function to search for students
def linear_search(students, search_term, search_type = "name"):
	# Loop through each student in the list
    for student in students:
        # Check if the search type matches and if the student matches the search term
        if search_type == "name" and student["name"].lower() == search_term.lower():
            return student
        elif search_type == "id" and student["id"].lower() == search_term.lower():
            return student
        elif search_type == "age" and str(student["age"]) == search_term:
            return student
        elif search_type == "major" and student["major"].lower() == search_term.lower():
            return student
        elif search_type == "gpa" and str(student["GPA"]) == search_term:
            return student
    return None  # Return None if the student is not found

## Greeting function to find student
def find_student():
	print("Welcome to student finder, we can locate students based on name, id, age, major, and GPA")

	show_full_list = input("If you want to see full list of student, type list: ").strip().lower()
	
	if show_full_list not in ['list', 'List', 'l']:
		while True:
			try:
				search_type = input("Please enter an option (name, id, age, major, gpa): ").strip().lower()

				if search_type not in ['name', 'id', 'age', 'major', 'gpa']:
					raise ValueError("Invalid choice, please enter a valid option.")

			except ValueError as e:
				print(e)  # Display error message and retry
				continue

			while True:
				try:
					if search_type in ['age', 'gpa']:
						search_term = float(input(f"Please enter the student's {search_type}: "))  # Ensure numeric input
					elif search_type == 'id':
						search_term = int(input("Please enter the student's ID: "))  # Ensure ID is an integer
					else:
						search_term = input(f"Please enter the student's {search_type}: ").strip()
					break
				except ValueError:
					print("Invalid input, please enter a number where required.")
					
				

			student = linear_search(students, search_term, search_type)

			if student:
				print("\nStudent Found!")
				print(f"Name: {student['name']}")
				print(f"ID: {student['id']}")
				print(f"Age: {student['age']}")
				print(f"Major: {student['major']}")
				print(f"GPA: {student['GPA']}")

			else:
				print("\nStudent not found.")

			retry = input("Would you like to find another student (Yes or No): ").strip().lower()
			
			if retry not in ['yes', 'Yes', 'y']:
				print("Program exiting, have a wonderful day!")
				break
	else:
		pprint.pprint(students)
		find_student()

				


