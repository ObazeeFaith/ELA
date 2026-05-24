
def multiplication_table(n=5):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:3}", end=" ")
        print()


def triangle(n=5):
    for i in range(1, n + 1):
        for _ in range(i):
            print("*", end="")
        print()


def iterate_matrix(matrix):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            print(f"matrix[{i}][{j}] = {val}")
    print()


if __name__ == "__main__":
    print("Multiplication table (1..5):")
    multiplication_table(5)

    print("\nTriangle pattern:")
    triangle(5)

    print("\nIterating a 2D list:")
    m = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    iterate_matrix(m)
