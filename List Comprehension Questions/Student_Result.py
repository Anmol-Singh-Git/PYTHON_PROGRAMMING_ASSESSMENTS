students=[
    
    {"name":"amit","marks":75},
    {"name":"rahul","marks":45},
    {"name":"neha","marks":90},
    {"name":"rohit","marks":55}
]
result=[data["name"] for data in students if data["marks"]>60]
print("name of pass student:",result)
