#Artan Rama

#March 23 2024   

#P3HW2

#Assignment assess student understanding of decision structures

def main():
    employee_name=input("Enter employees name: ")
    hours_worked=float(input("Enter numbers of hourse worked:  "))
    pay_rate=float(input("Enter the employee's pay rate: "))
print()
def calculate_pay(hours_worked, pay_rate):
    if hours_worked <= 40:
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0
    else:
        regular_pay = 40 * pay_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)

    gross_pay = regular_pay + overtime_pay
    return regular_pay, overtime_hours, overtime_pay, gross_pay   
print("-------------------------------------------------------------")
print("Employees name: John Smith")
var1=float(input("Enter a value with a decimal: "))
var2=float(input("Enter a value with a decimal: "))     
var3=float(input("Enter a value with a decimal: "))
var4=float(input("Enter a value with a decimal: "))
var5=float(input("Enter a value with a decimal: "))
var6=float(input("Enter a value with a decimal: "))
print("Hours Work   Pay Rate    OverTime    OverTime Pay    RegHour Pay Gross Pay")
print(f'{var1}{var2}{var3}{var4}{var5}{var6}')
