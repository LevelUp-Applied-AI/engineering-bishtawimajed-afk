def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def first_word(s):
    return s.split()[0]
