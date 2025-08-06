# Q. A movie theater charges different ticket prices depending on
#    person's age. If a person is under the age of 3, the ticket is free; 
#    if they are between 3 and 12, the ticket is $10; if they are over 
#    age 12, the ticket is $15. Write a loop(while loop) in which you ask 
#    their age, and then tell them the cost of their movie ticket. 


# i know you can solve this problem more easily than me :)  

while True:
    age_input = input("Please enter your age (or type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        break

    try:
        age = int(age_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if age < 0:
        print("Age cannot be a negative number.")
    elif age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")


 

    