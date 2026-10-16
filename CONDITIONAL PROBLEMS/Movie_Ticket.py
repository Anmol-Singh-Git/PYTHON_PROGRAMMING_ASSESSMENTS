seats = int(input("Enter available seats: "))

if seats > 0:
    age = int(input("Enter age: "))

    if age < 5:
        print("Ticket is Free")
    elif age <= 12:
        print("50% discount")
    elif age > 60:
        print("30% discount")
    else:
        print("Full price")
else:
    print("House Full")
