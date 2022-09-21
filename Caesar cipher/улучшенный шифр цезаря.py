import time

little_eng = [chr(i) for i in range (ord('a'), ord('z')+1)]
big_eng = [chr(i) for i in range (ord('A'), ord('Z')+1)]

print('введите строку: ')
s = str(input())
s1 = ''
for i in s:
    if i.isalpha() or i.isspace():
        s1 += i
    else:
        s1 += ' '
c = list(s1.split())
c1 = list(s.split())
length = list()
for i in c:
    length += [len(i)]

print('шифрованный текст: ')
time.sleep(0.5); print(3); time.sleep(0.5); print(2); time.sleep(0.5); print(1)

for word in range (len(c1)):
    for i in c1[word]:
        if i in little_eng:
            print(little_eng[(little_eng.index(i)+length[word])%26], end = "")
        elif i in big_eng:
            print(big_eng[(big_eng.index(i)+length[word])%26], end = "")
        elif i not in little_eng and i not in big_eng:
            print(i, end = "")
    print(' ', end = "")

print('', '', '', '', 'нажмите Enter для выхода', sep ='\n')
a = input()
