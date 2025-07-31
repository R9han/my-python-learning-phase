promt = "\nTell me something, I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program."

active = True 
while active:
    message = input(promt)

    if message.upper() == "quit": 
        active = False 
    else:
        print(f"\n____ {message}____")