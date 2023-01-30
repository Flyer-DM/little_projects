from random import choice
from string import printable


class Vernam:

    def __init__(self, message: str):
        self.__message = message

    def __str__(self):
        return self.__message

    def __repr__(self):
        return "'" + self.__message + "'"

    @staticmethod
    def __crypt(message: str, key: str):
        result = []
        if len(key) == len(message):
            for symbol, key_symbol in zip(message, key):
                result.append(chr(ord(symbol) ^ ord(key_symbol)))
            return Vernam(''.join(result))
        raise ValueError(f"Длина сообщения ({len(message)}) должна совпадать с длиной ключа ({len(key)}).")

    def crypt(self, key: str):
        """"Функция шифрования/дешифрования сообщения"""
        return Vernam.__crypt(self.__message, key)

    def rand_encrypt(self):
        """Функция шифрования сообщения со случайным ключом"""
        key = ''.join([choice(printable) for _ in range(len(self.__message))])
        return Vernam.__crypt(self.__message, key), key






