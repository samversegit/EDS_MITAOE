
"""
Program to print current date and time using datetime module
"""

# Import the datetime module
from datetime import datetime
# import datetime

# Get current date and time using now() function
current_datetime = datetime.now()
current_year = datetime.now().year
# Print the current date and time
print("Current Date and Time:")
print(current_datetime)
print("Current year :")
print(current_year)
print("Current month:",datetime.now().month)
print("Current Date : ")





















































'''
# You can also format it in different ways:
print("\nFormatted outputs:")
print(f"Date: {current_datetime.date()}")
print(f"Time: {current_datetime.time()}")
print(f"Formatted: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Custom format: {current_datetime.strftime('%B %d, %Y at %I:%M:%S %p')}")
'''