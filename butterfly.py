def print_butterfly_pattern(num_rows):
    # Upper half of the butterfly
    for i in range(1, num_rows + 1):
        # Print left stars
        print("*" * i, end="")
        # Print spaces
        print(" " * (2 * (num_rows - i)), end="")
        # Print right stars
        print("*" * i)

    # Lower half of the butterfly
    for i in range(num_rows - 1, 0, -1):
        # Print left stars
        print("*" * i, end="")
        # Print spaces
        print(" " * (2 * (num_rows - i)), end="")
        # Print right stars
        print("*" * i)

# Example usage:
rows = int(input("Enter the number of rows for the butterfly pattern: "))
print_butterfly_pattern(rows)
