def factorize(n):
    factors = []
    for i in range(2, n):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

with open('file.txt') as f:
    for line in f:
        n = int(line.strip())
        print(f"{n}=", end="")
        factors = factorize(n)
        print("=".join(str(f) for f in factors))
