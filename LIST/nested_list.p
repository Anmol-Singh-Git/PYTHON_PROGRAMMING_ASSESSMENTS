sales=[
    ["aman",12000,15000,18000],
    ["kunal",22000,17000,14000],
    ["rahul",16000,22000,19000]
]
highest_sale=0
top_salesperson=""
for person in sales:
    name=person[0]
    total=sum(person[1:])
    print("name:",name)
    print("total sale:",total)
    
    if total>highest_sale:
        higest_sale=total
        top_salesperson=name
        
print("top_salesperson",top_salesperson)  
print("higest_sale:",highest_sale)      
