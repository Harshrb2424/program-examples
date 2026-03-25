def right_angle(n):
    for i in range(n+1):
        for j in range(i):
            print("*", end=" ")
        print()

def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1: print("*", end=" ")
            elif j == 0 or j == n-1: print("*", end=" ")
            else: print(" ", end=" ")
        print()

n = int(input())
right_angle(n)
print()
square(n)
print()
hollow_square(n)