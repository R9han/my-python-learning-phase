responses = {}

polling_active = True 

while polling_active: 
    name = input("\nWhat is your name?: ")
    response = input("Which mountain would you like to climb someday?: ")
    responses[name] = response 
    
    repeat = input("Would you like to let another person respond(y/n)?: ")
    if repeat.lower() == "n": 
        polling_active = False 

print("_____POLL RESULT_____")
print()
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")