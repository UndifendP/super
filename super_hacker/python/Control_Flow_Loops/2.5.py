number=100
for n in range(2, number + 1):
    isPrime = True
    for i in range(2, n - 1):
        if n % i == 0:
            isPrime = False
    if isPrime:
        print(n)
