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

# First time welcome statement
print("Welcome what would you like to do today!")
while running:
    # Main menu
    print("1) View your list of contacts")
    print("2) View your list of events")
    print("3) Update the last date of communication for a contact")
    print("4) Add action items to a given event")

