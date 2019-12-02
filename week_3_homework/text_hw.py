# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки

with open('referat.txt', 'r',encoding='utf-8') as text_file:
    content = text_file.read()
    print(content)
    print('длинна строки ' + str(len(content)))
    
    # Подсчитайте количество слов в тексте
    splited_content = content.split(' ')
    print ('количество символов ' + str(len(splited_content)))

with open ('referat_2.txt', 'w', encoding='utf-8') as write_text:
    write_text.write(content.replace('.','!'))

# Сохраните результат в файл referat2.txt