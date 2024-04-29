# def manual_sum(number_list, starting_value = 0):
#     result = starting_value

#     for num in number_list:
#         result += num

#     return result

# print(manual_sum([1,2,3,4,5]))

# CodeWars

# 1) Find Maximum and Minimum Values of a List

# def minimum(arr):
#     min_value = arr[0]

#     for num in arr:
#         if min_value > num:
#             min_value = num
    
#     return min_value 

# def maximum(arr):
#     max_value = arr[0]

#     for num in arr:
#         if max_value < num:
#             max_value = num

#     return max_value


# 2) Returning Strings

# def greet(name):
#     return f"Hello, {name} how are you doing today?"

# 3) Double Char

# def double_char(s):
#     double_string = ""
    
#     for char in s:
#         double_string += char * 2
        
#     return double_string

# 4) Filter out the geese

# def goose_filter(birds):
#     geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
#     filtered = []
    
#     for bird in birds:
#         if bird not in geese:
#             filtered.append(bird)
            
#     return filtered

# 5) Difference of Volumes of Cuboids

# def find_difference(a, b):
#     multiplication_a = a[0] * a[1] * a[2]
#     multiplication_b = b[0] * b[1] * b[2]
#     difference = multiplication_a - multiplication_b
    
#     if difference < 0:
#         return difference * -1
    
#     return difference

# 6) Is it a palindrome?

# def is_palindrome(s):
#     s = s.lower()
#     return s == s[:: -1]

# 7) Sentence Smash

# def smash(words):
#     return " ".join(words)

# 8) Pirates!! Are the Cannons ready!??

# ეს ვერ გავიგე <3

# 9) 

# 10)Friend or Foe?

# def friend(x):
#     my_friends = []
    
#     for i in x:
#         if len(i) == 4:
#             my_friends.append(i)
            
#     return my_friends