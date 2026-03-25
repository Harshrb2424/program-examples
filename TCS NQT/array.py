a = [3, 52, 53, 23, 53]
array = list(map(int, input().split()))

def max(array):
    max = array[0]
    for i in array:
        if i > max:
            max = i

    return max

def max2(array):
    max1 = max(array)
    max2 = array[0]
    for i in array:
        if i > max2 and i < max1:
            max2 = i

    return max2

def sum(array):
    sum = 0
    for a in array:
        sum += a
    return sum

def rotate(array, n=1):
    while(n > 0):
        l = len(array)
        last = array[l-1]
        for i in range(l-1, 0, -1):
            array[i] = array[i-1]
        array[0] = last
        n-=1
    return array

print(max(a))
print(max2(a))
print(max(array))
print(max2(array))
print(a)
print(a[::-1])
print(array)
print(array[::-1])
print(sum(a))
print(sum(array))
print(a)
print(rotate(a, 2))
print(array)
print(rotate(array, 2))
