# Print the title of the program
print("Find the Greatest Number Among Three")
print("-" * 40)

# Take input of three numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Check which number is the greatest using if-elif-else statements
if num1 >= num2 and num1 >= num3:
    # If num1 is greater than or equal to both num2 and num3
    print(f"\n{num1} is the greatest number")
elif num2 >= num1 and num2 >= num3:
    # If num2 is greater than or equal to both num1 and num3
    print(f"\n{num2} is the greatest number")
else:
    # If num3 is the greatest number
    print(f"\n{num3} is the greatest number")