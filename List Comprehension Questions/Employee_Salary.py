employees=[
    
    {"name":"Amit","department":"IT","salary":55000},
    {"name":"Rahul","department":"HR","salary":70000},
    {"name":"Neha","department":"IT","salary":80000},
    {"name":"Rohit","department":"SALES","salary":45000}
]
result=[data["name"] for data in employees if data["department"]=="IT" and  data["salary"]>60000]
print(result)
