data=[22,55,12,89,34,67] 
i=1
largest=data[0]
while i<len(data):
    if data[i]>largest:
        largest=data[i]
    i+=1
print("largest num in a list:",largest)   
