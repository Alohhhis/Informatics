# автоматический вывод смайла по заданному ису (*)
print('Enter your isu number:')
isu_num = int(input())
eye = [":", ";", "X", "8", "="]
nose = ["-", "<", "-{", "<{"]
mouth = ["(", ")", "O", "|", "\ ", "/", "P"]
e, n, m = int(isu_num % 5), int(isu_num % 4), int(isu_num % 7)
isu_e = eye[e]
isu_n = nose[n]
isu_m = mouth[m]
print('Your smile is:')
s = isu_e + isu_n + isu_m
print(s)