English = float(input("Enter the English marks:"))
Science = float(input("Enter the Science marks:"))
Mathematics = float(input("Enter the Mathematics marks:"))

English = (English / 80) * 100
Science = (Science / 90) * 100
Mathematics = (Mathematics / 100) * 100

if English >= 90 and Science >= 90 and Mathematics >= 90:
    print("First class")
elif English >= 75 and Science >= 75 and Mathematics >= 75:
    print("Second class")
elif English <= 35 and Science <= 35 and Mathematics <= 35:
    print("Fail")
else:
    print("Average")

                      
                      
