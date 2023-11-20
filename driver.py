# Author: Nol Patterson
# Date: 11/20/2023
# File Name: driver.py
# Purpose: Driver file for CSC 2310-001 Term Project at Tennessee Tech

# Libraries
import json
from contact import Contact
from event import Event
import functions
import os
import platform

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


# FUNCTIONS
    


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
    print("3) Exit program")
    menu_choice = input("Please enter a value from 1 to 3: ")
    print()

    # Validating menu_choice
    menu_choice = functions.menu_validation(menu_choice, 1, 3)

    # Following the chosen action
    match menu_choice:
        case 1:
            # Outputting the list of contacts with their UserIDs and Names
            print("UserID\tLast, First Name")
            for contact in listContacts:
                print("{0}\t{1}, {2}".format(contact.user_id, contact.last_name, contact.first_name))
            print()

            # Outputting choices to do with the contact list
            print("Which of the following would you like to do?")
            print("1) View all information about a contact")
            print("2) Update last date of communication with a contact")
            print("3) Return to main menu")
            menu_choice = input("Please enter a value from 1 to 3: ")
            print()

            # Validating menu_choice
            menu_choice = functions.menu_validation(menu_choice, 1, 3)

            match menu_choice:
                case 1:
                    print("UserID\tLast, First Name")
                    for contact in listContacts:
                        print("{0}\t{1}, {2}".format(contact.user_id, contact.last_name, contact.first_name))
                    print()
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
                    print("UserID\tLast, First Name")
                    for contact in listContacts:
                        print("{0}\t{1}, {2}".format(contact.user_id, contact.last_name, contact.first_name))
                    print()
                    menu_choice = input("Please enter the UserID of the contact whose "
                                        "information you would like to see: ")
                    print()

                    # Validating menu_choice
                    menu_choice = functions.menu_validation(menu_choice, 0,
                                                            int(listContacts[len(listContacts) - 1].user_id))

                    old_date = listContacts[menu_choice].last_communication
                    new_date = input("Using the format \'YYYY-MM-DD\' Please enter the date of last "
                                     "communication with {0} {1}: ".format(listContacts[menu_choice].first_name,
                                                                           listContacts[menu_choice].last_name))
                    listContacts[menu_choice].last_communication(new_date)
                    print("The date of last communication with {0} {1} has been updated from {2} to {3}.".format(
                        listContacts[menu_choice].first_name, listContacts[menu_choice].last_name,
                        old_date, new_date))
                    wait_to_continue = input("Press enter to continue: ")
                    print()

                case 3:
                    continue

                case _:
                    print("Error in nested menu_choice from case 1 of primary menu_choice in primary while loop")

        case 2:
            # Outputting a list of events and event id:
            print("EventID\tEvent Name")
            for event in listEvents:
                print("{0}\t{1}".format(event.event_id, event.name))
            print()

            print("Which of the following would you like to do?")
            print("1) View all information about an event")
            print("2) Add action items to an event")
            print("3) Return to main menu")
            menu_choice = input("Please enter a value from 1 to 3: ")

            # Validating menu_choice
            menu_choice = functions.menu_validation(menu_choice, 1, 3)
            print()

            match menu_choice:
                case 1:
                    print("EventID\tEvent Name")
                    for event in listEvents:
                        print("{0}\t{1}".format(event.event_id, event.name))
                    print()

                    menu_choice = input("Please enter the EventID of the event "
                                        "whose information you would like to see: ")

                    menu_choice = functions.menu_validation(menu_choice, 0,
                                                            listEvents[len(listEvents)-1].event_id)
                    print()
                    print("EVENT INFO")
                    print("---------------")
                    listEvents[menu_choice].event_info()
                    wait_to_continue = input("Press enter to continue")
                    print()

                case 2:
                    print("EventID\t\tEvent Name")
                    for event in listEvents:
                        print("{0}\t\t\t{1}".format(event.event_id, event.name))
                    print()

                    menu_choice = input("Please enter the EventID of the event you "
                                        "would like to add action items to: ")
                    menu_choice = functions.menu_validation(menu_choice, 0,
                                                            listEvents[len(listEvents) - 1].event_id)
                    adding_items = True
                    while adding_items:
                        eventIndex = menu_choice
                        action_items = input("Please enter action items you would like to add to "
                                             "\"{0}\" as a comma seperated list: ".format(listEvents[menu_choice].name))

                        split_list = action_items.split(', ')
                        print()
                        print("The action items you would like to add are:")
                        for item in split_list:
                            print(" -", item)
                        menu_choice = input("If these items are correct enter 1 otherwise enter 0: ")

                        menu_choice = functions.menu_validation(menu_choice, 0, 1)
                        print()

                        if menu_choice == 1:
                            adding_items = False
                            listEvents[eventIndex].append_action_items(split_list)
                            print("The action items were successfully added to \"{0}\""
                                  .format(listEvents[eventIndex].name))
                            print()

                case 3:
                    continue

                case _:
                    print("Error in primary case 2 in primary while loop")

        case 3:
            running = False

        case _:
            print("Error in match menu_choice in primary while loop")

    # Clearing the console
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.systems('clear')



print()
print("Goodbye!")
