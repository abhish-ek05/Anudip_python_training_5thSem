total = 0
subject = 1
while subject<=5:
    marks = float(input(f"Enter marks of Subject {subject}: "))
    subject+=1
    if marks<=100:
        total += marks
    else:
        print("marks entered are invalid  Re-enter")
        marks = float(input("again enter marks:"))

percentage = total / 5

if percentage >= 90:
    grade = "A+"


elif percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "Fail"


print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)