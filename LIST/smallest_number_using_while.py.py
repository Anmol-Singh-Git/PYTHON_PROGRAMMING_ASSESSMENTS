# data=[22,55,12,89,34,67] 
# smallest=data[0]
# for num in data:
#     if num<data[0]:
#         smallest=num
# print("smallest num in a list:",smallest)

# using while loop
data=[22,55,12,89,34,67]
i=1
smallest=data[i]
while i<len(data):
    if(smallest>data[i]):
        smallest=data[i]
    i+=1
print("smallest num in a list:",smallest)       
