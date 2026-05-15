# Second Largest Element

arr = [2,71,11,15]

def secBig(arr):
    f = float('-inf')
    s = float('-inf')
    
    for i in arr:
        if i > f:
            s = f
            f = i
        elif i > s:
            s = i
    print(s)

secBig(arr)