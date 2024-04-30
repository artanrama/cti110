#Artan Rama

#April 21 2024

#P5Lab

def days_in_feb(user_year):
    if user_year % 4 == 0 and (user_year % 100 != 0 or user_year % 400 == 0):
        return 29
    else:
        return 28

if __name__ == '__main__':
    yearinput = int(input())
    dayinput = days_in_feb(yearinput)
    print(f"{yearinput} has {dayinput} days in February.")