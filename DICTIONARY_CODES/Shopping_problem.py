products={
    "Mobile":15000,
    "Mouse":500,
    "Laptop":60000,
    "Keyboard":1200
}
for pro_name,price in products.items():
    if(price>=1000):
        if(price>=5000):
            print(pro_name,"premium product")
        else:
            print(pro_name,"expensive product") 
    else:
        print(pro_name,"Affordable price")         
