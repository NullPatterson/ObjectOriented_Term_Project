# Author: Nol Patterson
# Date: 11/20/2023
# Purpose: Define the Event class used in driver.py for the CSC2310-001 Term Project
class Event:
    def __init__(self, event_name, event_id, date, start_time, location, duration):
        self.__name = event_name
        self.__event_id = event_id
        self.__date = date  # YYYY-MM-DD
        self.__start_time = start_time  # Military time 00:00
        self.__location = location
        self.__duration = duration  # In hours
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

    def action_items(self):
        print("Action items:")
        for item in self.__action_items:
            print(" -{}".format(item))

    def append_action_items(self, items):
        for item in items:
            self.__action_items.append(item)