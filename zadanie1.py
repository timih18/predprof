import csv


mn = set()
# 9г - 0, 11в - 1, 9т - 2, 8х - 3, 11и - 4
sp = ['9г', '11в', '9т', '8х', '11и']
sp1 = [0] * 5
sp2 = [0] * 5

with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)
    # print(answer)
    for num, name, title, clazz, score in answer:
        if 'Старокожев Артём' in name:
            print('Он учится в', clazz)
        if score != 'None':
            for i in range(len(sp)):
                if clazz == sp[i]:
                    sp1[i] = sp1[i] + int(score)
                    sp2[i] += 1

with open('student_new.csv', 'w', newline='') as file:
    write = csv.writer(file)
    write.writerow(answer[0])
    answer = answer[1:]
    for num, name, title, clazz, score in answer:
        if score != 'None':
            write.writerow([num, name, title, clazz, score])
        else:
            write.writerow([num, name, title, clazz, sp1[sp.index(clazz)] / sp2[sp.index(clazz)]])

