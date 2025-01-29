course_hours = []
course_grades = []

for i in range(1, 5):
    hours = int(input(f"Course {i} hours: "))
    grades = int(input(f"Grade for course {i}: "))

    course_hours.append(hours)
    course_grades.append(grades)


Total_Hours = sum(course_hours)
print(f"Total hours: ", Total_Hours)

Total_quality = sum(course_hours[i] * course_grades[i] for i in range(4))
print(f"Total quality points: ", Total_quality)

GPA = (Total_quality / Total_Hours)
print(f"Your GPA for this semester is ", round(GPA, 2))
