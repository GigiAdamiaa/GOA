# 1)

# i = 0
# while i <= 10:
#     print(i)
#     i = i + 1

# 2)

# for i in range(1,10 + 1):
#     if i % 2 ==0:
#         print(i)

# 3)

# num = int(input("Please enter number: "))

# if num < 0:
#     print(f"{num} is negative")
# elif num > 0:
#     print(f"{num} is positive")
# else:
#     print("Numer is zero")

# 4)

# correct_password = "abc123"
# inputed_password = input("Please enter your password: ")

# if correct_password == inputed_password:
#     print("Accses  granted")
# else:
#     print("Wrong password")

# 5)

# i = 0
# while i <= 10:
#     print(i)       #დაუსრულრბრლია
#     i = i + 1

# 6 )

# num = int(input("Enter number between 1 an 5: "))

# if num < 1:
#     print("Invalid input")
# elif num > 5:
#     print("Invalid input")
# else:
#     print("Valid input")

# 7)

num = int(input("Please enter number: "))

if num % 3 ==0:
    print("Fizz")
elif num % 5 ==0:
    print("Buzz")
elif num / 3 and num / 5:
    print("FizzBuzz")
else:
    print(num)