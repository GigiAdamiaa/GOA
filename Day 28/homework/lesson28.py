# 7 kyu

# 1) String ends with

def solution(text, ending):
    return text.endswith(ending)


# 2) Is this a triangle?

def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

# 3) Number of People in the Bus

def number(bus_stops):
    result = 0
    
    for passengers in bus_stops:
        result += passengers[0] - passengers[1]
        
    return result

# 4) Reverse words

def reverse_words(text):
    words = text.split(" ")
    
    reversed_words = []
    
    for word in words:
        reversed_words.append(word[len(word)::-1])
        
    return " ".join(reversed_words)

# 5) Make a function that does arithmetic!

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b
    


# 6 kyu


# 1) Break camelCase

def solution(s):
    result = ""
    
    for letter in s:
        if letter != letter.upper():
            result += letter
        
        elif letter == letter.upper():
            result += " " + letter
            
    return result

# 2) 

def is_prime(n):
    if n <= 0 or n == 1:
        return False
    i = 2
    while (i <= n ** 0.5 ):
        if n % i == 0:
            return False
        i += 1
    return True

# 3) Pyramid Array

def pyramid(n):
    result = []
    if n == 0:
        return result

    for n in range(1, n + 1):
        result.append([1] * n)

    return result