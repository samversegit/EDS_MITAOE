
"""
Program to calculate age from birth year using datetime module
"""

from datetime import datetime

# Get current year using datetime module
current_date = datetime.now()
current_year = datetime.now().year

# Get birth year from user
birth_year = int(input("Enter your birth year (e.g., 2000): "))

# Calculate age 
age = current_year - birth_year

# Display results

print(f"Current Year: {current_year}")
print(f"Birth Year: {birth_year}")
print(f"Your Age: {age} years old")


