import yaml
import json
import time

start_time = time.perf_counter()
with open("timetable.json", "r", encoding="UTF-8") as json_in, open("yamldop2.yaml", "w", encoding="UTF-8") as yaml_out:
    jsonobject = json.load(json_in)
    yaml.dump(jsonobject, yaml_out, encoding="utf-8", allow_unicode=True)


file = "yamldop2.yaml"
print(open(file).read())
print('Programm running time:', time.perf_counter() - start_time)


input = open('timetable.json')
output = open('timetable.yaml', 'w')
import time

start_time = time.perf_counter()

strings = input.read().split('\n')
input.close()
for i in range(len(strings)):
    if ':' in strings[i]:
        strings[i] = strings[i].replace('[', '')
        strings[i] = strings[i].replace('{', '')
        strings[i] = strings[i].replace('"', '')
        strings[i] = strings[i].replace(']', '')
        strings[i] = strings[i].replace('}', '')
        strings[i] = strings[i].replace(',', '')
        output.write('\n')
        output.write(strings[i])
        print(strings[i])
    else:
        continue
output.close()
print('\n')
print('Programm running time:', time.perf_counter() - start_time)
print("Done!")
'''
#TODO               import time
#TODO               start_time = time.perf_counter()

#TODO               print('Programm running time:', time.perf_counter() - start_time)