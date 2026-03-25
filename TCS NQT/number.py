def floyd(n):
    s = 1
    for i in range(n+1):
        for j in range(i):
            print(s, end=" ")
            s+=1
        print()

def binary_triangle(n):
    for i in range(n+1):
        for j in range(i):
            print((i+j)%2, end=" ")
        print()

def diamond(n):
    for i in range(n):
        m = n//2
        for j in range(n):
            if (j+i < m) or (j-i > m): print(" ", end=" ")
            else: print("*", end=" ")
        print()

n = int(input())
floyd(n)
print()
binary_triangle(n)
print()
diamond(n)