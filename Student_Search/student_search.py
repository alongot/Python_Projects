########################################
# Algorithm to find students, and retrieve name and ID
#######################################

# Create a dictionary with students information
students = {
	{"name": "Jane Smith", "id": "S002", "age": 22, "major": "Biology", "GPA": 3.5},
    {"name": "Mark Lee", "id": "S003", "age": 21, "major": "Physics", "GPA": 3.9},
    {"name": "Emily Davis", "id": "S004", "age": 23, "major": "Mathematics", "GPA": 3.8}
}

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


