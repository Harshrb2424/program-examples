def rev(n):
    r = 0
    while(n > 0):
        r = r*10 + n%10
        n = n // 10
    return r

def palindrome(n):
    reverse = rev(n)
    if (n == reverse):
        return True
    else:
        return False
    
def prime(n):
    return n==n[::-1]

print(palindrome(int(input())))
print(prime(input()))