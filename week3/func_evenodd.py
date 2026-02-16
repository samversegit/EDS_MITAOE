def check_even_or_odd(number: int) -> None:
    """
    Determines whether a given integer is even or odd and prints the result.

    A number is even if it is divisible by 2 (i.e., has no remainder when divided by 2).
    A number is odd if it is not divisible by 2 (i.e., has a remainder of 1).

    Args:
        number: The integer value to check.
    """

    # The modulo operator (%) returns the remainder of a division.
    # If number % 2 == 0, the number divides evenly by 2 → it's even.
    # If number % 2 != 0, there's a remainder of 1 → it's odd.
    # This works correctly for negative numbers too, since -3 % 2 == 1 in Python.
    if number % 2 == 0:
        return "The given no is Even"
    else:
        return "the given no is Odd"


# --- Example usage ---
print(check_even_or_odd(12))#even
print(check_even_or_odd(3))#odd
print(check_even_or_odd(-5))#odd
print(check_even_or_odd(0))#even 0 is div by 2

