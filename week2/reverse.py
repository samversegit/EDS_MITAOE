# Print the title of the program
print("Reverse an Integer using Typecasting")
print("-" * 40)

# Take an integer input from the user
number = int(input("Enter an integer: "))

# Convert the integer to a string (typecasting)
number_string = str(number)

# Reverse the string using slicing
reversed_string = number_string[::-1]

# Convert the reversed string back to an integer (typecasting)
reversed_number = int(reversed_string)

# Display the reversed integer
print(f"\nOriginal number: {number}")
print(f"Reversed number: {reversed_number}")