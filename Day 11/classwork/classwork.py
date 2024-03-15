registerd_password = "Gigi123"
authorized = False

while authorized != True:
    user_input = input("Please enter your password: ")
    
    if user_input == registerd_password:
        authorized = True
        print("Accses granted")
    else:
        print("Wrong password. Please try again")

