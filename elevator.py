import time

# Creating a dictionary of the floors to allow easy floor lookup
floor_panel = {
    "L": "Lobby",
    "2": "Second Floor",
    "3": "Third Floor",
    "4": "Fourth Floor",
    "5": "Fifth Floor"
}
user_floor = 1

# Flags declared for menu selections
user_leaving = False
user_inside = False

# Prints the menu when user is inside of the elevator
def print_internal_menu():

    for floor in floor_panel:
        print(f"Enter '{floor}' for the {floor_panel[floor]} floor.")
    print("Enter 'E' to exit the elevator.")

# Prints the menu when user is outside of the elevator
def print_external_menu():
    if(user_floor < 5):
        print("Enter 'U' to call an elevator going up.")

    if(user_floor > 1):
        print("Enter 'D' to call an elevator going down.")
    else:
        print("Enter 'E' to exit the building.")

# Simple message for user selection
def user_select():
    selection = input("Selection: ")
    return selection

# Has user wait for the elevator
def call_elevator():
    print("Please wait for elevator", end='')
    for i in range(4):
        time.sleep(0.5)
        print(".", end='')
    print()

# Moves the user down floors
def move_user_down(select):
    global user_floor
    if (select == 'L'):
        select = 1
    else:
        select = int(select)
    
    while(user_floor > select):
        user_floor -= 1
        if(user_floor != 1):
            print("↓ " + floor_panel[f"{user_floor}"])
        else:
            print("↓ " + floor_panel["L"])
        time.sleep(1)

# Moves the user up floors
def move_user_up(select):
    global user_floor
    select = int(select)
    
    while(user_floor < select):
        user_floor += 1
        print("↑ " + floor_panel[f"{user_floor}"])
        time.sleep(1)

# Introduction message
print("-------------------------------------------------------------")
print("Welcome to Monty Inc.!")

# While loop while user hasn't left building
while(not user_leaving):
    print("Would you like to call an elevator?")
    print("-------------------------------------------------------------")

    # User makes selection from outside of elevator
    print_external_menu()
    print("-------------------------------------------------------------")
    match(user_select().capitalize()):
        # User calls elevator going up
        case 'U':
            if (user_floor < 5):
                print("Going up!")
                call_elevator()
                user_inside = True
            else:
                print("Invalid Selection! At top floor!")
                time.sleep(3)

        # User calls elevator going down
        case 'D':
            if (user_floor > 1):
                print("Going down!")
                call_elevator()
                user_inside = True
            else:
                print("Invalid Selection! At bottom floor!")
                time.sleep(3)

        # User exits building
        case 'E':
            if (user_floor == 1):
                print("GOODBYE!")
                user_leaving = True
            else:
                print("Invalid Selection! Not in Lobby!")
                time.sleep(3)
        
        # User makes an invalid selection
        case _:
            print("Invalid Selection!")
            time.sleep(3)

    while(not user_leaving and user_inside):

        # User makes selection inside of elevator
        print("-------------------------------------------------------------")
        print_internal_menu()
        print("-------------------------------------------------------------")
        
        # Decide action based on user input
        floor_select = user_select()
        match(floor_select.capitalize()):

            # User picked a floor button
            case 'L' | '2' | '3' | '4' | '5':
                print(f"Going to {floor_panel[floor_select]}!")
                if((floor_select == 'L' or int(floor_select) < user_floor)
                    and user_floor != 1):
                        move_user_down(floor_select)
                elif(floor_select != 'L' and int(floor_select) > user_floor):
                        move_user_up(floor_select)
                else:
                    print("You are already on this floor!")
                    time.sleep(3)
                
                # Prints where the user is (possibly after moving)
                if (user_floor == 1):
                    floor_name = floor_panel["L"]
                else:
                    floor_name = floor_panel[f"{user_floor}"]
                print(f"You are now at the {floor_name}!")

            # User makes selection to get off elevator
            case 'E':
                print("Getting off Elevator!")
                user_inside = False

            # User makes an invalid selection
            case _:
                print("Invalid Selection!")
                time.sleep(3)

        # End match(floor_select)
    # End while(not user_leaving and user_inside)
# End while(not user_leaving)
