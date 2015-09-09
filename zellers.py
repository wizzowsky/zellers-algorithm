# Zeller's algorithm is used to calculate the day of the week a specific date falls on.
# The purpose of this program is to compute Zeller's algorithm and spit out a day of the week.

NAMES_OF_MONTHS = {'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                   'november', 'december'}


# check to see if the input was a value of the actual months of the year
def check_input(x):
    return x in NAMES_OF_MONTHS


# This function takes the result of Zeller's algorithm and returns the weekday
def define_weekday(x):
    if x == 0:
        return 'Sunday'
    elif x == 1:
        return 'Monday'
    elif x == 2:
        return 'Tuesday'
    elif x == 3:
        return 'Wednesday'
    elif x == 4:
        return 'Thursday'
    elif x == 5:
        return 'Friday'
    elif x == 6:
        return 'Saturday'
    else:
        return 'Broken?'


# This converts the string inputted by the user into an int
def convert_month_to_int(x):
    if x == 'january':
        return 11
    elif x == 'february':
        return 12
    elif x == 'march':
        return 1
    elif x == 'april':
        return 2
    elif x == 'may':
        return 3
    elif x == 'june':
        return 4
    elif x == 'july':
        return 5
    elif x == 'august':
        return 6
    elif x == 'september':
        return 7
    elif x == 'october':
        return 8
    elif x == 'november':
        return 9
    elif x == 'december':
        return 10

# loop allows only a real month to be allowed as input
while True:
    # 'a' is the month of the year with 1 being March and 12 being February
    month = raw_input('What month are you looking in? ').lower()
    if check_input(month):
        a = convert_month_to_int(month)
        break
    else:
        print 'Please pick REAL month.'
        print ''

# 'b' is the day of the month that the date in question is
b = int(raw_input('What day are you lookin for? '))

# 'c' is the year in that century. eg: 19(91)
c = int(raw_input('What are the last two digits of the year you are looking in? '))

# 'd' is the century that the date falls in. eg: (19)91
d = int(raw_input('What are the first two digits of the year you are lookin in? '))

# In Zeller's algorithm the months of January and February use the preceding year. This changes the year to match.
if a == 12 or a == 11:
    if c == 00:
        c = 99
        d -= 1
    else:
        c -= 1


# MATH to determine the day of the week
w = (13*a - 1) / 5
x = c / 4
y = d / 4
z = w + x + y + b + c - 2 * d

# 'r' is the day of the week with 0 being Sunday and 6 being Saturday.
r = z % 7

weekday = define_weekday(r)

# print r
# print a
# print b
# print str(d)+str(c)

print ''
print month + ',', b, str(d) + str(c), 'lands on a', weekday
