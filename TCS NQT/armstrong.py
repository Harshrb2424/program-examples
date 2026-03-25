def armstrong(n):
    arm = 0
    num = n
    while(n > 0):
        arm = arm + (n%10)**3
        n = n // 10
    return arm == num

print(armstrong(int(input())))