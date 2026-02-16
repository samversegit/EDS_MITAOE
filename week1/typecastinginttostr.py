# Program to convert integer to string and string to integer

print("=== Integer to String and String to Integer Conversion ===\n")

# --- Part 1: Integer to String Conversion ---
print("--- Converting Integer to String ---")

# Define an integer variable
num_int = 12345
print(f"Original integer: {num_int}")
print(f"Type: {type(num_int)}")

# Convert integer to string using str() function
num_string = str(num_int)
print(f"Converted to string: '{num_string}'")
print(f"Type: {type(num_string)}")

# Proof: Try concatenating with another string (only works with strings)
result = num_string + " is now a string!"
print(f"Concatenation test: {result}\n")




# --- Part 2: String to Integer Conversion ---
print("--- Converting String to Integer ---")

# Define a string variable containing numeric characters
str_num = "54321"
print(f"Original string: '{str_num}'")
print(f"Type: {type(str_num)}")

# Convert string to integer using int() function
converted_int = int(str_num)
print(f"Converted to integer: {converted_int}")
print(f"Type: {type(converted_int)}")

# Proof: Try arithmetic operation (only works with integers)
result = converted_int + 100
print(f"Arithmetic test: {converted_int} + 100 = {result}\n")




# --- Part 3: User Input Example ---
print("--- User Input Conversion Example ---")

# Get a number from user as string (input() always returns string)
user_input = input("Enter a number: ")
print(f"Your input: '{user_input}' (Type: {type(user_input)})")

# Convert the string input to integer for calculations
user_number = int(user_input)
print(f"Converted to integer: {user_number} (Type: {type(user_number)})")

# Perform calculation
doubled = user_number * 2
print(f"Double of your number: {doubled}")

# Convert result back to string
result_string = str(doubled)
print(f"Result as string: '{result_string}' (Type: {type(result_string)})\n")


