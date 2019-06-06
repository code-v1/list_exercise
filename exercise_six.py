
students = ['bob', 'will','henry']
foods = (
    'burgers',
    'pickles',
    'donuts'
    
)
 
 
cohort = []

for index, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[index]
    })

for student in cohort:
    print(student)
    

      

