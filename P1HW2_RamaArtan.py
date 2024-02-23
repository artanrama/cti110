#Artan Rama

#Feb 23 2024

#P1HW2

#For this assignment you will create a program that does some basic math on numbers that are entered

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
print("Initial Budget: ",budget)
print()
print("Fuel: ", gas)
print("Accomodation: ",accomodation)
print("Food: ", food)
print()
balance = budget - gas - accomodation - food
print("Remaining Balance: ", balance)
