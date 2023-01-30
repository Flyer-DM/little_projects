class Caesar:
    LITTLE_ENG = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    BIG_ENG = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    LITTLE_RUS = [chr(i) for i in range(ord('а'), ord('я') + 1) if chr(i) != 'ё']
    BIG_RUS = [chr(i) for i in range(ord('А'), ord('Я') + 1) if chr(i) != 'Ё']

    def __init__(self, message: str):
        self.__message = message

    def __str__(self):
        return self.__message

    @staticmethod
    def __crypt(step: int, lang: str):
        step = step % 26 if lang == 'e' else step % 32 if lang == 'р' else None
        if step is None:
            raise ValueError("Неизвестный язык, попробуйте английский (e) или русский (р).")
        return step

    @classmethod
    def __create_string(cls, string: str, step: int, lang: str):
        result = []
        if lang == 'e':
            for symbol in string:
                if symbol in cls.LITTLE_ENG:
                    result.append(cls.LITTLE_ENG[(cls.LITTLE_ENG.index(symbol) + step) % 26])
                elif symbol in cls.BIG_ENG:
                    result.append(cls.BIG_ENG[(cls.BIG_ENG.index(symbol) + step) % 26])
                else:
                    result.append(symbol)
        elif lang == 'р':
            for symbol in string:
                if symbol in cls.LITTLE_RUS:
                    result.append(cls.LITTLE_RUS[(cls.LITTLE_RUS.index(symbol) + step) % 32])
                elif symbol in cls.BIG_RUS:
                    result.append(cls.BIG_RUS[(cls.BIG_RUS.index(symbol) + step) % 32])
                else:
                    result.append(symbol)
        return Caesar(''.join(result))

    def encrypt(self, step: int, lang: str):
        """"Функция шифрования сообщения"""
        return Caesar.__create_string(self.__message, Caesar.__crypt(step, lang), lang)

    def decrypt(self, step: int, lang: str):
        """"Функция дешифрования сообщения со знанием ключа"""
        if lang == 'e':
            return Caesar.__create_string(self.__message, 26 - Caesar.__crypt(step, lang), lang)
        elif lang == 'р':
            return Caesar.__create_string(self.__message, 32 - Caesar.__crypt(step, lang), lang)

    def hack(self, lang: str):
        """Функция подбора ключа для зашифрованного сообщения"""
        if lang == 'e':
            print("Варианты расшифровки сообщения: ")
            for i in range(1, 26 + 1):
                print(Caesar.__create_string(self.__message, i, 'e'))
        elif lang == 'р':
            print("Варианты расшифровки сообщения: ")
            for i in range(1, 32 + 1):
                print(Caesar.__create_string(self.__message, i, 'р'))
        else:
            print("Неизвестный язык, попробуйте английский (e) или русский (р).")
