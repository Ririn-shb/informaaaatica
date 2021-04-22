#5 Список стипендиатов
name = ['Войкин Владимир','Разенко Виктория','Ложкина Юлия','Калинина Татьяна', 'Тишина Дарья', 'Самостроенко Алена']
x = [[2,4,3,3],[5,5,4,5],[3,5,4,4],[4,4,4,5],[4,3,4,4],[4,5,4,5]]
w = ['Русский язык','Математика','Физика', 'История']
y = 0
print('Стипендиаты:')
for i in range(len(name)):
    k = 0
    for j in range(len(x[i])):
        if (x[i][j] == 5) or (x[i][j] == 4):
            k+=1
    if k == 4:
        y+=1
print('Кол-во: ', y, 'человек')

#6 Список отстающих
print('Отстают по дисциплине:')
for i in range(len(name)):
    k = 0
    for j in range(len(x[i])):
        if x[i][j] == 2:
            k+=1
    if k >= 1:
        print(name[i])

#4 Список студентов на повышенную стипендию
print('Получают повышенную стипендию: ')
for i in range(len(name)):
    k = 0
    for j in range(len(x[i])):
        if x[i][j] == 5:
            k+=1
    if k == 4:
        print(name[i])

#1 Список группы с оценками
for i in range(len(name)):
    summ = 0
    for j in range(len(x[i])):
        summ += x[i][j]
    print(name[i],':',x[i])

#2 Средний балл студентов
for i in range(len(name)):
    summ = 0
    for j in range(len(x[i])):
        summ += x[i][j]
        srd = summ/4
    print(name[i],':','Средний балл: ',srd)

#3 Средний балл группы по дисциплине
for q in range(len(x[i])):
    sr=0
    for u in range(len(x)):
        sr+=x[u][q]
    print(w[q],':',round(sr/6,2))
