print (' Задание 1')
print (' Необходимо вывести имена всех учеников из списка с новой строки')

names = ['Оля', 'Петя', 'Вася', 'Маша']
print(names)
for word in names:
    print (word)

print('------')
print('Задание 2')
print('Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.')
names = ['Оля', 'Петя', 'Вася', 'Маша']
print (names)

for word in names:
    lenght = len(word)
    print (f'name {word} symbols {lenght}')


print('------')
print ('Задание 3')

print ('Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика')

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
print (f'names {names}')
print(f'is_male {is_male}')

for name in is_male:
    if is_male[name] == True:
        print (f'{name} is male')
    else:
        print (f'{name} is female')



print('------')
print ('Задание 4')

print('Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней')
# # Пример вывода:
# # Всего 2 группы.
# # В группе 2 ученика.
# # В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print(f'total groups = {len(groups)}')
group_number=0

for gr in groups:
    group_number=group_number+1
    print( f'group number is {str(group_number)}')
    print( f'students count is {len(gr)}')

print('------')
print ('Задание 5')

print('Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.')
# # Пример:
# # Группа 1: Вася, Маша
# # Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
group_number=0

for gr in groups:
    group_number=group_number+1
    to_print =  f'group number is {str(group_number)}, students in group are'

    gr_length= len(gr)
    nm_counter=0
    for nm in gr:
        nm_counter=nm_counter+1
        nm=str(nm)
        if nm_counter < gr_length:

                to_print= to_print+' '+nm+','
        else:  to_print= to_print+' '+nm
    print(to_print)
    

