# Print the title of the program
print("Momentum Calculator")
print("-" * 30)

# Display the formula for momentum
print("Formula: Momentum (p) = Mass (m) × Velocity (v)")
print()

# Take input for mass from the user
mass = float(input("Enter the mass (in kg): "))

# Take input for velocity from the user
velocity = float(input("Enter the velocity (in m/s): "))

# Calculate momentum using the formula p = m × v
momentum = mass * velocity

# Display the calculated momentum
print(f"\nThe momentum is: {momentum} kg·m/s")