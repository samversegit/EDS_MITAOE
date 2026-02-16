# Initialize a counter variable to keep track of the number of digits
count = 0

# Prompt the user to enter a number and convert the input to an integer
num = int(input("Enter a number : "))

# Convert the number to a string and iterate through each character (digit)
# str(num) converts the integer to a string, allowing us to loop through each digit
for i in str(num):
    count += 1  # Increment the counter by 1 for each digit found

# Display the total count of digits in the number
print("the number of digits in the number is : ", count)
