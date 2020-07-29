def genPrimes():
    n = 2

    def check_is_prime(n):
        return sum([(n % i) != 0 for i in range(2, n)]) == n-2
    while True:
        if check_is_prime(n):
            yield(n)
        n += 1


a = genPrimes()
for i in range(1, 20):
    print(a.__next__())
