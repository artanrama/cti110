# I was supposed to put a comment here
# Artan Rama


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

grade1 = float(input(f'Enter grade for Module 1:'))
print()
grade2 = float(input(f'Enter grade for Module 2:'))
print()
grade3 = float(input(f'Enter grade for Module 3:'))
print()
grade4 = float(input(f'Enter grade for Module 4:'))
print()
grade5 = float(input(f'Enter grade for Modlue 5:'))
print()
grade6 = float(input(f'Enter grade for Module 6:'))
print()
# Add grades entered to a list
print()
gradelist = []
gradelist.append(grade1)
gradelist.append(grade2)
gradelist.append(grade3)
gradelist.append(grade4)
gradelist.append(grade5)
gradelist.append(grade6)
print()
# TO DO: determine lowest, highest , sum and average for grades
print()
min_grade =min(gradelist)
max_grade=max(gradelist)
length_list=len(gradelist)
sum_list =sum(gradelist)
avg =sum_list/length_list
print()
# determine letter grade for average
print()
print('---------RESULTS--------')
print(f"LOWEST GRADE:   {min_grade:.2f}")
print(f"HIGEST GRADE:   {max_grade:.2f}")
print(f"SUM OF GRADE:   {sum_list:.2f}")
print(f"AVERAGE:        {avg:.2f}")
print()
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')    
else:
    print('Your grade is: F')
print()


# TO DO: finish this





