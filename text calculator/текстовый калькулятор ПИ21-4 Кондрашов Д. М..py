import tkinter, math

values_dict = {'ноль': 0, 'один': 1, 'одна': 1, 'два': 2, 'две': 2, 'три': 3, 'четыре': 4, 'пять': 5,
               'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12,
               'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17,
               'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50,
               'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90, 'сто': 100, 'двести': 200,
               'триста': 300, 'четыреста': 400, 'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700,
               'восемьсот': 800, 'девятьсот': 900, 'плюс': '+', 'минус': '-', 'делить': '/', 'от': '',
               'разделить': '/', 'умножить': '*', 'на': '', 'сотая': '00', 'десятая': '10', 'десятых': '10',
               'сотых': '00', 'целых': '',  'целая': '', 'сотые': '00', 'тысячных': '000', 'тысячные': '000',
               'тысячная': '000', 'и': '.', 'скобка': '', 'открывается': '(', 'закрывается': ')', 'в': '',
               'степени': '**', 'пи': 'math.pi', 'косинус': 'math.cos', 'синус': 'math.sin', 'тангенс': 'math.tan'}
numbers_dict = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
                9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать',
                15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать',
                20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
                80: 'восемьдесят', 90: 'девяносто', 100: 'сто', 200: 'двести', 300: 'триста', 400: 'четыреста',
                500: 'пятьсот', 600: 'шестьсот', 700: 'семьсот', 800: 'восемьсот', 900: 'девятьсот', '': ''}


def deleter():  # функция очистки поля ответа и поля ввода
    lable_three['text'] = ''
    entry_one.delete(0, tkinter.END)
    entry_one.focus_set()


def glue(n: list):  # функция удаления лишних нулей в записи числа
    if len(n) == 2 and n[0] == '0' and len(n[1]) == 1:
        n[0] = ''  # замена 0 в записи сторичного числа
    if len(n) == 2 and n[0] in '2030405060708090' and n[1] == '0':
        del n[1]  # удаление лишнего нуля в записи десяток
    elif len(n) == 3 and n[0] == '0' and len(n[1]) == 2:
        n[0] = ''  # замена 0 в записи тысячиричного нуля, если десятки
        if n[1] == '10' and n[2] in '123456789':
            n[1] = str(int(n[1]) + int(n[2]))
            del n[2]
    elif len(n) == 3 and n[0] == '0' and n[1] == '0':
        n[0], n[1] = '', ''  # замена 0 в записи тысячиричного нуля, если сотни
    elif len(n) >= 1 and n[0] == '10':  # пример 10, 1 -> 11
        n[0] = str(int(n[0]) + int(n[1]))
        del n[1]
    elif len(n) == 3 and len(n[0]) == 3:
        if n[1] == '10' and n[2] != '0':  # пример 100, 10, 1 -> 100, 11
            n[1] = str(int(n[1]) + int(n[2]))
            del n[2]
        elif len(n[1:]) >= 1 and n[1] == '0' and n[2] != '0':  # пример 100, 0, 1 -> 100, 1
            del n[1]
        elif n[1] == '0' and n[2] == '0':  # пример 100, 0, 0 -> 100
            del n[1]
            del n[1]
        elif n[1] in '102030405060708090' and n[2] == '0':
            del n[2]

def calc():
    entry_one.focus_set()  # перевод текстового курсора на строку
    lable_three['text'], output_text, input_text, z, q = '', [], entry_one.get(), 0, True
    if len(input_text) == 0:
        lable_three['text'] = 'пустая строка'
    elif len(input_text.split()) != len([True for word in input_text.split() if word in values_dict]):
        lable_three['text'] = 'введены неверные символы'
    else:
        for word in input_text.split():
            output_text += [values_dict[word]]  # перевод слов в знаки
        while '' in output_text:  # удаление лишних пустных символов
            output_text.pop(output_text.index(''))
        while '10' in output_text or '00' in output_text or '000' in output_text:
            if z == len(output_text):
                break
            if output_text[z] == '10':  # проверка на десятиричное число
                if len(str(output_text[z-1])) == 1 and output_text[z-2] == '.':
                    del output_text[z]
                    continue
                else:
                    lable_three['text'] = 'ошибка записи десятичного числа (десятых)'
                    q = False
                    break
            if output_text[z] == '00':  # проверка на сторичное число
                if isinstance(output_text[z-1], int) and len(str(output_text[z-1])) == 1 and output_text[z-2] == '.':
                    output_text.insert(z-1, '0')  # запись формата 0.01
                    del output_text[z+1]
                    z = 0
                elif isinstance(output_text[z-1], int) and len(str(output_text[z-1])) == 1 and \
                        isinstance(output_text[z-2], int) and 100 > output_text[z-2] > 19 and output_text[z-3] == '.' or \
                        len(str(output_text[z-1])) == 2 and 9 < output_text[z-1] < 20 and output_text[z-2] == '.' and\
                        output_text[z-3] == '.':
                    del output_text[z]  # запись формата 0.11 | 0.21
                    continue
                else:
                    lable_three['text'] = 'ошибка записи десятичного числа (сотых)'
                    q = False
                    break
            if output_text[z] == '000':  # проверка на тысячеричное число
                if isinstance(output_text[z-1], int) and len(str(output_text[z-1])) == 1 and output_text[z-2] == '.':
                    output_text.insert(z-1, '0')  # запись формата 0.001
                    output_text.insert(z-1, '0')
                    del output_text[z+2]
                    z = 0
                elif isinstance(output_text[z-1], int) and len(str(output_text[z-1])) == 1 \
                        and isinstance(output_text[z-2], int) and len(str(output_text[z - 2])) == 2 and 19 < \
                        output_text[z - 2] < 100 and output_text[z-3] == '.':
                    output_text.insert(z-2, '0')  # запись формата 0.021
                    del output_text[z+1]
                    z = 0
                elif isinstance(output_text[z-1], int) and len(str(output_text[z-1])) == 2 \
                        and 10 < output_text[z-1] < 20 and output_text[z-2] == '.':
                    output_text.insert(z-1, '0')  # запись формата 0.011
                    del output_text[z+1]
                    z = 0
                elif isinstance(output_text[z - 1], int) and len(str(output_text[z-1])) == 1 and isinstance(output_text[z - 2], int) \
                        and len(str(output_text[z - 2])) == 2 and 19 < output_text[z-2] < 100 and isinstance(output_text[z - 3], int) \
                        and len(str(output_text[z - 3])) == 3 and output_text[z-4] == '.':
                    del output_text[z]  # запись формата 0.111
                    continue
                else:
                    lable_three['text'] = 'ошибка записи десятичного числа (тысячных)'
                    q = False
                    break
            z += 1
        output_text.append('')
        if q:
            try:
                made_numbers_list, k = [], 0
                if output_text != [0, ''] and output_text != [0, '.', 0, '']:
                    for i in output_text:
                        if isinstance(i, int):
                            k += i
                        else:
                            if k != 0:
                                made_numbers_list += [str(k), i]
                                k = 0
                            else:
                                made_numbers_list += [i]
                else:
                    made_numbers_list = ['0']
                solution = str(round(eval(''.join(made_numbers_list)), 3))
                if -1000 <= float(solution) <= 1000:
                    if '-' in solution:
                        final, solution = ['минус'], solution[1:]
                    else:
                        final = []
                    if '.' in solution:  # случай дроби
                        k1, k2 = 1, 1
                        n1, n2 = [i for i in solution[:solution.index('.')]], [i for i in solution[solution.index('.')+1:]]
                        n1.reverse()  # число до запятой
                        n2.reverse()  # число после запятой
                        for i in range(len(n1)):
                            n1[i] = str(int(n1[i]) * k1)
                            k1 *= 10
                        for i in range(len(n2)):
                            n2[i] = str(int(n2[i]) * k2)
                            k2 *= 10
                        n1.reverse(); n2.reverse(); glue(n1); glue(n2)
                        k = 'десятых' if len(n2) == 1 and len(n2[0]) == 1 else 'сотых' if len(n2) == 2 and \
                             len(n2[1]) == 1 or len(n2) == 1 and 10 < int(n2[0]) < 20  \
                             else 'тысячных'  # добавление в конец фразы
                        final = final + [numbers_dict[int(elem)] for elem in n1] + ['целых и'] + \
                                [numbers_dict[int(elem)] for elem in n2 if elem != ''] + [k]
                        lable_three['text'] = ' '.join(final)  # запись собранного числа
                    else:  # случай целого числа
                        n1, k1 = [i for i in solution], 1
                        n1.reverse()
                        for i in range(len(n1)):
                            n1[i] = str(int(n1[i]) * k1)
                            k1 *= 10
                        n1.reverse(); glue(n1)
                        lable_three['text'] = ' '.join(final + [numbers_dict[int(elem)] for elem in n1])
                else:
                    lable_three['text'] = 'получилось необрабатываемое число'
            except ZeroDivisionError:
                lable_three['text'] = 'нельзя делить на ноль'
            except SyntaxError:
                lable_three['text'] = 'неккоректный баланс вложенности скобок либо ошибка в записи операций'
            except:
                lable_three['text'] = 'произошла какая-то ошибка'


def enter(event):
    if event.char == '\r':
        calc()
    elif event.keycode == 16:
        deleter()
    elif event.char == '\x1b':
        quit()


win = tkinter.Tk()
win.title('Текстовый калькулятор')
win.geometry("1000x80+150+150")
win.resizable(False, False)
win.config(bg='#696969')
lable_one = tkinter.Label(win, text='Введите значения:', bg='#696969', font=('Times New Roman', 14)).grid(row=0, column=0)
entry_one = tkinter.Entry(win, background='#696969', font=('Times New Roman', 12), width=100)
entry_one.grid(row=0, column=1)
button_one = tkinter.Button(win, text='=', bg='#696969', font=('Times New Roman', 14), activebackground='#696969', command=calc)
win.bind('<Key>', enter)
button_one.grid(row=0, column=2, sticky='we')
lable_two = tkinter.Label(win, text='Ответ:', bg='#696969', font=('Times New Roman', 14)).grid(row=1, column=0, sticky='w')
lable_three = tkinter.Label(win, bg='#696969', font=('Times New Roman', 14))
lable_three.grid(row=1, column=1)
button_two = tkinter.Button(win, text='Del', bg='#696969', font=('Times New Roman', 12), activebackground='#696969', command=deleter).grid(row=1, column=2)
entry_one.focus_set()
win.mainloop()

# итого получились номера: 1) 3) 4) 5) 8) 10): 2 + 3 + 3 + 1 + 2 + 2
