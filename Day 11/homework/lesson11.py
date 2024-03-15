#1)

num = float(input("Please enter number: "))
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is zero")

#2)

for i in range(1,20 + 1):
    if i % 2 ==0:
        print(i, "is even")
    else:
        print(i, "is odd")

#3)

# first example
number = int(input("Enter number: "))

sum = 0
i = 0

while i <=  number:
    sum = sum + i 
    i = i + 1

print(sum)

# second example

result = 0

while number >= 0:
    result = result + number
    number = number - 1

print(result)


# #4)
registered_pincode = 1234
authorized = False

while authorized != True: 
    user_input = int(input("Please enter your pincode: "))

    if user_input == registered_pincode:
        print("Accses granted")
        authorized = True
    else:
        print("Please tray again")

#5)
        
username = input("Please enter your name: ")
password = input("Please enter your password: ")

if username == "admin" and password == "password123":
    print("Login successful")

else:
    print("Your Login is faild")


# 6)
    
age = int(input("Please enter age: "))

if age < 13:
    print("You are child")
elif age < 20:
    print("You are teenager")
else:
    print("You are adult")