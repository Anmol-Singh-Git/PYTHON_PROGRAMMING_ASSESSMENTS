unit=float(input("enter your unit :"))

if( unit<=100):
    print("charges of 5 per unit")
    bill=unit*5
elif( unit<=200) :
    print("charges of 7 per unit") 
    bill=unit*7
elif( unit<=300):
    print("charges of 10 unit") 
    bill=unit*10
else:
    print("charges of 15 per unit")
    bill=unit*15
    
if bill>3000:
    print("include supercharges bill is above 3000")
    super_charges= bill * 10/100
    bill=bill+super_charges
else:
    print("no supercharges- bill is below to 3000:",unit)
    
    
print("the electricity bill is :",bill)
