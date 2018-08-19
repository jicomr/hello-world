prompt = "\nYou can enter 'quit' at any time to end this program. "
prompt += "\nPlease enter a positive integer between 1 and 99: "
active = True
upper_bound = 99
#print("\nBeginning while loop")
while active:
    ui_input = input(prompt)
    if ui_input == 'quit':
        active = False
    elif int(ui_input) > 99: #evaluate if too big
        print("too big")
    elif int(ui_input) < 1:  #evaluate if too smaall
        print("too small")
    elif int(ui_input) % 2 == 0:  #evaluate as even or odd
        #number is even
        print("number is even")
        if int(ui_input) > 20:  #evaluate if greater than twenty
            print("greater than 20")
        else:  #less than or = to 20
            if int(ui_input) >= 6:  #evaluate is greater than or equal to 6
                print("Weird")
            else:
                print("Not Weird")
    else:
        #number is odd 
        print("number is odd")
