def each_vowel_count(s):
    vowels = "aeiou"
    freq = {}
    for c in s:
        if c.lower() in vowels:
            freq[c.lower()] = freq.get(c.lower(), 0) + 1
    print(freq)


each_vowel_count("Hello World")