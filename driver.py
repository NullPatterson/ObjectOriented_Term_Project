# Author: Nol Patterson
# Date: 11/20/2023
# File Name: driver.py
# Purpose: Driver file for CSC 2310-001 Term Project at Tennessee Tech

# Libraries
import json
from contact import Contact
from event import Event
import functions

# Iterators for the different list
contactListIterator = 0
eventListIterator = 0

# Reading data from contacts.json
with open("contacts.json") as contact_file:
    contact_data = json.load(contact_file)
# Creating a list of contacts
listContacts = []
for contact in contact_data:
    newContact = Contact(contact['FirstName'], contact['LastName'], contact['UID'], contact['EmailAddress'],
                         contact['Dept'], contact['Title'], contact['Phone'], contact['Building'], contact['POBox'])
    listContacts.append(newContact)
    # Debug Statements to check if Events were read in properly
    # print("{0}: {1}".format(listContacts[contactListIterator].user_id, listContacts[contactListIterator].first_name))
    # contactListIterator = contactListIterator + 1
# contactListIterator = 0  # Used to reset eventListIterator if used for debugging
contact_file.close()

# Debug Statement to see if all contact info is able to be output
# listContacts[0].contact_info()

# Reading data from events.json
with open("events.json") as event_file:
    event_data = json.load(event_file)
# Creating a list of events
listEvents = []
for event in event_data['university_events']:
    newEvent = Event(event['Name'], event['UID'], event['Date'],
                     event['StartTime'], event['Location'], event['Duration'])
    listEvents.append(newEvent)
    # Debug Statements to check if Events were read in properly
    # print("{0}: {1}".format(listEvents[eventListIterator].name, listEvents[eventListIterator].location))
    # eventListIterator = eventListIterator + 1
# eventListIterator = 0  # Used to reset eventListIterator if used for debugging
event_file.close()

# Debug statement to check event_info()
# listEvents[0].event_info()

# Bool value to keep user interface open and that the application is running
running = True
# Value to track user menu choice.
menu_choice = "0"
# Used to pause the program until enter is pressed
wait_to_continue = ""

# First time welcome statement
print("Welcome what would you like to do today!")
while running:
    # Main menu
    print("Main Menu:")
    print("1) View your list of contacts")
    print("2) View your list of events")
    print("3) Update the last date of communication for a contact")
    print("4) Add action items to a given event")
    print("5) Exit program")
    menu_choice = input("Please enter a value from 1 to 5: ")
    print()

    # Validating menu_choice
    menu_choice = functions.menu_validation(menu_choice, 1, 5)

    # Following the chosen action
    match menu_choice:
        case 1:
            # Outputting the list of contacts with their UserIDs and Names
            functions.print_all_contacts(listContacts)

            # Outputting choices to do with the contact list
            print("Which of the following would you like to do?")
            print("1) View all information about a contact")
            print("2) Correct a contact's information")
            print("3) Update last date of communication with a contact")
            print("4) Return to main menu")
            menu_choice = input("Please enter a value from 1 to 4: ")
            print()

            # Validating menu_choice
            menu_choice = functions.menu_validation(menu_choice, 1, 4)

            match menu_choice:
                case 1:
                    functions.print_all_contacts(listContacts)
                    menu_choice = input("Please enter the UserID of the contact whose "
                                        "information you would like to see: ")
                    print()

                    # Validating menu_choice
                    menu_choice = functions.menu_validation(menu_choice, 0,
                                                            int(listContacts[len(listContacts)-1].user_id))

                    print("CONTACT INFO")
                    print("---------------------")
                    listContacts[menu_choice].contact_info()
                    wait_to_continue = input("Press enter to continue: ")
                    print()

                case 2:
                    menu_choice = input("Please enter the UserID of the contact whose "
                                "information you would like to correct: ")
                    print()

                    # Validating menu_choice
                    menu_choice = functions.menu_validation(menu_choice, 0,
                                                            int(listContacts[len(listContacts) - 1].user_id))

                case _:
                    print("Error in nested menu_choice from case 1 of primary menu_choice in primary while loop")

        case _:
            print("Error in match menu_choice in primary while loop")
