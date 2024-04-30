#Artan Rama

#March 22 2024

#P3H1

#Assignment assess student understanding of decision structures
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter the employee's pay rate: "))

def calculate_pay(hours_worked, pay_rate):
    if hours_worked <= 40:
        regular_pay = hours_worked * pay_rate
        overtime_hours = 0
        overtime_pay = 0
    else:
        regular_pay = 40 * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)

    gross_pay = regular_pay + overtime_pay
    return regular_pay, overtime_hours, overtime_pay, gross_pay

regular_pay, overtime_hours, overtime_pay, gross_pay = calculate_pay(hours_worked, pay_rate)

print("-------------------------------------------------------------")
print("Employee's name:", employee_name)
print("Hours Worked   Pay Rate    Overtime Hours    Overtime Pay    Regular Hourly Pay   Gross Pay")
print(f'{hours_worked:<15.2f}{pay_rate:<12.2f}{overtime_hours:<17.2f}{overtime_pay:<16.2f}${regular_pay:<20.2f}${gross_pay:.2f}')