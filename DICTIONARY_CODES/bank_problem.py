account={
    "Rahul":25000,
    "Amit":5000,
    "Priya":0,
    "Neha":-2000
}
for name,balance in account.items():
    if(balance>=10000):
        print(name,"- premium account")
    elif(balance<0):
        print(name,"- over draft")
    elif(balance==0):
        print(name,"- No balance")
    else:
        print(name,"- Regular aacount")
