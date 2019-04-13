#   Victor Chimenti
#   CPSC 5210 Testing and Debugging
#   19SQ Seattle University
#   get_time.py
#   A program to unit test a valid date format


import datetime


def getdate(date_in):
    try:
        datetime.datetime.strptime(date_in, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Invalid Date Format, enter format YYYYY-MM-DD')
    return True


date_input = input("Enter any date: ")
date_today = datetime.datetime.now()
print(str(date_today))
print(str(getdate(date_input)))
