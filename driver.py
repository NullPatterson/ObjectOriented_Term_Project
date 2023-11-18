# Author: Nol Patterson
# Date: 11/20/2023
# File Name: driver.py
# Purpose: Driver file for CSC 2310-001 Term Project at Tennessee Tech

# Libraries
import json
from contact import Contact

class Event:
    def __init__(self, event_name, event_id, date, start_time, location, duration):
        self.__name = event_name
        self.__event_id = event_id
        self.__date = date             # YYYY-MM-DD
        self.__start_time = start_time  # Military time 00:00
        self.__location = location
        self.__duration = duration     # In hours
        self.__action_items = []

    # Getters and Setters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def event_id(self):
        return self.__event_id

    @event_id.setter
    def event_id(self, event_id):
        self.__event_id = event_id

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    

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

# Debug Statement to see if all contact info is able to be outputted
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

