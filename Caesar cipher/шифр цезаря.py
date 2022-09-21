import time


little_eng = [chr(i) for i in range (ord('a'), ord('z')+1)]
big_eng = [chr(i) for i in range (ord('A'), ord('Z')+1)]
little_rus = [chr(i) for i in range (ord('а'), ord('я')+1) if chr(i) != 'ё']
big_rus = [chr(i) for i in range (ord('А'), ord('Я')+1) if chr(i) != 'Ё']

print('введите язык: ')
print('(eng) (рус)')
language = str(input())
while language != 'eng' and language != 'рус':
    print('введите "eng" или "рус"')
    language = str(input())

print('шифруем или дешифруем?')
print('(ш) (д)')
cipher = str(input())
while cipher != 'ш' and cipher != 'д':
    print('введите "ш" или "д"')
    cipher = str(input())

if cipher == 'ш':
    print('введите сдвиг (вправо или влево): ')
    print('(п) (л)')
    shift = str(input())
    while shift != 'п' and shift != 'л':
        print('введите "п" или "л"')
        shift = str(input())

    if shift == 'л':
        if language == 'eng':
            print('введите сдвиг (больше 0 и меньше 27): ')
            n = int(input())
            while n > 26 or n < 1:
                print('введите число от 1 до 26')
                n = int(input())
        elif language == 'рус':
            print('введите сдвиг (больше 0 и меньше 33): ')
            n = int(input())
            while n > 33 or n < 1:
                print('введите число от 1 до 32')
                n = int(input())

        print('введите строку: ')
        s = str(input())
        print('шифрованный текст: ')
        time.sleep(0.5); print(3); time.sleep(0.5); print(2); time.sleep(0.5); print(1)

        if language == 'eng':
            for i in s:
                if i in little_eng:
                    print(little_eng[little_eng.index(i)-n], end = "")
                elif i in big_eng:
                    print(big_eng[big_eng.index(i)-n], end = "")
                elif i not in little_eng and i not in big_eng:
                    print(i, end = "")
        elif language == 'рус':
            for i in s:
                if i in little_rus:
                     print(little_rus[little_rus.index(i)-n], end = "")
                elif i in big_rus:
                    print(big_rus[big_rus.index(i)-n], end = "")
                elif i not in little_rus and i not in big_rus:
                    print(i, end = "")

    elif shift == 'п':
        if language == 'eng':
            print('введите сдвиг (больше 0 и меньше 27): ')
            n = int(input())
            while n > 26 or n < 1:
                print('введите число от 1 до 26')
                n = int(input())
        elif language == 'рус':
            print('введите сдвиг (больше 0 и меньше 33): ')
            n = int(input())
            while n > 33 or n < 1:
                print('введите число от 1 до 32')
                n = int(input())

        print('введите строку: ')
        s = str(input())
        print('шифрованный текст: ')
        time.sleep(0.5); print(3); time.sleep(0.5); print(2); time.sleep(0.5); print(1)

        if language == 'eng':
            for i in s:
                if i in little_eng:
                    print(little_eng[(little_eng.index(i)+n)%26], end = "")
                elif i in big_eng:
                    print(big_eng[(big_eng.index(i)+n)%26], end = "")
                elif i not in little_eng and i not in big_eng:
                    print(i, end = "")
        elif language == 'рус':
            for i in s:
                if i in little_rus:
                     print(little_rus[(little_rus.index(i)+n)%32], end = "")
                elif i in big_rus:
                    print(big_rus[(big_rus.index(i)+n)%32], end = "")
                elif i not in little_rus and i not in big_rus:
                    print(i, end = "")

elif cipher == 'д':
    print('введите строку: ')
    s = str(input())
    print('все возможные варианты: ')
    if language == 'eng':
        for n in range (1, 27):
            for i in s:
                if i in little_eng:
                    print(little_eng[(little_eng.index(i)+n)%26], end = "")
                elif i in big_eng:
                    print(big_eng[(big_eng.index(i)+n)%26], end = "")
                elif i not in little_eng and i not in big_eng:
                    print(i, end = "")
            print()
    elif language == 'рус':
        for n in range (1, 33):
            for i in s:
                if i in little_rus:
                     print(little_rus[(little_rus.index(i)+n)%32], end = "")
                elif i in big_rus:
                    print(big_rus[(big_rus.index(i)+n)%32], end = "")
                elif i not in little_rus and i not in big_rus:
                    print(i, end = "")
            print()
print('', '', '', '' ,'', sep = '\n')
a = int(input('Нажмите Enter для выхода'))
