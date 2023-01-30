from Vernam import Vernam


def main():
    print("""Что вы хотите сделать:
1. Зашифровать сообщение по Вернаму с ключом.
2. Зашифровать сообщение по Вернаму со случайным ключом.
3. Дешифровать сообщение по Вернаму.
4. Выйти.""")
    while True:
        act = input("Введите номер действия: ")
        if act == '4':
            break
        elif act in '13':
            message = input("Введите ваше сообщение: ")
            key = input("Введите ваш ключ: ")
            print("Результат:", Vernam(message).crypt(key), '\n')
        elif act == '2':
            message = input("Введите ваше сообщение: ")
            message, key = Vernam(message).rand_encrypt()
            print("Результат:", "Сообщение:", message, "Ключ:", key, '\n')
        else:
            print("Неизвестное действие.")


if __name__ == '__main__':
    main()
