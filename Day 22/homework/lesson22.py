# Codewars 8 kyu

# 1) Invert Values

# def invert(lst):
#     mylist = []
#     for num in lst:
#         num = num * -1
#         mylist.append(num)
        
#     return mylist

# 2) How good are you really?

# def better_than_average(class_points, your_points):
#     average_points = sum(class_points) / len(class_points)
#     return your_points > average_points

# 3) Century From Year

# def century(year):
#     century = year // 100
#     if year % 100 == 0:
#         return century
    
#     return century + 1

# 4) Convert a string to an array

# def string_to_array(s):
#     return s.split(" ")

# 5) Remove exclamation marks

# def remove_exclamation_marks(s):
#     if "!" in s:
#         s = s.replace("!", "")
        
#     return s

# Codewars 7 kyu

# 1) List Filtering

# def filter_list(l):
#     myarr = []
    
#     for i in l:
#         if type(i) != str:
#             myarr.append(i)
    
#     return myarr

# 2) Is this a triangle?

# def is_triangle(a, b, c):
#     return a + b > c and b + c > a and a + c > b

# 3) Shortest Word 

# def find_short(s):
#     return min([len(word) for word in s.split()])

# 4) Remove the minimum

# def remove_smallest(numbers):
#     if len(numbers) < 2:
#         return []
    
#     else:
#         nums = numbers.copy()
#         nums.remove(min(numbers))
#         return nums

# 5) Leap Years

# def is_leap_year(year):
#     leap = False
    
#     if year % 400 == 0:
#         leap = True
#     elif year % 4 == 0 and year % 100 != 0:
#         leap = True
    
#     return leap