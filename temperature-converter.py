temp = float(input("Enter the temperature: "))
unit = input("Enter the Unit of that temperature(C or F): ").upper()

if unit == "C":
    result = (temp * 9)/5 + 32 
    print(f"The temperature in Farenheit is:{round(result, 2)}F ")
elif unit == "F": 
    result = (temp - 32)*5 / 9 
    print(f"The temperature in Celcius is:{round(result, 2)}C ")

else:
    print(f"{unit} is not a valid Unit. Try again! ")