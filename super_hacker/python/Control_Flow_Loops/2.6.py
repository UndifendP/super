attmps = 3
while attmps > 0:
    print("You have", attmps, "attempts left.")
    userText = input("Enter your password: ")
    if userText == "password":
        print("You have successfully logged in.")
        break
    else:
        print("Incorrect password.")
        attmps -= 1
