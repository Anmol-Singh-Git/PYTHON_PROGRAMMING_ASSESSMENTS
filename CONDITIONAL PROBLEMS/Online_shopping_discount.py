amount=int(input("enter cart amount"))
premium=input("customer is a premium member/ yes?no")
if(amount>=5000):
        
    if(premium=="yes"):
        discount=20
        if(amount<0):
            print("amount is invalid:")
        else:
            print("amount is 0")
    else:
         discount=10   

else:
    if(premium=="yes"):
        discount=5

    else:
       discount=0

discount_amount =amount * discount/100   
final_amount=amount-discount_amount
print("discount",discount,"%")  
print("final amount=",final_amount)   
