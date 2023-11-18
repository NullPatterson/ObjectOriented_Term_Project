# Author: Nol Patterson
# Date: 11/20/2023
# Purpose: Define the Contact class used in driver.py for the CSC2310-001 Term Project
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
        self.__last_communication = None # YYYY-MM-DD

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

    @property
    def last_communication(self):
        return self.__last_communication

    @last_communication.setter
    def last_communication(self, last_communication):
        self.__last_communication = last_communication

    # Method to output all relevant information about the contact
    def contact_info(self):
        # \t used to align output arguments
        print("First Name:\t\t\t", self.__first_name)
        print("Last Name:\t\t\t", self.__last_name)
        print("User ID:\t\t\t", self.__user_id)
        print("Email Address:\t\t", self.__email_address)
        print("Department:\t\t\t", self.__department)
        print("Job Title:\t\t\t", self.__job_title)
        print("Phone Number:\t\t", self.__phone_number)
        print("Building:\t\t\t", self.__building)
        print("Post Office Box:\t", self.__post_box)
        if self.__last_communication != None:
            print("Last Communication:\t", self.__last_communication)