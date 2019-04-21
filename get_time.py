#   Victor Chimenti
#   get_time.py
#   A program to unit test a valid date format


import datetime


def getdate(date_in):
    try:
        datetime.datetime.strptime(date_in, '%Y-%m-%d')
    except ValueError:
        # print('Invalid Date Format, enter format YYYYY-MM-DD')  // user input commented out
        return False
    return True


date_today = datetime.datetime.now()
print(str(date_today))

# // user input commented out
# date_input = input("Enter any month and day in the format YYYY-MM-DD to verify if it is a correct date format: ")
# print(str(getdate(date_input)) + '\n')
