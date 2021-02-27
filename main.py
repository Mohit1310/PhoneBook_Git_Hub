def welcome():
    choice = int(input('''Welcome to Phonebook App.Select Your option ==>
                1.Create new contact
                2.Display your existing contact
                3.View the contacts by name
                4.Delete a contact
                5.Exit
                '''))
    return choice


def phonebook():
    # Created an empty dictionary
    contact = {}

    # To run phonebook app continuosly
    while True:
        option = welcome()
        if option == 1:
            contact_name = input("Enter contact name in this format 'First name  Last name': ")
            contact_number = int(input("Enter your number"))

        if option == 2:
            pass
        if option == 3:
            pass
        if option == 4:
            pass
        if option == 5:
            pass

if __main__ =='__name__'
