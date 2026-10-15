data={
    "a":10,
    "b":15,
    "c":25,
    "d":30,
    "e":40
}
for alphabet,number in data.items():
    if(number%2==0):
        if(number>=20):
            print(alphabet,"even large")
        else:
            print (alphabet,"even")  
    else:
        print(alphabet,"odd")
