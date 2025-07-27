weight = float(input("Enter your weight: "))
unit = input("Enter the Unit(k or L): ")

if  unit == "k":
    result = weight * 0.4535920  
    print(f"Your weight is {round(result, 2)}Lbs")  # I use the capital 'L' because small L is similar to the number 1.... l1 
elif unit == "L": 
    result = weight * 2.20462  
    print(f"Your weight is {round(result, 2)}Kg")
else:
    print(f"{unit} is not a valid unit :( ")