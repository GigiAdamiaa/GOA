# 1)

# def grow(arr):
#     result = 1

#     for i in arr:
#         result *= i

#     return result

# print(grow([1,2,3,4]))

# 2)

# def bmi(weight, height):
#     bmi1 = weight / (height ** 2)
    
#     if bmi1 <= 18.5:
#         return "Underweight"
#     elif bmi1 <= 25.0:
#         return "Normal"
#     elif bmi1 <= 30.0:
#         return "Overweight"
#     else:
#         return "Obese"

# 3)

# def get_count(sentence):
#     vowel_count = 0
#     vowel = "aeiou"
    
#     for i in sentence:
#         if i in vowel:
#             vowel_count = vowel_count + 1
            
#     return vowel_count

# 4)

# def square_digits(num):
#     nums = [int(x) for x in str(num)]
#     string = ""
    
#     for i in nums:
#         string = string + str(i*i)
        
#     return int(string)

# 5)


# 6)

# def likes(names):
#     num_likes = len(names)
#     if num_likes == 0:
#         return "no one likes this"
#     elif num_likes == 1:
#         return f"{names[0]} likes this"
#     elif num_likes == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif num_likes == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         others = num_likes - 2
#         return f"{names[0]}, {names[1]} and {others} others like this"

# 7)

# def solution(number):
#     sum = 0
#     for i in range(1,number):
#         if (i % 3 == 0 or i % 5 ==0):
#             sum = sum + i
#     return sum