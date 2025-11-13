#Programme which asks user login username and password and then shows their marks
login_username = "Soulreaper"
correct_password = "Avengers123"
username = input(" Enter the username ")
if username == login_username:
     password = input("Enter the correct password ")
     if password == correct_password:
      print("Welcome back Rohan sharma")
     else:
        print("Enter the correct password")
else:
     print("Enter correct username")