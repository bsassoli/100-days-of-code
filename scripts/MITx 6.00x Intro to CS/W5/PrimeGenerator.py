def genPrimes():
    n = 2

    def check_is_prime(n):
        checklist = [(n % i) != 0 for i in range(2, n)]
        a = int(sum(checklist))
        return a == n-2
    while True:
        if check_is_prime(n):
            yield(n)
        n += 1


a = genPrimes()
for i in range(3, 29000):
    print(a.__next__())
