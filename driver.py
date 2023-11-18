# Author: Nol Patterson
# Date: 11/20/2023
# File Name: driver.py
# Purpose: Driver file for CSC 2310-001 Term Project at Tennessee Tech

# Libraries
import json


class Contact:
    def __init__(self, first_name, last_name, user_id, email, department, job_title, phone_number, building, post_box):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_id = user_id
        self.__email_address = email
        self.__department = department
        self.__job_title = job_title
        self.__phone_number = phone_number
        self.__building = building
        self.__post_box = post_box
        self.__last_communication = "0000-00-00"  # YYYY-MM-DD

    # Getters and Setters in case information needs to be updated
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def email(self):
        return self.__email_address

    @email.setter
    def email(self, email):
        self.__email_address = email

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, department):
        self.__department = department

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, job_title):
        self.__job_title = job_title

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def building(self):
        return self.__building

    @building.setter
    def building(self, building):
        self.__building = building

    @property
    def post_box(self):
        return self.__post_box

    @post_box.setter
    def post_box(self, post_box):
        self.__post_box = post_box


class Event:
    def __init__(self, eventname, eventid, date, starttime, location, duration):
        self.__name = eventname
        self.__id = eventid
        self.__date = date             # YYYY-MM-DD
        self.__start_time = starttime  # Military time
        self.__location = location
        self.__duration = duration     # In hours
        self.__action_items = []

    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location


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

    # Debug Statement to check if Contacts were read in properly
    # print("{0}: {1}".format(newContact.user_id, newContact.first_name))

    listContacts.append(newContact)
    # Debug Statements to check if Events were read in properly
    # print("{0}: {1}".format(listContacts[contactListIterator].user_id, listContacts[contactListIterator].first_name))
    # contactListIterator = contactListIterator + 1
# contactListIterator = 0  # Used to reset eventListIterator if used for debugging

contact_file.close()

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

