# Print the title of the program
print("Even or Odd Checker")
print("-" * 30)

# Take a number input from the user and convert it to an integer
number = int(input("Enter a number: "))

# Check if the number is divisible by 2 (even) or not (odd)
if number % 2 == 0:
    # If remainder is 0, the number is even
    print(f"\n{number} is an Even number")
else:
    # If remainder is not 0, the number is odd
    print(f"\n{number} is an Odd number")