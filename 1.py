print('Введите имя:')
name=input()
print('Введите фамилию:')
surname=input()
print('Введите дату рождения:')
date=int(input())
print(name, surname, date, sep='_')
name1= surname
surname= name 
name=name1
date+=60
print(name, surname, date, sep='_')

