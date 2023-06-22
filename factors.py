import sys


def factorize(n):
    """
    Factorizes a number into two smaller numbers.

    Args:
        n (int): The number to factorize.

    Returns:
        str: The factorization of the number in the format "n=p*q".

    """
    factors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return '\n'.join([f"{n}={p}*{q}" for p, q in factors])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        factorization = factorize(int(number))
        print(factorization)
