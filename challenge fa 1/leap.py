def checkLeapYear(year):
#importing the calendar module
    import calendar
#returning boolean value based on given year is leap year or not
    return(calendar.isleap(year))

# Driver Code for the leap year program in python 
#taking input (year) from the user
year = int(input("Enter the year: "))
if (checkLeapYear(year)):
#if checkLeapYear function returns true
    print("Leap Year")
else:
#if checkLeapYear function returns false
    print("Not a Leap Year")