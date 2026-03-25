def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("madam"))

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("listen", "silent"))

from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1

    return v_count, c_count

v, c = count_vowels_consonants("hello world")
print("Vowels:", v)
print("Consonants:", c)

print(ord('A'))  # 65
print(chr(65))  # 'A'

def shift_string(s, shift):
    result = ""
    for char in s:
        result += chr(ord(char) + shift)
    return result

print(shift_string("abc", 1))

def toggle_case(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

print(toggle_case("Hello World"))

def clean_string(s):
    return ''.join(char for char in s if char.isalpha())

print(clean_string("h3llo!@#"))

from collections import Counter

def string_operations(s1, s2):
    print("Palindrome:", s1 == s1[::-1])
    print("Anagram:", Counter(s1) == Counter(s2))

    vowels = "aeiouAEIOU"
    v = sum(1 for c in s1 if c in vowels)
    c = sum(1 for c in s1 if c.isalpha() and c not in vowels)

    print("Vowels:", v)
    print("Consonants:", c)

    print("ASCII values:", [ord(c) for c in s1])

string_operations("listen", "silent")