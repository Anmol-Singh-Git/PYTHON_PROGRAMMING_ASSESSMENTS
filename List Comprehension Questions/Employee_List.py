
employees=[
    
    {"name":"Amit","department":"IT"},
    {"name":"Rahul","department":"HR"},
    {"name":"Neha","department":"IT"},
    {"name":"Rohit","department":"SALES"}
]
result=[data["name"] for data in employees if data["department"]=="IT"]
print(result)
