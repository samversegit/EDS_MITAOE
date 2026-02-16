def find_greatest(a: int | float, b: int | float) -> int | float:
    """
    Takes two numbers as parameters, finds the greatest among them,
    and returns it.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The greatest of the two numbers.
    """

    # Compare a and b:
    # If a is greater than or equal to b → a is the greatest
    # Otherwise → b is the greatest
    if a >= b:
        greatest = a
    else:
        greatest = b

    return greatest


# --- Example usage ---
result1 = find_greatest(10, 25)
print(f"Greatest of 10 and 25   → {result1}")   # 25

result2 = find_greatest(100, 45)
print(f"Greatest of 100 and 45  → {result2}")   # 100

result3 = find_greatest(7, 7)
print(f"Greatest of 7 and 7     → {result3}")   # 7 (both equal)

result4 = find_greatest(-5, -1)
print(f"Greatest of -5 and -1   → {result4}")   # -1 (negative numbers)

result5 = find_greatest(1.5, 2.7)
print(f"Greatest of 1.5 and 2.7 → {result5}")   # 2.7 (floats)