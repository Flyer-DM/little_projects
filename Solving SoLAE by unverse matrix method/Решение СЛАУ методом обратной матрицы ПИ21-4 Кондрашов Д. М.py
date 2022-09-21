import numpy
import tkinter
import re
import fractions
count = 2
norm_digit = re.compile(r"-?\d+[,.]?\d*")
def remover():
    matrix_a['text'] = ''
    entererror['text'] = ''
    matrix_a['text'] = ''
    matrix_b['text'] = ''
    matrix_result['text'] = ''
    lable_multiply['text'] = ''
    lable_equall['text'] = ''
    matrix_a.grid_remove()
    entererror.grid_remove()
    matrix_a.grid_remove()
    matrix_b.grid_remove()
    matrix_result.grid_remove()
    lable_multiply.grid_remove()
    lable_equall.grid_remove()
def check_count(x, how):
    if x == 3 and how == '+':
        x1enter3.grid(row=4, column=0, ipadx=5, ipady=5, stick='e')
        x2enter3.grid(row=4, column=2, ipadx=5, ipady=5, stick='w')
        x3enter1.grid(row=2, column=4, ipadx=5, ipady=5, stick='w')
        x3enter2.grid(row=3, column=4, ipadx=5, ipady=5, stick='w')
        x3enter3.grid(row=4, column=4, ipadx=5, ipady=5, stick='w')
        x13.grid(row=4, column=1,stick='w')
        x23.grid(row=4, column=3,stick='w')
        x31.grid(row=2, column=5,stick='w')
        x32.grid(row=3, column=5,stick='w')
        x33.grid(row=4, column=5,stick='w')
        eq3.grid(row=4, column=13,stick='w')
        eq3enter.grid(row=4, column=12, ipadx=5, ipady=5, stick='w')
    if x == 4 and how == '+':
        x1enter4.grid(row=5, column=0, ipadx=5, ipady=5, stick='e')
        x2enter4.grid(row=5, column=2, ipadx=5, ipady=5, stick='w')
        x3enter4.grid(row=5, column=4, ipadx=5, ipady=5, stick='w')
        x4enter1.grid(row=2, column=6, ipadx=5, ipady=5, stick='w')
        x4enter2.grid(row=3, column=6, ipadx=5, ipady=5, stick='w')
        x4enter3.grid(row=4, column=6, ipadx=5, ipady=5, stick='w')
        x4enter4.grid(row=5, column=6, ipadx=5, ipady=5, stick='w')
        x14.grid(row=5, column=1, stick='w')
        x24.grid(row=5, column=3, stick='w')
        x34.grid(row=5, column=5, stick='w')
        x41.grid(row=2, column=7, stick='w')
        x42.grid(row=3, column=7, stick='w')
        x43.grid(row=4, column=7, stick='w')
        x44.grid(row=5, column=7, stick='w')
        eq4.grid(row=5, column=13, stick='w')
        eq4enter.grid(row=5, column=12, ipadx=5, ipady=5, stick='w')
    if x == 5 and how == '+':
        x1enter5.grid(row=6, column=0, ipadx=5, ipady=5, stick='e')
        x2enter5.grid(row=6, column=2, ipadx=5, ipady=5, stick='w')
        x3enter5.grid(row=6, column=4, ipadx=5, ipady=5, stick='w')
        x4enter5.grid(row=6, column=6, ipadx=5, ipady=5, stick='w')
        x5enter1.grid(row=2, column=8, ipadx=5, ipady=5, stick='w')
        x5enter2.grid(row=3, column=8, ipadx=5, ipady=5, stick='w')
        x5enter3.grid(row=4, column=8, ipadx=5, ipady=5, stick='w')
        x5enter4.grid(row=5, column=8, ipadx=5, ipady=5, stick='w')
        x5enter5.grid(row=6, column=8, ipadx=5, ipady=5, stick='w')
        x15.grid(row=6, column=1, stick='w')
        x25.grid(row=6, column=3, stick='w')
        x35.grid(row=6, column=5, stick='w')
        x45.grid(row=6, column=7, stick='w')
        x51.grid(row=2, column=9, stick='w')
        x52.grid(row=3, column=9, stick='w')
        x53.grid(row=4, column=9, stick='w')
        x54.grid(row=5, column=9, stick='w')
        x55.grid(row=6, column=9, stick='w')
        eq5.grid(row=6, column=13, stick='w')
        eq5enter.grid(row=6, column=12, ipadx=5, ipady=5, stick='w')
    if x == 6 and how == '+':
        x1enter6.grid(row=7, column=0, ipadx=5, ipady=5, stick='e')
        x2enter6.grid(row=7, column=2, ipadx=5, ipady=5, stick='w')
        x3enter6.grid(row=7, column=4, ipadx=5, ipady=5, stick='w')
        x4enter6.grid(row=7, column=6, ipadx=5, ipady=5, stick='w')
        x5enter6.grid(row=7, column=8, ipadx=5, ipady=5, stick='w')
        x6enter1.grid(row=2, column=10, ipadx=5, ipady=5, stick='w')
        x6enter2.grid(row=3, column=10, ipadx=5, ipady=5, stick='w')
        x6enter3.grid(row=4, column=10, ipadx=5, ipady=5, stick='w')
        x6enter4.grid(row=5, column=10, ipadx=5, ipady=5, stick='w')
        x6enter5.grid(row=6, column=10, ipadx=5, ipady=5, stick='w')
        x6enter6.grid(row=7, column=10, ipadx=5, ipady=5, stick='w')
        x16.grid(row=7, column=1, ipadx=5, ipady=5, stick='w')
        x26.grid(row=7, column=3, ipadx=5, ipady=5, stick='w')
        x36.grid(row=7, column=5, ipadx=5, ipady=5, stick='w')
        x46.grid(row=7, column=7, ipadx=5, ipady=5, stick='w')
        x56.grid(row=7, column=9, ipadx=5, ipady=5, stick='w')
        x61.grid(row=2, column=11, ipadx=5, ipady=5, stick='w')
        x62.grid(row=3, column=11, ipadx=5, ipady=5, stick='w')
        x63.grid(row=4, column=11, ipadx=5, ipady=5, stick='w')
        x64.grid(row=5, column=11, ipadx=5, ipady=5, stick='w')
        x65.grid(row=6, column=11, ipadx=5, ipady=5, stick='w')
        x66.grid(row=7, column=11, ipadx=5, ipady=5, stick='w')
        e6.grid(row=7, column=13, stick='w')
        eq6enter.grid(row=7, column=12, ipadx=5, ipady=5, stick='w')

    if x == 2 and how == '-':
        for i in range (1, 3):
            eval(f'x{i}enter3.grid_remove()')
            eval(f'x3enter{i}.grid_remove()')
            eval(f'x{i}3.grid_remove()')
            eval(f'x3{i}.grid_remove()')
        x3enter3.grid_remove()
        x33.grid_remove()
        eq3.grid_remove()
        eq3enter.grid_remove()
    if x == 3 and how == '-':
        for i in range (1, 4):
            eval(f'x{i}enter4.grid_remove()')
            eval(f'x4enter{i}.grid_remove()')
            eval(f'x{i}4.grid_remove()')
            eval(f'x4{i}.grid_remove()')
        x4enter4.grid_remove()
        x44.grid_remove()
        eq4.grid_remove()
        eq4enter.grid_remove()
    if x == 4 and how == '-':
        for i in range (1, 5):
            eval(f'x{i}enter5.grid_remove()')
            eval(f'x5enter{i}.grid_remove()')
            eval(f'x{i}5.grid_remove()')
            eval(f'x5{i}.grid_remove()')
        x5enter5.grid_remove()
        x55.grid_remove()
        eq5.grid_remove()
        eq5enter.grid_remove()
    if x == 5 and how == '-':
        for i in range (1, 6):
            eval(f'x{i}enter6.grid_remove()')
            eval(f'x6enter{i}.grid_remove()')
            eval(f'x{i}6.grid_remove()')
            eval(f'x6{i}.grid_remove()')
        x6enter6.grid_remove()
        x66.grid_remove()
        e6.grid_remove()
        eq6enter.grid_remove()
def cplus():
    global count
    if count < 6:
        count += 1
        lable3['text'] = f'{count}'
        check_count(count, '+')
def cminus():
    global count
    if count > 2:
        count -= 1
        lable3['text'] = f'{count}'
        check_count(count, '-')
def delete():  # полная очистка всех панелей
    for i in range(1, 7):
        eval(f'eq{i}enter.delete(0, tkinter.END)')
        for j in range(1, 7):
            eval(f'x{i}enter{j}.delete(0, tkinter.END)')
    remover()
def number_maker(number):
    def digits(stroka):
        for letter in stroka:
            if letter not in '1234567890-.,':
                return False
        return True
    global norm_digit
    if not norm_digit.search(number) is None and digits(number):
        entered_number = norm_digit.search(number).group().replace(',', '.')
        try:
            entered_number = int(entered_number)
        except ValueError:
            entered_number = float(entered_number)
        return entered_number
def solver():
    global mat_solve
    remover()
    big_a = list()
    big_b = list()
    for i in range(1, 7):
        stroka_list = []
        big_b.append([number_maker(eval(f'eq{i}enter.get()'))])
        for j in range(1, 7):
            stroka_list.append(number_maker(eval(f'x{j}enter{i}.get()')))
        if len(stroka_list) != 0:
            big_a.append(stroka_list)
    big_a = list(filter(lambda x: any([True for elem in x if not elem is None]), big_a))
    big_b = list(filter(lambda x: any([True for elem in x if not elem is None]), big_b))
    for i in range(len(big_a)):
        big_a[i] = list(filter(lambda x: True if not x is None else False, big_a[i]))
    q = len(big_a) == len(big_b) and len(big_a) != 0 and len(big_b) != 0
    for i in range(len(big_a)):
        if len(big_a[i]) != len(big_a):
            q = False
            break
    if not q:
        remover()
        entererror['text'] = 'Ошибка ввода'
        entererror.place(x=80, y=290)
    else:
        entererror.grid_remove()
        big_b = numpy.array(big_b)
        big_a = numpy.array(big_a)
        try:
            big_a_det = int(fractions.Fraction(numpy.linalg.det(big_a)).limit_denominator(1))
            if big_a_det != 0:
                try:
                    mat_solve = numpy.linalg.solve(big_a, big_b)
                except:
                    big_a_det = 'Error'
        except:
            big_a_det = 'Error'
        if big_a_det == 0:
            matrix_a['text'] = 'Вырожденная матрица (определитель равен нулю)'
            matrix_a.place(x=80, y=290)
        elif big_a_det == 'Error':
            matrix_a['text'] = 'Ошибка ввода'
            matrix_a.place(x=80, y=290)  # панель ошибки ввода
        else:
            big_a = numpy.linalg.inv(big_a)
            big_a_text, big_b_text, mat_solve_text = '', '', ''
            for i in range(len(big_a)):  # печать обратной матрицы
                if i == 0:
                    big_a_text += '/  '.ljust(8)
                elif i == len(big_a)-1:
                    big_a_text += '\\  '.ljust(8)
                else:
                    big_a_text += '|  '.ljust(8)
                for j in range(len(big_a)):
                    big_a_text += str(fractions.Fraction(big_a[i][j]).limit_denominator(100)).center(7)+'  '
                if i == 0:
                    big_a_text += '  \\\n'.rjust(8)
                elif i == len(big_a) - 1:
                    big_a_text += '  /\n'.rjust(8)
                else:
                    big_a_text += '  |\n'.rjust(8)
            matrix_a['text'] = big_a_text
            matrix_a.place(x=80, y=290)  # панель матрицы а
            for i in range(len(big_b)):  # печать матрицы свободных членов
                if i == 0:
                    big_b_text += '/'.ljust(8) + str(-big_b[i][0]).center(5) + '\\\n'.rjust(8)
                elif i == len(big_b)-1:
                    big_b_text += '\\'.ljust(8) + str(-big_b[i][0]).center(5) + '/\n'.rjust(8)
                else:
                    big_b_text += '| '.ljust(8) + str(-big_b[i][0]).center(5) + ' |\n'.rjust(8)
            matrix_b['text'] = big_b_text
            lable_multiply['text'] = '*'
            lable_multiply.place(x=500, y=310)
            matrix_b.place(x=530, y=290)  # панель матрицы свободных членов
            for i in range(len(mat_solve)):  # печать матрицы ответа
                if i == 0:
                    mat_solve_text += '/'.ljust(8) + str(-fractions.Fraction(mat_solve[i][0]).limit_denominator(100)).center(5) + '\\\n'.rjust(8)
                elif i == len(big_b)-1:
                    mat_solve_text += ' \\'.ljust(8) + str(-fractions.Fraction(mat_solve[i][0]).limit_denominator(100)).center(5) + '/\n'.rjust(8)
                else:
                    mat_solve_text += '| '.ljust(8) + str(-fractions.Fraction(mat_solve[i][0]).limit_denominator(100)).center(5) + ' |\n'.rjust(8)
            matrix_result['text'] = mat_solve_text
            lable_equall['text'] = '='
            lable_equall.place(x=620, y=310)
            matrix_result.place(x=650, y=290)  # панель матрицы результата

win = tkinter.Tk()
logo = tkinter.PhotoImage(file='math.png')
win.iconphoto(False, logo)
win.config(bg='#ADEDE0')
win.title('Решение СЛАУ методом обратной матрицы')
win.geometry("800x550+150+150")
win.resizable(False, False)

lable1 = tkinter.Label(win, text='Количество неизвестных:', background='#ADEDE0', font=('Times New Roman', 12))
lable1.grid(row=0, column=0, stick='w', columnspan=4)
lable2 = tkinter.Label(win, text='Коэффициенты при неизвестных:', background='#ADEDE0', font=('Times New Roman', 12))
lable3 = tkinter.Label(win, text=f'{count}', background='#ADEDE0', font=('Times New Roman', 12))
lable2.grid(row=1, column=0, stick='w', columnspan=13)
lable3.place(x=180, y=0)
button_plus = tkinter.Button(win, text='+', background='#ADEDE0', font=('Times New Roman', 12), activebackground='#ADEDE0', command=cplus, width=3)
button_minus = tkinter.Button(win, text='-', background='#ADEDE0', font=('Times New Roman', 12), activebackground='#ADEDE0', command=cminus, width=3)
button_plus.place(x=210, y=0)
button_minus.place(x=248, y=0)
solve = tkinter.Button(win, text='Решить', background='#ADEDE0', font=('Times New Roman', 12), activebackground='#ADEDE0', command=solver)
solve.grid(row=8, column=0)
answer = tkinter.Label(win, text='Ответ:', background='#ADEDE0', font=('Times New Roman', 12)).grid(row=9, column=0)
deleter = tkinter.Button(win, text='Очистить', background='#ADEDE0', font=('Times New Roman', 12), activebackground='#ADEDE0', command=delete)
deleter.place(x=288, y=0)
entererror = tkinter.Label(win, text='Ошибка ввода', background='#ADEDE0', font=('Times New Roman', 12))
matrix_a = tkinter.Label(win, background='#ADEDE0', font=('Times New Roman', 12))
matrix_b = tkinter.Label(win, background='#ADEDE0', font=('Times New Roman', 12))
matrix_result = tkinter.Label(win, background='#ADEDE0', font=('Times New Roman', 12))

# 2 неизвестные
x1enter1 = tkinter.Entry(win, width=3, background='#ADEDE0')
x1enter1.grid(row=2, column=0, ipadx=5, ipady=5, stick='e')
x1enter2 = tkinter.Entry(win, width=3, background='#ADEDE0')
x1enter2.grid(row=3, column=0, ipadx=5, ipady=5, stick='e')
x2enter1 = tkinter.Entry(win, width=3, background='#ADEDE0')
x2enter1.grid(row=2, column=2, ipadx=5, ipady=5, stick='w')
x2enter2 = tkinter.Entry(win, width=3, background='#ADEDE0')
x2enter2.grid(row=3, column=2, ipadx=5, ipady=5, stick='w')
x10 = tkinter.Label(win, width=3, text='x1 +', background='#ADEDE0', font=('Times New Roman', 12)).grid(row=2, column=1,stick='w')
x11 = tkinter.Label(win, width=3, text='x1 +', background='#ADEDE0', font=('Times New Roman', 12)).grid(row=3, column=1,stick='w')
x20 = tkinter.Label(win, width=3, text='x2 +', background='#ADEDE0', font=('Times New Roman', 12)).grid(row=2, column=3,stick='w')
x21 = tkinter.Label(win, width=3, text='x2 +', background='#ADEDE0', font=('Times New Roman', 12)).grid(row=3, column=3,stick='w')
eq1 = tkinter.Label(win, width=3, text='= 0', background='#ADEDE0', font=('Times New Roman', 12)).grid(row=2, column=13,stick='w')
eq2 = tkinter.Label(win, width=3, text='= 0', background='#ADEDE0', font=('Times New Roman', 12)).grid(row=3, column=13,stick='w')
eq1enter = tkinter.Entry(win, width=3, background='#ADEDE0')
eq1enter.grid(row=2, column=12, ipadx=5, ipady=5, stick='w')
eq2enter = tkinter.Entry(win, width=3, background='#ADEDE0')
eq2enter.grid(row=3, column=12, ipadx=5, ipady=5, stick='w')

# 3 неизвестные
x1enter3 = tkinter.Entry(win, width=3, background='#ADEDE0')
x2enter3 = tkinter.Entry(win, width=3, background='#ADEDE0')
x3enter1 = tkinter.Entry(win, width=3, background='#ADEDE0')
x3enter2 = tkinter.Entry(win, width=3, background='#ADEDE0')
x3enter3 = tkinter.Entry(win, width=3, background='#ADEDE0')
x13 = tkinter.Label(win, width=3, text='x1 +', background='#ADEDE0', font=('Times New Roman', 12))
x23 = tkinter.Label(win, width=3, text='x2 +', background='#ADEDE0', font=('Times New Roman', 12))
x31 = tkinter.Label(win, width=3, text='x3 +', background='#ADEDE0', font=('Times New Roman', 12))
x32 = tkinter.Label(win, width=3, text='x3 +', background='#ADEDE0', font=('Times New Roman', 12))
x33 = tkinter.Label(win, width=3, text='x3 +', background='#ADEDE0', font=('Times New Roman', 12))
eq3 = tkinter.Label(win, width=3, text='= 0', background='#ADEDE0', font=('Times New Roman', 12))
eq3enter = tkinter.Entry(win, width=3, background='#ADEDE0')

#4 неизвестные
x1enter4 = tkinter.Entry(win, width=3, background='#ADEDE0')
x2enter4 = tkinter.Entry(win, width=3, background='#ADEDE0')
x3enter4 = tkinter.Entry(win, width=3, background='#ADEDE0')
x4enter1 = tkinter.Entry(win, width=3, background='#ADEDE0')
x4enter2 = tkinter.Entry(win, width=3, background='#ADEDE0')
x4enter3 = tkinter.Entry(win, width=3, background='#ADEDE0')
x4enter4 = tkinter.Entry(win, width=3, background='#ADEDE0')
x14 = tkinter.Label(win, width=3, text='x1 +', background='#ADEDE0', font=('Times New Roman', 12))
x24 = tkinter.Label(win, width=3, text='x2 +', background='#ADEDE0', font=('Times New Roman', 12))
x34 = tkinter.Label(win, width=3, text='x3 +', background='#ADEDE0', font=('Times New Roman', 12))
x41 = tkinter.Label(win, width=3, text='x4 +', background='#ADEDE0', font=('Times New Roman', 12))
x42 = tkinter.Label(win, width=3, text='x4 +', background='#ADEDE0', font=('Times New Roman', 12))
x43 = tkinter.Label(win, width=3, text='x4 +', background='#ADEDE0', font=('Times New Roman', 12))
x44 = tkinter.Label(win, width=3, text='x4 +', background='#ADEDE0', font=('Times New Roman', 12))
eq4 = tkinter.Label(win, width=3, text='= 0', background='#ADEDE0', font=('Times New Roman', 12))
eq4enter = tkinter.Entry(win, width=3, background='#ADEDE0')

# 5 неизвестных
x1enter5 = tkinter.Entry(win, width=3, background='#ADEDE0')
x2enter5 = tkinter.Entry(win, width=3, background='#ADEDE0')
x3enter5 = tkinter.Entry(win, width=3, background='#ADEDE0')
x4enter5 = tkinter.Entry(win, width=3, background='#ADEDE0')
x5enter1 = tkinter.Entry(win, width=3, background='#ADEDE0')
x5enter2 = tkinter.Entry(win, width=3, background='#ADEDE0')
x5enter3 = tkinter.Entry(win, width=3, background='#ADEDE0')
x5enter4 = tkinter.Entry(win, width=3, background='#ADEDE0')
x5enter5 = tkinter.Entry(win, width=3, background='#ADEDE0')
x15 = tkinter.Label(win, width=3, text='x1 +', background='#ADEDE0', font=('Times New Roman', 12))
x25 = tkinter.Label(win, width=3, text='x2 +', background='#ADEDE0', font=('Times New Roman', 12))
x35 = tkinter.Label(win, width=3, text='x3 +', background='#ADEDE0', font=('Times New Roman', 12))
x45 = tkinter.Label(win, width=3, text='x4 +', background='#ADEDE0', font=('Times New Roman', 12))
x51 = tkinter.Label(win, width=3, text='x5 +', background='#ADEDE0', font=('Times New Roman', 12))
x52 = tkinter.Label(win, width=3, text='x5 +', background='#ADEDE0', font=('Times New Roman', 12))
x53 = tkinter.Label(win, width=3, text='x5 +', background='#ADEDE0', font=('Times New Roman', 12))
x54 = tkinter.Label(win, width=3, text='x5 +', background='#ADEDE0', font=('Times New Roman', 12))
x55 = tkinter.Label(win, width=3, text='x5 +', background='#ADEDE0', font=('Times New Roman', 12))
eq5 = tkinter.Label(win, width=3, text='= 0', background='#ADEDE0', font=('Times New Roman', 12))
eq5enter = tkinter.Entry(win, width=3, background='#ADEDE0')

# 6 неизвестных
x1enter6 = tkinter.Entry(win, width=3, background='#ADEDE0')
x2enter6 = tkinter.Entry(win, width=3, background='#ADEDE0')
x3enter6 = tkinter.Entry(win, width=3, background='#ADEDE0')
x4enter6 = tkinter.Entry(win, width=3, background='#ADEDE0')
x5enter6 = tkinter.Entry(win, width=3, background='#ADEDE0')
x6enter1 = tkinter.Entry(win, width=3, background='#ADEDE0')
x6enter2 = tkinter.Entry(win, width=3, background='#ADEDE0')
x6enter3 = tkinter.Entry(win, width=3, background='#ADEDE0')
x6enter4 = tkinter.Entry(win, width=3, background='#ADEDE0')
x6enter5 = tkinter.Entry(win, width=3, background='#ADEDE0')
x6enter6 = tkinter.Entry(win, width=3, background='#ADEDE0')
x16 = tkinter.Label(win, width=3, text='x1 +', background='#ADEDE0', font=('Times New Roman', 12))
x26 = tkinter.Label(win, width=3, text='x2 +', background='#ADEDE0', font=('Times New Roman', 12))
x36 = tkinter.Label(win, width=3, text='x3 +', background='#ADEDE0', font=('Times New Roman', 12))
x46 = tkinter.Label(win, width=3, text='x4 +', background='#ADEDE0', font=('Times New Roman', 12))
x56 = tkinter.Label(win, width=3, text='x5 +', background='#ADEDE0', font=('Times New Roman', 12))
x61 = tkinter.Label(win, width=3, text='x6 +', background='#ADEDE0', font=('Times New Roman', 12))
x62 = tkinter.Label(win, width=3, text='x6 +', background='#ADEDE0', font=('Times New Roman', 12))
x63 = tkinter.Label(win, width=3, text='x6 +', background='#ADEDE0', font=('Times New Roman', 12))
x64 = tkinter.Label(win, width=3, text='x6 +', background='#ADEDE0', font=('Times New Roman', 12))
x65 = tkinter.Label(win, width=3, text='x6 +', background='#ADEDE0', font=('Times New Roman', 12))
x66 = tkinter.Label(win, width=3, text='x6 +', background='#ADEDE0', font=('Times New Roman', 12))
e6 = tkinter.Label(win, width=3, text='= 0', background='#ADEDE0', font=('Times New Roman', 12))
eq6enter = tkinter.Entry(win, width=3, background='#ADEDE0')

lable_multiply = tkinter.Label(win, width=3, text='*', background='#ADEDE0', font=('Times New Roman', 12))
lable_equall = tkinter.Label(win, width=3, text='=', background='#ADEDE0', font=('Times New Roman', 12))
win.mainloop()
