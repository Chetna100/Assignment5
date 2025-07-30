# 1. Create a dictionary where student names are keys and their marks are values.
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 65,
    "Eve": 95
}

# 2. Ask the user to input a student's name.
name = input("Enter the student's name: ")

# 3. Retrieve and display the corresponding marks.
# 4. If the student’s name is not found, display an appropriate message.
if name in student_marks:
    marks = student_marks[name]
    print(f"{name}'s marks: {marks}")
else:
    print(f"Student '{name}' not found")