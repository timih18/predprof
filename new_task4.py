import csv
import random


def passw_gen():
    s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklmnbvcxz1234567890'
    res = ''
    for _ in range(8):
        res = res + random.choice(s)
    lower = 0
    upper = 0
    nums = 0
    for i in range(len(res)):
        if 'A' <= res[i] <= 'Z':
            upper += 1
        if 'a' <= res[i] <= 'z':
            lower += 1
        if '0' <= res[i] <= '9':
            nums += 1
    if lower != 0 and upper != 0 and nums != 0:
        return res
    else:
        passw_gen()


with open('students (1).csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)

    for i in range(len(answer)):
        if answer[i][1] == 'Name':
            answer[i].append('login')
            answer[i].append('password')
        else:
            sp = answer[i][1].split()
            login = sp[0] + '_' + sp[1][0] + sp[2][0]
            answer[i].append(login)
            answer[i].append(passw_gen())


with open('students_password (new).csv', 'w', encoding='utf8', newline='') as file:
    write = csv.writer(file)
    itog = write.writerows(answer)

