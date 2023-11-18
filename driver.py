# Author: Nol Patterson
# Date: 11/20/2023
# File Name: driver.py
# Purpose: Driver file for CSC 2310-001 Term Project at Tennessee Tech

# Libraries
import json


class Contact:
    def __init__(self, firstname, lastname, userid, email, department, jobtitle, phonenumber, building, postbox):
        self.__first_name = firstname
        self.__last_name = lastname
        self.__userID = userid
        self.__email_address = email
        self.__department = department
        self.__job_title = jobtitle
        self.__phone_number = phonenumber
        self.__building = building
        self.__post_box = postbox

    @property
    def first_name(self):
        return self.__first_name

    @property
    def user_id(self):
        return self.__userID


class Event:
    def __init__(self, eventname, eventid, date, starttime, location, duration):
        self.__name = eventname
        self.__id = eventid
        self.__date = date
        self.__start_time = starttime
        self.__location = location
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

    # Debug Statement to check if Contacts were read in properly
    # print("{0}: {1}".format(newContact.user_id, newContact.first_name))

    