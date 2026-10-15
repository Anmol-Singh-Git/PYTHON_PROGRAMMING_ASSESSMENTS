products={
    "laptop":10,
    "mouse":3,
    "keyboard":0,
    "monitor":7,
    "Printer":2
}
for pro_name,stock in products.items():
    if (stock>0):
        if(stock<=5):
            print(pro_name,"- low stocks")
        elif(stock>5):
            print(pro_name,"- stock is available")  
    else:
        print(pro_name,"- out of stock")          
