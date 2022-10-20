import re

def surnamesList(filename):
    surnames = [] #сюда вывод фамилий
    rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #для сортировки
    for string in filename:
        fios = re.findall(r'[А-ЯЁ](?:[а-яё]|[А-ЯЁ])* [А-ЯЁ]\.[А-ЯЁ]\.', string) #поиск фамилии + инициалов
        for elem in fios:
            surnames.extend(elem.split()[::2])# выбор именно фамилии+ добавление фамилии в конец списка
    surnames.sort(key=lambda a: rus_alphabet.index(a[0]))#сортировка по возрастанию буквы
    return surnames

for i in range(5):
    print('Список фамилий в файле' + str(i + 1))
    fin = open('test' + str(i + 1) + '.txt', encoding='UTF-8')
    l = surnamesList(fin)# передача списка в переменную для сменяемости теста
    for j in range(len(l)):
        print(l[j])
    print("\n")