from Encryptor import Encryptor
from utils import shift_letters
from utils import show_letters_distribute


class VigenereSquare(Encryptor):
    def __init__(self):
        super(VigenereSquare, self).__init__()
        self._init_dicts()

    def _init_dicts(self):
        letters = list(super().get_letters())

        # fill the dictionary as a matrix of n*n letters, each row is one shift forward of the row previous row.
        # the keys are the last letter.
        # for example - in the letter 'A' -> 'B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
        for i, c in enumerate(letters):
            shift = (i + 1) % len(letters)
            shifted_letters = shift_letters(letters, shift)

            # convert to upper case characters as convention of cipher text
            for j, k in enumerate(shifted_letters):
                shifted_letters[j] = str(k).upper()

            self._encrypt_dict[shifted_letters[0]] = shifted_letters

    def encrypt(self, file_path):
        plain_text, self._key = super()._parse_input_file(file_path)
        self._key = self._key.strip()

        # The index of the key letter that is currently using in the encryption
        i = 0

        cipher = ''

        for line in plain_text:
            for c in line:
                c = c.lower()

                # the letter of the key in the current index
                key_letter_by_index = self._key[i]

                # skip letters not in the alphabet
                if c.upper() not in self._encrypt_dict[key_letter_by_index]:
                    cipher += c
                    continue

                # get the index of the plain letter in the plain alphabet
                letter_index_in_alphabet = str.index(super().get_letters(), c)

                # get the shifted cipher alphabet according to the key-letter, now choose the cipher letter according
                # to the index of the plain letter
                cipher += self._encrypt_dict[key_letter_by_index][letter_index_in_alphabet]

                # We want to cycle on the key word as long as the plain text
                i = (i + 1) % len(self._key)

        print(cipher)
        return cipher

    def decrypt(self, text):
        # The index of the key letter that is currently using in the encryption
        i = 0

        plain_text = ''

        for c in text:

            # the letter of the key in the current index
            key_letter_by_index = self._key[i]

            # skip letters not in the alphabet
            if c not in self._encrypt_dict[key_letter_by_index]:
                plain_text += c
                continue

            # get the index of the cipher letter in the cipher alphabet
            letter_index_in_cipher_alphabet = list.index(self._encrypt_dict[key_letter_by_index], c)

            # get the plain letter in the index of the cipher letter from the alphabet letters
            plain_text += self.get_letters()[letter_index_in_cipher_alphabet]

            # We want to cycle on the key word as long as the plain text
            i = (i + 1) % len(self._key)

        print(plain_text)
        return plain_text


encryptor = VigenereSquare()
c = encryptor.encrypt('vigenere_input')
p = encryptor.decrypt(c)

show_letters_distribute('abcdefghijklmnopqrstuvwxyz', c)