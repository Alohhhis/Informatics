import re

def stud_list(filename):
    group_num = 'P3121'
    students = [] #туда записываются студенты
    for lines in fin:
        if re.fullmatch(r'[А-ЯЁ](?:[а-яё]|[А-ЯЁ])+ ([А-ЯЁ]\.){2} [A-Z]\d+\s', lines):
            surname, initials, group = lines.split()# разделение фамилии, инициалов и группы по пробелу
            if initials[0] != initials[2] or group != group_num:
                students.append(surname + ' ' + initials + ' ' + group)
    return students


for i in range(5):
    print('Список студентов №' + str(i+1))
    fin = open('test' + str(i+1) + '.txt', encoding='UTF-8')
    l = stud_list(fin)
    for j in range(len(l)):
        print(l[j])
    print("\n")
