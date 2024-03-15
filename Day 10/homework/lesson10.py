correct_username = "gigi"
correct_password = "1234"

entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

while (
      entered_username != correct_username
      or entered_password != correct_password
  ):
      print("Your username or password doesn't match. Please try again.")
    
      entered_username = input("Enter your username: ")
      entered_password = input("Enter your password: ")

print("Access granted")