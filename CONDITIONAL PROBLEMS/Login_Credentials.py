username = input("Enter username: ")
password = input("Enter password: ")

if username == "kunal":
    if password == "1234":
        role = input("Enter role:")

        if role == "admin":
            print("Full Access")
        elif role == "teacher":
            print("Teacher Dashboard")
        elif role == "student":
            print("Student Dashboard")
        else:
            print("Invalid Role")
    else:
        print("Wrong Password")
else:
  print("Invalid Username")  
