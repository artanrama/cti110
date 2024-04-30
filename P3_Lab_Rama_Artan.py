#Artan Rama

#March 17 2024

#P3Lab_LeapYear

#Assignment tests student's knowledge of how to write code that displays information to users

is_leap_year = False
print()   
input_year = int(input())
print()
if (input_year % 400 == 0):
    if (input_year % 4 == 0):
        print(input_year, "- leap year")
    else:
        print(input_year, "- not a leap year")
else:
    if (input_year % 100 != 0) and (input_year % 4 == 0):
        print(input_year, "- leap year")
    else:
        print(input_year, "- not a leap year") 