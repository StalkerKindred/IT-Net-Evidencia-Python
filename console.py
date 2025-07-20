from person import Person

#Longer descriptions of functions are found at their end

def top_console_graphics():
    print("""----------------------------------------------------
Evidence of recorded insured persons
----------------------------------------------------""")

def select_action():

    print("""Select your action:
    1 - Add new insured person
    2 - List all insured persons
    3 - Search for insured person
    4 - End""")

    getting_user_input = True
    #Gets input
    while getting_user_input:
        try:
            user_input = int(input("Action: "))

            if user_input > 4 or user_input < 0:
                print("You need to enter 1 number (1-4)")
                continue 
            else:
                getting_user_input = False

        except Exception:
            print("You need to enter 1 number (1-4)")

    return user_input

    """
    Select action:
    Firstly it prints for the user what actions they can do
    It will ask in console for an input of INT type numbers between and including 1 to 4
    Then it checks if its INT and its between 1 and 4
    After that it returns it for console logic to use
    """

def find_person(insured_list):

    print("Enter First name: ")
    first_name = input_and_checker().lower()

    print("Enter Last name: ")
    last_name = input_and_checker().lower()

    print("")

    #List for persons found with the same fist and last name
    insured_found = []

    print("First name  Last name  Age  Phone")
    #Finds the persons using user input that is stripped of blank spaces and lowered for easier searching.
    for person in insured_list:
        if person.first_name.strip().lower() == first_name and person.last_name.strip().lower() == last_name:
            insured_found.append(person)
            print(person)

    if len(insured_found) == 0:
        print("This person does not yet exist.")

    """
    Find Person
    It requires a list 
    It will call for input_and_checker() function to get the first and last name from user.
    In for loop that looks at every person in it,
        it uses .lower on first and last names from input and the person that the loop is currently looking at
        making all letters lower case for easier matching
        if it finds a person it prints them
    If it found no person, it prints to console a message
    """

def input_and_checker(type = "none", number_type = ""):
    #Checking for INT/numbers type 
    if type == "number":
        print("numbering")
        checking_number = True

        while checking_number:

            try:
                user_input = input().strip()

                #At least 1 number
                if len(user_input) == 0:
                    print("You need to enter at least 1 number.")
                    continue
               
                #Checks for realistic age number
                if number_type == "age" and (int(user_input) > 122 or int(user_input) < 0):
                    print("You need to enter a realistic age.")
                    continue

                #Minimum and Maximum characters for phone number
                if number_type == "phone" and (len(user_input) > 10 or len(user_input) < 9):
                    print("You need to enter numbers between 9-10 (0-9)")
                    continue

                return user_input
                
            #Catching errors
            except Exception:
                print("Please enter only numbers(0-9)")
                continue
    
    #Checking for letters/words
    else:

        checking_letters = True

        while checking_letters:

            user_input = input().strip()
            #min characters

            if len(user_input) == 0:
                print("You need to enter at least 1 letter.")
                continue

            #Catching not letters
            if not user_input.isalpha():
                print("You need to only enter letters.")
                continue

            #Modifying input
            return user_input.lower().capitalize()
        
    """
    Input And Checker
    It asks user for an input that based on requierments will be checked
    It has 2 optional requierments type and number_type
        - type number will check for INT types.
            otherwise it checks for letters only.
        - number_type is for class person to check for valid age and phone number.

    Optional Requiermets:
    Type number
        Will check for at least 1 INT (number), it removes all blank spaces in front and behind the number
        then returns it

    Type number and Number type phone
        Similiar to Type number but it checks for INT number long between 9-10 characters
        then returns it

    Type number and Number type age
        Similiar to Type number, but it checks for a realistic age between and including 0 - 122(The maximum recored age in human known history)
        then returns it

    No Option requierments
        Will check for letters only input,it has to be at least 1 character long,
        it will remove all blank spaces in front and behind the word/s
        then lower the word/words and makes the first letter higher case.
    """

def create_person():
    #Input - First name, Last name, Age, Phone Number
    print("Enter First name: ")
    first_name = input_and_checker()
    print("Enter Last name: ")
    last_name = input_and_checker()
    print("Enter Age: ")
    age = input_and_checker(type = "number", number_type = "age")
    print("Enter Phone Number: ")
    phone_number = input_and_checker(type = "number", number_type = "phone")

    #Creating person
    person = Person(first_name, last_name, age, phone_number)
    return person

    """
    Create Person
    It will call for input_and_checker() function to get the first and last name, age and phone number from the user.
    Then it creates the person and returns it
    """