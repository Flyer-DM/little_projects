from Vernam import Vernam


def main():
    print("""Что вы хотите сделать:
1. Зашифровать сообщение по Цезарю.
2. Дешифровать сообщение по Цезарю.
3. Взломать зашифрованное сообщение по Цезарю.
4. Выйти.""")
    while True:
        act = input("Введите номер действия: ")
        if act == '4':
            break
        elif act == '1':
            message = input("Введите ваше сообщение: ")
            language = input("Введите язык сообщения (eng - e/рус - р): ")
            try:
                step = int(input("Введите шаг (целое число): "))
                print("Результат:", Caesar(message).encrypt(step, language), '\n')
            except ValueError:
                print("Ошибка! Шаг может быть только целым числом; доступные языки: русский (р), english (e).")
        elif act == '2':
            message = input("Введите ваше сообщение: ")
            language = input("Введите язык сообщения (eng - e/рус - р): ")
            step = int(input("Введите шаг (целое число): "))
            print("Результат:", Caesar(message).decrypt(step, language), '\n')
        elif act == '3':
            message = input("Введите ваше сообщение: ")
            language = input("Введите язык сообщения (eng - e/рус - р): ")
            print("Результат:")
            Caesar(message).hack(language)
        else:
            print("Неизвестное действие.")


if __name__ == '__main__':
    main()
