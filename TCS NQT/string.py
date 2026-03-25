from collections import Counter

# def count_vowels(s):
#     a = "aeiou"
#     c = 0
#     for i in s:
#         if i in a:
#             c+=1
#     return c

# print(count_vowels(str(input())))

# def remove_space(s):
#     a = str(s).split()
#     return "".join(a)

# print(remove_space(str(input())))

def con(s):
    count = Counter(s)
    return count

print(con(str(input())))