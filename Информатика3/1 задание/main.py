import re


def count(filename):
    pattern = re.compile(r':<{P')
    check_file = open(filename)#проверяемый файл
    file_str = check_file.read()#чтение проверяемого файла
    return len(pattern.findall(file_str))#возвращает количество найденных паттернов


for i in range(5):
    test = 'test' + str(i + 1) + '.txt'
    print("number of smiles in test", (i + 1), "is: ", count(test))
    print("\n")
