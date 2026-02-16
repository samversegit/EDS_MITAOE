def find_greatest(a: int | float, b: int | float, c: int | float) -> int | float:
    """
    Takes three numbers as parameters, finds the greatest among them,
    and returns it.
    use of " | " (bitwise or operator ) is done to accept both int and float values as parameters
    Args:
        a: The first number.
        b: The second number.
        c: The third number.

    Returns:
        The greatest of the three numbers.
    """

    # First, compare a and b to find the larger of the two.
    # Then compare that result with c to determine the overall greatest.
    if a >= b and a >= c:
        # a is greater than or equal to both b and c → a is the greatest
        greatest = a
    elif b >= a and b >= c:
        # b is greater than or equal to both a and c → b is the greatest
        greatest = b
    else:
        # If neither a nor b is the greatest, c must be
        greatest = c

    return greatest


# --- Example usage ---
result1 = find_greatest(10, 25, 7)
print(f"Greatest of 10, 25, 7  → {result1}")   # 25

result2 = find_greatest(100, 45, 99)
print(f"Greatest of 100, 45, 99 → {result2}")  # 100

result3 = find_greatest(3, 3, 3)
print(f"Greatest of 3, 3, 3    → {result3}")   # 3 (all equal)

result4 = find_greatest(-5, -1, -9)
print(f"Greatest of -5, -1, -9 → {result4}")   # -1 (negative numbers)

result5 = find_greatest(1.5, 2.7, 2.1)
print(f"Greatest of 1.5, 2.7, 2.1 → {result5}") # 2.7 (floats)
