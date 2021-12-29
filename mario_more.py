while True:
    n = int(input("Height: "))
    width = n

    if n > 0 and n <= 8:
        break

for num_of_hashes in range(1, n + 1):

    num_of_spaces = n - num_of_hashes

    print(" " * num_of_spaces, end="")

    print("#" * num_of_hashes, end="")

    print("  ", end="")

    print("#" * num_of_hashes)
