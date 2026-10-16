salary=float(input("Enetr your salary:"))
experience=int(input("Enter year of experience:"))
performance=int(input("Enter your performance:"))
if(salary>=50000):
    if(experience>=1):
        if(performance>=90):
            print("salary bonus is 20%")
            bonus=salary*20/100
            print("bonus",bonus)  
        elif(performance>=75):
            print("salary bonus is 10%") 
            bonus=salary*10/100

            print("bonus",bonus)  

        else:
            print("salary bonus is 5%") 
            bonus=salary*5/100
            print("bonus",bonus)  

    else: 
        if(performance>=90 ):
            bonus=salary*15/100
            print("bonus",bonus)  

        else:
            bonus=salary*5/100 
            print("bonus",bonus)          
else:
    print("no bonus")    
           
  
               
