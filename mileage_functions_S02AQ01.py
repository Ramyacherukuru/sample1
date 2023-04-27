def cal_mileage(Starting_value,Ending_value,Fuel_consumed):
    
    distance_travelled = Ending_value - Starting_value
    car_mileage = distance_travelled/Fuel_consumed
    return car_mileage
Starting_value = float(input("Enter the starting value:"))
Ending_value = float(input("Enter the Ending value:"))
Fuel_consumed = float(input("Enter the value of Fuel_consumed:"))
car_mileage = cal_mileage(Starting_value, Ending_value, Fuel_consumed)
print("car_mileage:", car_mileage,"per gallon")

