# age.py

from datetime import datetime


def birthday_input():
    """
    Asks the user to input their birthday and returns it as a datetime object.

    Input in the format 'DD-MM-YYYY'.
    If the input is not formatted correctly an error message is printed and they are asked again.
    """
    date = input("Please input your birthday in the format 'DD-MM-YYYY': ")
    try:
        date = datetime.strptime(date, "%d-%m-%Y")
    except:
        if date:  # strings are evaluated True if non-empty or False if empty
            print(f"'{date}' is not a valid input")
        else:
            print("You have not entered anything")
        return birthday_input()
    else:
        return date


def birthdate_to_age(birthdate):
    """
    Takes a datetime format parameter and returns the age of someone with that birthdate.
    """
    now = datetime.now()  # creates a datetime object called now with the current date and time
    age = now.year-birthdate.year
    if now.month < birthdate.month or now.month == birthdate.month and now.day < birthdate.day:
        age -= 1
    return age


def main():
    date = birthday_input()
    print(birthdate_to_age(date))


main()
