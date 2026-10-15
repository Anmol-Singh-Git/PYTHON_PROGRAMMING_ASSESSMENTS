# count even and odd number from 1 to 50
i=1
count_even=0
count_odd=0
while(i<=50):
   if(i%2==0):
      count_even+=1
   else:
      count_odd+=1
   i+=1  
print("Even number:",count_even)     
print("odd number:",count_odd)
