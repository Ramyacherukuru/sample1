Tank_capacity = 900
current_level = int(input("Enter the current level of ethanol in the tank:"))
if current_level > 0.8 * Tank_capacity:
    print("Raise an alarm to close the valve")
elif current_level < 0.2 * Tank_capacity:
    print("Send an sms to buy more liquid")
else:
    print("It is safe:")
