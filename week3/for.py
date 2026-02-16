# Initialize a counter variable (note: this will be overwritten by the for loop)
i = 1 

# Prompt the user to enter a number and convert the input to an integer
num = int(input("Enter a number: "))

# Loop through numbers from 1 to num-1 (num is excluded in range())
# The variable i takes each value in the range during each iteration
for i in range(1, num):
    print(i, end=" ")  # Print i followed by a space instead of a newline
    
# Print a newline character (\n) followed by "Done!" to move to the next line
print("\nDone!")

# Alternative way to print numbers in new lines
# This commented section shows a different formatting approach
'''
# Initialize counter variable
i = 1

# Loop through numbers from 1 to num-1
for i in range(1, num):
    print(i)  # Print each number on a new line (default behavior)

# Print completion message
print("Done!")
'''