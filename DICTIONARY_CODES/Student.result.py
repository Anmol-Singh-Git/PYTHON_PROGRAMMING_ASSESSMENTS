student={
    "Rahul":75,
    "Amit":32,
    "Priya":88,
    "Neha":39,
    "Rohit":55
}
for name,marks in student.items():
    if(marks>=40):
        print(name,"= pass")
    else:
        print(name,"= fail")
