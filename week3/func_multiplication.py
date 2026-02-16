def multiplication_table(n: int) -> None:
    """
    Takes an integer as a parameter and prints its
    multiplication table from 1 to 10.

    Args:
        n: The integer whose multiplication table is to be printed.
    """

    print(f"Multiplication Table of {n}")
    print("-" * 25)

    # Loop from 1 to 10 (inclusive) using range(1, 11)
    # In each iteration, multiply n by the current loop value (i)
    # and print the result in a formatted table style
    for i in range(1, 11):
        result = n * i
        print(f"  {n}  x  {i:2}  =  {result}")


# --- Example usage ---
multiplication_table(5)
print()
multiplication_table(12)