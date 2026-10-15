employee={
    "Rahul":{"salary":60000,"department":"IT"},
    "Amit":{"salary":40000,"department":"HR"},
    "Priya":{"salary":70000,"department":"IT"},
    "Neha":{"salary":45000,"department":"Finance"}
}
for name,data in employee.items():
    sal=data["salary"]
    dept=data["department"]
    if(sal>=50000):
        if(dept=="IT"):
            print(name,"senior IT employee")
        elif(dept=="HR") :
            print(name,"senior HR employee") 
        elif(dept=="finance"):
            print(name,"senior finance employee") 
        else:
            print(name,"senior employee")    
    else:
        print(name,"junior employee")
