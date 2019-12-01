print('Задание 1')
print('Дан список учеников, нужно посчитать количество повторений каждого имени ученика')

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
print(students)

uniq_student_names= []
for name in students:
    if name  not in  uniq_student_names:
        uniq_student_names.append(name)



for name in uniq_student_names:
    count=0
    for name_count in students:
        if name_count['first_name'] == name['first_name']:
            count=count+1
    
    print (name['first_name']+': '+ str(count))


# # Пример вывода:
# # Вася: 1
# # Маша: 2
# # Петя: 2

print('------')
print('Задание 2')
print ('Дан список учеников, нужно вывести самое часто повторящееся имя.')
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]



uniq_student_names= []
for name in students:
    if name  not in  uniq_student_names:
        uniq_student_names.append(name)
    print (name['first_name'])



max_count=0
max_name=''
for name in uniq_student_names:
    count=0
    for name_count in students:
        if name_count['first_name'] == name['first_name']:
            count=count+1
    if count>max_count : 
        max_name = name['first_name']
        max_count=count

print('Самое частое имя среди учеников: '+ max_name)

    
    

# # Пример вывода:
# # Самое частое имя среди учеников: Маша
print('-----')
print('Задание 3')

print('Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.')

school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
print(school_students)
print('')
def most_popular_in_class (class_students):
    uniq_student_names= []

    for name in class_students:
        if name  not in  uniq_student_names:
            uniq_student_names.append(name)
            #print (name['first_name'])



    max_count=0
    max_name=''
    for name in uniq_student_names:
        count=0
        for name_count in class_students:
            if name_count['first_name'] == name['first_name']:
                count=count+1
        if count>max_count : 
            max_name = name['first_name']
            max_count=count

    #print('Самое частое имя среди учеников класса: '+ max_name)
    return (max_name)

classes_count=0
for schools_class in school_students:
    classes_count=classes_count+1
    print ('Самое частое имя в классе '+str(classes_count)+': ' + most_popular_in_class(schools_class))












# # Пример вывода:
# # Самое частое имя в классе 1: Вася
# # Самое частое имя в классе 2: Маша

print('-------')
print('Задание 4')
print('Для каждого класса нужно вывести количество девочек и мальчиков в нём.')

school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


# def sex_checker (is_male_dict, student_name):
#     for name in is_male_dict:
#         print (name)
#         if student_name ==  name:
#             print (is_male_dict[name])
#             #return (is_male_dict['name'])
                 

for schools_class in school:
    male_counter=0
    female_counter=0
    for student_first_name in schools_class['students']:
        if ( is_male[student_first_name['first_name']]):
            male_counter= male_counter+1
        else: 
            female_counter=female_counter+1
    print (schools_class['class'])
    print('male_counter '+ str(male_counter))
    print('female_counter ' + str(female_counter))



#Пример вывода:
# # В классе 2a 2 девочки и 0 мальчика.
# # В классе 3c 0 девочки и 2 мальчика.


print('')
print('Задание 5')

# # По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???
max_male=0
max_female=0

for schools_class in school:
    male_counter=0
    female_counter=0
    for student_first_name in schools_class['students']:
        if ( is_male[student_first_name['first_name']]):
            male_counter= male_counter+1
        else: 
            female_counter=female_counter+1
    print (schools_class['class'])
    print('male_counter '+ str(male_counter))
    print('female_counter ' + str(female_counter))
    if male_counter > max_male:
        max_male_class = schools_class['class']
    if female_counter > max_female:
        max_female_class= schools_class['class']


print('max_male_class '+max_male_class)
print('max_female_class '+max_female_class)
# # Пример вывода:
# # Больше всего мальчиков в классе 3c
# # Больше всего девочек в классе 2a