#!/usr/bin/env python3
"""
Program to calculate age and timeline from birth date using datetime module
"""

from datetime import datetime

# Get birth date from user
print("=== Age Calculator ===\n")
print("Enter your birth date:")

# Input birth date
birth_day = int(input("Enter day (1-31): "))
birth_month = int(input("Enter month (1-12): "))
birth_year = int(input("Enter year (e.g., 2000): "))

# Create datetime object for birth date
birth_date = datetime(birth_year, birth_month, birth_day)

# Get current date and time
current_date = datetime.now()

# Calculate the difference
age_difference = current_date - birth_date

# Calculate age in years, months, and days
years = current_date.year - birth_date.year
months = current_date.month - birth_date.month
days = current_date.day - birth_date.day

# Adjust if current month/day is before birth month/day
if days < 0:
    months -= 1
    # Get days in previous month
    if current_date.month == 1:
        prev_month = 12
        prev_year = current_date.year - 1
    else:
        prev_month = current_date.month - 1
        prev_year = current_date.year
    
    days_in_prev_month = (datetime(prev_year, prev_month + 1, 1) - datetime(prev_year, prev_month, 1)).days if prev_month < 12 else 31
    days += days_in_prev_month

if months < 0:
    years -= 1
    months += 12

# Display results
print("\n" + "="*50)
print("YOUR AGE DETAILS")
print("="*50)

print(f"\nBirth Date: {birth_date.strftime('%B %d, %Y')}")
print(f"Current Date: {current_date.strftime('%B %d, %Y')}")

print(f"\n📅 You are exactly:")
print(f"   • {years} years, {months} months, and {days} days old")

print(f"\n⏱️  Timeline:")
print(f"   • Total days lived: {age_difference.days:,} days")
print(f"   • Total hours lived: {age_difference.days * 24:,} hours (approximately)")
print(f"   • Total minutes lived: {age_difference.days * 24 * 60:,} minutes (approximately)")
print(f"   • Total seconds lived: {age_difference.total_seconds():,.0f} seconds")

print(f"\n🎂 Age Milestones:")
print(f"   • Age in weeks: {age_difference.days // 7:,} weeks")
print(f"   • Age in months: {years * 12 + months} months (approximately)")

# Calculate next birthday
next_birthday = datetime(current_date.year, birth_month, birth_day)
if next_birthday < current_date:
    next_birthday = datetime(current_date.year + 1, birth_month, birth_day)

days_to_birthday = (next_birthday - current_date).days

print(f"\n🎉 Next Birthday:")
print(f"   • Date: {next_birthday.strftime('%B %d, %Y')}")
print(f"   • Days remaining: {days_to_birthday} days")

print("\n" + "="*50)