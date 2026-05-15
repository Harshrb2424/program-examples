# Remove Duplicates From String
input = "programming"
freq = {}

for char in input:
    freq[char] = freq.get(char, 0) + 1

for char in freq:
    print(char, end="")
    
print()



from collections import Counter

inputs = "programming"
freq = Counter(inputs)


for char in freq:
    print(char, end="")