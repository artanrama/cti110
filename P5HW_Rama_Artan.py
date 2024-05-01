#Artan Rama

#April 28 2024

#P5HW

#Use of loops, functions and module import to complete assignments and make the program a menu driven program. Meaning the program is to display a list of options to the user to choose from.

#

import random

def generate_numbers():
    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99)
    return num1, num2

def add_numbers():
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    while True:
        user_answer = int(input(f"{num1} + {num2} Enter Answer.?"))
        if user_answer == correct_answer:
            return True
        elif user_answer < correct_answer:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")

def subtract_numbers():
    num1, num2 = generate_numbers()
    correct_answer = num1 - num2
    while True:
        user_answer = int(input(f"{num1} - {num2} Enter Answer.? "))
        if user_answer == correct_answer:
            return True
        elif user_answer < correct_answer:
            print("Sorry, guess is too low")
        else:
            print("Sorry, guess is too high")

def main():
    while True:
        print("Welcome To THe Math Quiz")
        print("Main Menu:")
        print("------------------------------")
        print("1. Adding Randomm Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")

        choice = input("Please Choose One OF The Menu Options:")

        if choice == "1":
            if add_numbers():
                print("Congratulations!!!! Your answer is correct.")
            else:
                print("Try again:")
        elif choice == "2":
            if subtract_numbers():
                print("Congratulations!!!! Your answer is correct.")
            else:
                print("Try again:")
        elif choice == "3":
            print("Thank you for playing...........")
            print("Bye!!")
            break
     
if __name__ == "__main__":
 main()