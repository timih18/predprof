from random import randint
import csv


with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)
    answer = answer[1:]

used_passwords = {''}

with open('students_password.csv', 'w', encoding='utf8', newline='') as file:
    write = csv.writer(file)
    write.writerow(['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    for ID, FIO, title, CLASS, score in answer:
        login = f"{FIO[:FIO.find(' ')]}_{FIO[FIO.find(' ') + 1]}{FIO[FIO.rfind(' ') + 1]}"
        checker = set()
        password = ''
        symbols = ['QWERTYUIOPASDFGHJKLMNBVCXZ', 'qwertyuiopasdfghjklzxcvbnm', '1234567890']
        while checker != {0, 1, 2} and password in used_passwords:
            password = ''
            checker = set()
            for _ in range(8):
                ind = randint(0, 2)
                checker.add(ind)
                password = password + symbols[ind][randint(0, len(symbols[ind]) - 1)]
        used_passwords.add(password)
        write.writerow([ID, FIO, title, CLASS, score, login, password])
