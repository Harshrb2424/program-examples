def rev(n):
    r = 0
    while(n > 0):
        r = r*10 + n%10
        n = n // 10
    return r

def rev_string(n):
    return str(n)[::-1]

print(rev(int(input())))
print(rev_string(int(input())))
    