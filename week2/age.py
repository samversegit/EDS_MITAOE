# Print the title of the program
print("Life Stage Determiner")
print("-" * 30)

# Take age input from the user and convert it to an integer
age = int(input("Enter your age: "))

# Check if age is negative (invalid input)
if age < 0:
    print("\nInvalid age! Age cannot be negative.")

# Check if age is between 0 and 2 (Infant stage)
elif age <= 2:
    print("\nYour life stage is: Infant")

# Check if age is between 3 and 12 (Child stage)
elif age <= 12:
    print("\nYour life stage is: Child")

# Check if age is between 13 and 19 (Teenager stage)
elif age <= 19:
    print("\nYour life stage is: Teenager")

# Check if age is between 20 and 39 (Young Adult stage)
elif age <= 39:
    print("\nYour life stage is: Young Adult")

# Check if age is between 40 and 59 (Middle-Aged Adult stage)
elif age <= 59:
    print("\nYour life stage is: Middle-Aged Adult")

# Check if age is between 60 and 79 (Senior stage)
elif age <= 79:
    print("\nYour life stage is: Senior")

# If age is 80 or above (Elderly stage)
else:
    print("\nYour life stage is: Elderly")
