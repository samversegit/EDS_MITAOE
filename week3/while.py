# Initialize a counter variable starting at 1
i = 1

# Prompt the user to enter a number and convert the input to an integer
num = int(input("Enter a number: "))

# Loop from 1 to num (inclusive)
# The loop continues while i is less than num+1
while i < num + 1:
    print(i)  # Print the current value of i
    i += 1    # Increment i by 1 for the next iteration

# Print a completion message after the loop finishes
print("Done!")



'''
**What this program does:**
- Takes a number as input from the user
- Prints all numbers from 1 to that number (inclusive)
- Displays "Done!" when finished

**Example:** If the user enters `5`, the output will be:
```
Enter a number: 5
1
2
3
4
5
Done!
'''

