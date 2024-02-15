import csv


with open('example_txt.txt', encoding='utf8') as file:
    answer = []
    for i in file:
        sp = i.strip().split('*')
        answer.append(sp)

with open('result.csv', 'w', encoding='utf8', newline='') as file:
    write = csv.writer(file)
    write.writerows(answer)
