data="shivansh vashishth"
i=0
count=0
while i<len(data):
    if data[i] in "aeiou":
        count+=1
    i+=1
print("vowel:",count)
