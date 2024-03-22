# 1)

# def myfunc(numbers):
#     divided_into_four = []

#     for num in numbers:
#         if num % 4 == 0:
#             divided_into_four.append(num)
#     return divided_into_four

# print(myfunc([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))

# 2)

# name = input("Please enter your name: ")
# last_name = input("Please enter your last name: ")

# def info(name):
#     user_input = []
    
#     user_input.append(name)
#     return user_input

# print(info([name,last_name]))

# 3)


# 4)

# lastname = input("Please enter your lastname: ")

# def even_index(lastname):
#     char_list = []
#     even_index_char = []

#     for char in lastname:
#         char_list.append(char)

#     for index in range(len(char_list)):
#         if index % 2 ==0:
#             even_index_char.append(char_list[index])
#     return(even_index_char)
        

# print(even_index(lastname))

# chad_ური ამოხსნა

# def even_indexes(lastname):
#     even_index_chars = []

#     for index in range(len(lastname)):
#         if index % 2 == 0:
#             even_index_chars.append(lastname[index])
    
#     return even_index_chars


# lastname = input("Please enter lastname: ")

# print(even_indexes(lastname))