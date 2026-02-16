# Program to perform all arithmetic operations on two numbers without using functions

# Get two numbers from the user
# input() reads user input as string, so we convert to float for decimal support
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the input numbers
print(f"\nFirst number: {num1}")
print(f"Second number: {num2}")
print("\n--- Arithmetic Operations ---\n")

# Addition: sum of two numbers
addition = num1 + num2
print(f"Addition: {num1} + {num2} = {addition}")

# Subtraction: difference between two numbers
subtraction = num1 - num2
print(f"Subtraction: {num1} - {num2} = {subtraction}")

# Multiplication: product of two numbers
multiplication = num1 * num2
print(f"Multiplication: {num1} × {num2} = {multiplication}")

# Division: quotient of two numbers
# We check if num2 is not zero to avoid division by zero error
if num2 != 0:
    division = num1 / num2
    print(f"Division: {num1} ÷ {num2} = {division}")
else:
    print(f"Division: Cannot divide by zero!")

# Floor Division: quotient without decimal part
# Also called integer division
if num2 != 0:
    floor_division = num1 // num2
    print(f"Floor Division: {num1} // {num2} = {floor_division}")
else:
    print(f"Floor Division: Cannot divide by zero!")

# Modulus: remainder after division
# Useful for finding remainders
if num2 != 0:
    modulus = num1 % num2
    print(f"Modulus (Remainder): {num1} % {num2} = {modulus}")
else:
    print(f"Modulus: Cannot divide by zero!")

# Exponentiation: num1 raised to the power of num2
# For example: 2 ** 3 = 2 × 2 × 2 = 8
exponentiation = num1 ** num2
print(f"Exponentiation: {num1} ^ {num2} = {exponentiation}")

# Display completion message
print("\n--- All operations completed! ---")
