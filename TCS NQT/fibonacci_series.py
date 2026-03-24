def fibonacci_series(n):
    if (n == 1):
        print(0)
    elif (n == 2):
        print("0 1")
    else:
        print("0 1", end=" ")
        n = n - 2
        
        a = 0
        b = 1
        c = a + b
        while(n > 0):
            print(c, end=" ")
            a = b
            b = c
            c = a + b
            n = n - 1

fibonacci_series(int(input()))