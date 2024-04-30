#Artan Rama

#March 7 2024

#Assignment assess student understanding of Lists

grade1= float(input(f"Enter grade for Module 1 : "))
print()
grade2= float(input(f"Enter grade for Module 2 : "))
print()
grade3= float(input(f"Enter grade for Module 3 : "))
print()
grade4= float(input(f"Enter grade for Module 4 : "))
print()
grade5= float(input(f"Enter grade for Module 5 : "))
print()
grade6= float(input(f"Enter grade for Module 6 : "))
print()
gradelist=[]
gradelist.append(grade1)
gradelist.append(grade2)
gradelist.append(grade3)
gradelist.append(grade4)
gradelist.append(grade5)
gradelist.append(grade6)
print()
min_grade= min(gradelist)
max_grade= max(gradelist)
length_list=len(gradelist)
sum_list=sum(gradelist)
avg=sum_list/length_list
print ("------------RESULTS----------")
print (f"Lowest Grade:     {min_grade:.2f}")
print (f"Higest Grade:     {max_grade:.2f}")
print (f"Sum of Grades:    {sum_list:.2f}")
print (f"Average:          {avg:.2f} ")

