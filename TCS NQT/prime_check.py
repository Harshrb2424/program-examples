def prime_check(n):
    for i in range(2, n//2):
        print(i, n)
        if (n%i == 0):
            return False
    return True

a = input()
print(a)
print(prime_check(int(a)))