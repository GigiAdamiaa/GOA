# 1)

# def sum_of_numbers(numbers):
#     result = 0
#     for i in numbers:
#         result = result + i
#     return result

# numbers = [1,2,3,4,5]
# print(sum_of_numbers(numbers))


# 2)

# def filter(strings_list):
#     filterd_list = []
    
#     for word in strings_list:
#         if len(word) > 5:
#             filterd_list.append(word)
#     return filterd_list

# names = ["nika" , "Gabrieli" , "Gigi" , "luka", "Giorgi"]

# print(filter(names))

# 3)

# def even_numbers(numbers):
#     even_numbers_list = []
    
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers_list.append(num)
#     return even_numbers_list    

# print(even_numbers([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
        
# 4)

# first example

# def largest_number(numbers):
#     biggest_num = numbers[0]
#     for num in numbers:
#         if biggest_num < num:
#             biggest_num = num
#     return biggest_num

# numbers = [3,8,17,45,32,98]
# print(largest_number(numbers))

# second example

# def largest_number(numbers):
#     return max(numbers)

# print(largest_number([1,2,3,4,5]))

# 5)

# def filter_list(strings_list):
#     filtered_list = []

#     for word in strings_list:
#         if word[0] == 'a':
#             filtered_list.append(word)
    
#     return filtered_list

# words = ["apple", "anaconda", "anakomi", "python", "java", "javascript"]

# print(filter_list(words))

# 6)
# def squared_numbers(numbers):
#     squared_numbers_list = []

#     for num in numbers:
#         squared_numbers_list.append(num*num)

#     return squared_numbers_list

# print(squared_numbers([2,4,5]))

# 7)

# def length_strings(strings):
#     length_list = []

#     for word in strings:
#         length_list.append(len(word))
    
#     return length_list

# print(length_strings(["Luka", "Gigi", "Giorgi"]))

# 8)

# def sum_of_numbers(numbers):
#     result = 0

#     for num in numbers:
#         if num > 10:
#             result = result + num

#     return result

# print(sum_of_numbers([3,6,4,11,15]))