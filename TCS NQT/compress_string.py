def compress_string(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result

print(compress_string("aaabbc"))


def matrix_add(A, B):
    rows = len(A)
    cols = len(A[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(matrix_add(A, B))

def move_zeros(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    for i in range(count, len(arr)):
        arr[i] = 0

    return arr


print(move_zeros([4, 5, 0, 1, 9, 0]))

def move_zeros(arr):
    j = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr


print(move_zeros([4, 5, 0, 1, 9, 0]))