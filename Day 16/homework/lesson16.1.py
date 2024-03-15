# Multipies of 3 or 5 

def solution(number):
    sum = 0
    for i in range(1,number):
        if (i % 3 == 0 or i % 5 == 0):
            sum = sum + i
    return sum

# Vowels count

def get_count(sentence):
    num_vowels = 0
    vowels = "aeiou"
    for i in sentence:
        if i in vowels:
            num_vowels = num_vowels + 1
    return num_vowels

# Convert a number to a string

def number_to_string(num):
    return str(num)

# square of digits

def square_digits(num):
    nums = [int(x) for x in str(num)]
    string = ""
    for i in nums:
        string  = string + str(i*i)
    return int(string)

# unique in order

def unique_in_order(sequence):
    unique_list = []
    prev = None
    for i in sequence:
        if i != prev:
            unique_list.append(i)
        prev = i
    return unique_list