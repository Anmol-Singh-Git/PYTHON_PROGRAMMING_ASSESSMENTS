student={
    "Rahul":85,
    "Amit":32,
    "Priya":78,
    "Neha":48,
    "Rohit":55
}
for name,marks in student.items():
    if(marks>40):
        if(marks>=80):
            print(name,"excellent")  
        elif(marks>=60):
            print(name,"good") 
        elif(marks>=40):
            print(name,"average")       
    else:
        print(name,"fail")
