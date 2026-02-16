# Program to calculate the area of a square without using functions

# Get the side length from the user
# input() function reads user input as a string, so we convert it to float
side_length = float(input("Enter the side length of the square: "))

# Calculate the area of the square
# Formula: Area = side * side (or side²)
area = side_length * side_length

# Display the result to the user
# We use an f-string for formatted output
print(f"The area of the square with side {side_length} is: {area}")

# Alternative way to calculate area using the power operator
# area = side_length ** 2

# You can also add validation to ensure positive values
# if side_length > 0:
#     area = side_length * side_length
#     print(f"The area of the square is: {area}")
# else:
#     print("Error: Side length must be positive!")