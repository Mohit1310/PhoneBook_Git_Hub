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
            contact_number = int(input("Enter your number: "))

            if contact_number in contact.values():
                print("Contact already exists!!!")
            else:
                contact[contact_name]=contact_number

        if option == 2:
            if bool(contact) != False:
                for k,v in contact.items():
                    print("{} ==> {}".format(k,v))
            else:
                print("No Contacts exist !!! Your PhoneBook is empty.")

        if option == 3:
            name = input("Enter the name of contact details: ")
            if name in contact:
                print("{} ==> {}".format(name,contact[name]))
            else:
                print("No contacts exist with {}  name.".format(name))

        if option == 4:
            name = input("Enter the name of Contact Details that you wish to delete: ")
            if name in contact:
                contact.pop(name)
            else:
                print("No contact exist with name {} ".format(name))

        if option == 5:
            print("Thanks for using out Phonebook App")
            break

if __name__ =='__main__':
    phonebook()
