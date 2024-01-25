import csv

empty_score = set()
classes = ['9г', '11в', '11и', '8х', '9т']
summaries = [0] * 5
counts = [0] * 5

with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)

    for num, name, title, clazz, score in answer:
        if 'Хадаров Владимир' in name:
            print('Ты получил:', score, 'за проект', title)

        '''if score == 'None':
            empty_score.add(clazz)
            Узнаем классы с пустыми оценками
            '''
    # print(empty_score) Выведем на экран классы с пустыми оценками
        if clazz in classes and score != 'None':
            summaries[classes.index(clazz)] += int(score)
            counts[classes.index(clazz)] += 1

with open('student_new.csv', 'w', newline='') as file:
    write = csv.writer(file)
    write.writerow(answer[0])
    answer = answer[1:]
    for num, name, title, clazz, score in answer:
        if score != 'None':
            write.writerow([num, name, title, clazz, score])
        else:
            ind = classes.index(clazz)
            write.writerow([num, name, title, clazz, str(summaries[ind]/counts[ind])[:5]])
