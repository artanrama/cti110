#Artan Rama

#March 7 2024

#P2HW1

#Assignment assess student ability to edit and enhance exiting programs



print("This program calculates and displays travel expenses5")
print()
budget = int(input("Enter Budget: "))
print()
destination =(input("Enter your travel destination: "))
print()
gas= int(input("How much do you think you will spend on gas? "))
print()
accomodation= int(input("Approximately how much will you need for accomodation/hotel? "))
print()
food= int(input("Last how much do you need for food? "))
print()
print("----------Travel Expenses-------")
print("Location: ",destination)
print(f"Initial Budget is: ${budget:.2f}")
print()
print(f"Fuel is: ${gas:.2f}")
print(f"Accomodation is: ${accomodation:.2f}")
print(f"Food is: ${food:.2f}")
print()
balance = budget - gas - accomodation - food
print(f"Remaining Balance:  ${balance:.2f}")
