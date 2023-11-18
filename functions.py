# Author: Nol Patterson
# Date: 11/20/2023
# Purpose: Define functions used in driver.py for the CSC2310-001 Term Project

# Function Name: menu_validation()
# Purpose: Check a user input against a range of acceptable values
# Parameters: choice, the menu choice made by the user; will be in the format of "x" where x is an integer
#             minval, the minimum integer choice could be
#             maxval, the maximum integer choice could be
# Returns: int(choice); after it is validated that  minval <= int(choice) <= maxval
def menu_validation(choice, minval, maxval):
    if not choice.isdigit():
        print("{0} is not a valid choice please enter an integer between {1} and {2}:".format(choice, minval, maxval), end=" ")
        choice = input()
        menu_validation(choice, minval, maxval)
    elif (int(choice) < minval) or (int(choice) > maxval):
        print("{0} is not a valid choice please enter a value between {1} and {2}:".format(choice, minval, maxval), end=" ")
        choice = input()
        menu_validation(choice, minval, maxval)
    return int(choice)

def print_all_contacts(*contacts):
    print("UserID\tLast, First Name")
    for contact in contacts:
        print("{0}\t{1}, {2}".format(contact.user_id, contact.last_name, contact.first_name))
    print()
