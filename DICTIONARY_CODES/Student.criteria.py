student={
    "Rahul":{"attendance":85,"marks":70 },
    "Amit":{"attendance":60,"marks":80},
    "Priya":{"attendance":90,"marks":35},
    "Neha":{"attendance":78,"marks":55}
}
for stu_name,data in student.items():
    attendance=data["attendance"]
    marks=data["marks"]
    if(attendance>=75):
        if(marks>=40):
            print(stu_name,"- Eligible")
        else:
            print(stu_name,"- Failed in Exam")
    else:
        print(stu_name,"- Not eligible")
