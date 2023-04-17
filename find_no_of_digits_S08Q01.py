num = int(input("Enter a numer: "))
count = 0
while num > 0:
    count +=1
    num = num // 10;
    
print("Number of Digits: " ,count)
