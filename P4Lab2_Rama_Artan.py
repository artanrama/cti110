#Artan Rama

#April 7 2024

#Assignment tests student's knowledge of how to write code that displays information to users


first_integer = int(input("Enter First Integer: "))
second_integer = int(input("Enter Second Integer: "))

if first_integer > second_integer:
    while first_integer > second_integer:
        print(first_integer, end=" ")
        first_integer += 5
    
else:
    print("Second Intager cannot be less than the first integer!!")