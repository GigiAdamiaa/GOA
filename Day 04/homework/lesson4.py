#დავპრინტოთ ორი რიცხვის ჯამი
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
print(int(number1) + int(number2))

#დავპრინტოთ მომხმარებლის სახელი, რამდენი წლისაა, და მომავალში რამდენი წლის შემდეგ უნდა დროში მოგზაურობა
name = input("Please enter your name: ")
print(name)

age = input("Please enter your age: ")
print(age)

time_travel = input("How many years into the future do you want to time travel?: ")
print(time_travel)

print("Your age in the future: " + str(int(age) + int(time_travel)))