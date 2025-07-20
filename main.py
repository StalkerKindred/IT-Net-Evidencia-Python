from console import *
from person import *

top_console_graphics()

#For testing purposes allready created duško
duško = Person("Dušan","Stránsky","69","915631081")
insured_people = [duško]

running = True

#Main loop
while running:
    selected_action = 0
    action = select_action()
    print("")

    """
    Match action:
    It will ask in console for an input of INT type numbers between and including 1 to 4
    1 - Will call function create_person() that creates a new person and adds them to a list of all insured persons
    2 - Will print every single persons first name, last name, age, phone number
    3 - Will call function find_person() that prints person if it finds the matching first name and last name input
    4 - Will end the program
    """

    match action:
        #Creates a person
        case 1:
            selected_action = 1
            insured_people.append(create_person())
        #Prints all insured people
        case 2:
            print("First name  Last name  Age  Phone")
            for person in insured_people:
                print(person)
        #Finds all matching insured people with user inputed first and last name
        case 3:
            find_person(insured_people)
        #Ends the program
        case 4:
            print("Ending the program")
            running = False

    print("")

    #Print an end message based on selected action and pauses the program until the person presses anything on keyboard
    if selected_action == 1:
        print("Person was saved. Continue with pressing any key.")
        input("")
    else:
        print("Continue with pressing any key.")
        input("")
