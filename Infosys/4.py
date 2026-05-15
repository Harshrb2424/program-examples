# Frequency Count

input = "programming"
freq = {}
for char in input:
    freq[char] = freq.get(char, 0) + 1
print(freq)



from collections import Counter

inputs = "programming"
freq = Counter(inputs)
print(freq)