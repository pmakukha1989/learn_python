print ('Вывести последнюю букву в слове')
word = 'Архангельск'
# ???
print (word)
print ('last letter is: ' + word [-1])
print('------')
print ('Вывести количество букв "а" в слове')
word = 'Архангельск'
print (word)
word = str.lower (word)
print ( word.count('а'))

print('------')
print ('Вывести количество гласных букв в слове')
word = 'Архангельск'
print (word)
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
print (vowels)
vowels_count = 0
word = str.lower (word)
for symbol in word:
    for letter in vowels:
        if symbol == letter :
            vowels_count= vowels_count+1

print ('количество гласных ' + str(vowels_count))

print('------')
print ('Вывести количество слов в предложении')
sentence = 'Мы приехали в гости'

sentence = sentence.split(' ')
print(sentence)
print (len(sentence))

# sentence= str(sentence)
# print(sentence)

# spaces_count = 1
# for symbol in sentence:
#          if symbol == ' ':
#              spaces_count= spaces_count+1

# print(spaces_count)
print('------')


print ('Вывести первую букву каждого слова на отдельной строке')
sentence = 'Мы приехали в гости'
sentence= sentence.split(' ')
print (sentence)
for word in sentence:
    print (word[0])


print('------')
print (' Вывести усреднённую длину слова.')
sentence = 'Мы приехали в гости'
sentence = sentence.split(' ')
print (sentence)
words_counter=0
letters_sum=0
for word in sentence:
    words_counter=words_counter+1
    letters_sum=letters_sum +len(word)
avg_symbols= letters_sum / words_counter
avg_symbols = str(avg_symbols)
print('avg_symbols ' + avg_symbols)


