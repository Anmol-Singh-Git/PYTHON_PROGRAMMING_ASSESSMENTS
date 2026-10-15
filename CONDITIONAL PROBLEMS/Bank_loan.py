print("A bank gives a loan based on:")
age=int(input("enter age:"))
if(age>=21):
    print("age is valid")
    sal=float(input("enetr your salary:"))
    if(sal>=25000):
        print("salary is valid:")
        credit_score=int(input("enetr your credit score:"))

        if(credit_score>=750):
            print("loan approved")
        elif(credit_score>=650):
            print("loan approved with higer interest:")
        else:
            print("loan rejected:")
    else:
        print("salary is to low:")
else:
    print("age is not valid for loan")        
