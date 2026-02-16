# Program to convert temperature from Fahrenheit to Celsius

# Display program title
print("=== Temperature Converter: Fahrenheit to Celsius ===\n")

# Get temperature in Fahrenheit from the user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius using the formula
# Formula: Celsius = (Fahrenheit - 32) × 5/9
celsius = (fahrenheit - 32) * 5 / 9

# Display the result
print(f"\n--- Conversion Result ---")
print(f"{fahrenheit}°F = {celsius}°C")

# Optional: Display with rounded value for cleaner output
print(f"{fahrenheit}°F = {round(celsius, 2)}°C (rounded to 2 decimal places)")

# Program end message
print("\n=== Conversion Complete ===")
