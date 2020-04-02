from abc import abstractmethod


class Encryptor():
    def __init__(self):
        self._letters = 'abcdefghijklmnopqrstuvwxyz'
        self._enc_letters = ''
        self._key = ''
        self._encrypt_dict = {}
        self._decrypt_dict = {}

    def get_letters(self):
        return self._letters

    @abstractmethod
    def encrypt(self, file_path):
        pass

    @abstractmethod
    def decrypt(self, text):
        pass

    def get_unique_letters_key(self, key):
        key_chars = []
        new_key = ''

        for c in key:
            if c not in key_chars:
                key_chars.append(c)
                new_key += c
        return new_key

    def _parse_input_file(self, file_path):
        with open(file_path, 'r') as f:
            # remove white spaces and convert to upper case
            key = f.readline().replace(" ", "").upper()

            # read the plain text
            lines = f.readlines()
            return lines, key