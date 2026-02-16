# Program to calculate the speed of a vehicle in m/s

# Display program title
print("=== Vehicle Speed Calculator ===\n")

# Get distance traveled from the user
# Distance should be in meters
distance = float(input("Enter the distance traveled (in meters): "))

# Get time taken from the user
# Time should be in seconds
time = float(input("Enter the time taken (in seconds): "))

# Check if time is not zero to avoid division by zero error
if time > 0:
    # Calculate speed using the formula: Speed = Distance / Time
    # Speed will be in meters per second (m/s)
    speed = distance / time
    
    # Display the result
    print(f"\n--- Result ---")
    print(f"Distance traveled: {distance} meters")
    print(f"Time taken: {time} seconds")
    print(f"Speed of the vehicle: {speed} m/s")
    
    # Optional: Convert speed to km/h for better understanding
    # To convert m/s to km/h, multiply by 3.6
    speed_kmh = speed * 3.6
    print(f"Speed in km/h: {speed_kmh} km/h")
    
else:
    # Error message if time is zero or negative
    print("\nError: Time must be greater than zero!")

# Program end message
print("\n=== Calculation Complete ===")
