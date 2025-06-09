import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eddie", "Fred"]

student_scores = {name:random.randint(0,100) for name in names}

passed_students = {name:score for (name,score) in student_scores.items() if score>40}

print(student_scores)
print(passed_students)