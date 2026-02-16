"""
Student Grading System
Calculates aggregate marks and assigns grades based on specific criteria
"""

def calculate_grade(marks_list, aggregate_percentage):
    """
    Calculate grade based on the following criteria:
    - If marks < 40 in any course: FAIL
    - If aggregate < 40: FAIL
    - If marks > 75 in all courses: DISTINCTION
    - If marks between 60-75: FIRST DIVISION
    - If marks between 50-60: SECOND DIVISION
    - If marks between 40-50: THIRD DIVISION
    
    Parameters:
    marks_list: list of marks for all courses
    aggregate_percentage: aggregate percentage of all courses
    
    Returns:
    grade: string containing the grade
    """
    
    # Check if any course has marks less than 40
    for marks in marks_list:
        if marks < 40:
            return "FAIL"
    
    # Check if aggregate is less than 40
    if aggregate_percentage < 40:
        return "FAIL"
    
    # Check if all marks are greater than 75
    if all(marks > 75 for marks in marks_list):
        return "DISTINCTION"
    # Check grade based on aggregate percentage
    if aggregate_percentage >= 60 and aggregate_percentage <= 75:
        return "FIRST DIVISION"
    elif aggregate_percentage >= 50 and aggregate_percentage < 60:
        return "SECOND DIVISION"
    elif aggregate_percentage >= 40 and aggregate_percentage < 50:
        return "THIRD DIVISION"
    elif aggregate_percentage > 75:
        return "DISTINCTION"
    
    return "FAIL"
'''
End of function defnition . From here we start taking desired inputs and perform possible 
operations on it 

'''

# Get number of courses
num_courses = int(input("Enter the number of courses: "))

# Initialize list to store marks
marks_list = []

# Get marks for each course using for loop
print("\nEnter marks for each course (out of 100):")
for i in range(num_courses):
    marks = float(input(f"Course {i+1}: "))
    marks_list.append(marks) # add the input marks into 

# Calculate aggregate marks and percentage
total_marks = sum(marks_list)
max_possible_marks = num_courses * 100
aggregate_percentage = (total_marks / max_possible_marks) * 100

# Call the grading function and pass parameters
grade = calculate_grade(marks_list, aggregate_percentage)

# Display results with mrks in each course and aggregate percentage with grade

print(f"Number of Courses: {num_courses}")
print(f"\nMarks obtained in each course:")
#for i, marks in enumerate(marks_list, 1):
   # print(f"  Course {i}: {marks}")
for i in range(num_courses):
    # We add + 1 because range starts at 0 (ie the defualt indexing in python)
    print(f"Course {i + 1}: {marks_list[i]}")

print(f"\nTotal Marks: {total_marks} out of {max_possible_marks}")
print(f"Aggregate Percentage: {aggregate_percentage:.2f}%")
print(f"\nGrade: {grade}")
