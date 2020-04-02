
"""
A MonoAlphaBet encryptor
The encryptor reads a plain text from a file with a key and a shift of the key.
The encryption alphabet is the unique letters of the key concatenate with the rest of the alphabet letters.
The shift determines how many places to move the start of the encrytion alphabet.
For example - the key is SEEDS which will convert to SED (removing all non unique letters),
therefore the encryption letters will be SEDABCFGHIJKLMNOPQRTUVWXYZ.
With a shift of 3 for example we will get - XYZSEDABCFGHIJKLMNOPQRTUVW which is a cyclic shift of 3.
"""

from Encryptor import Encryptor


class MonoAlphaBetEncryptor(Encryptor):
    def __init__(self):
        super(MonoAlphaBetEncryptor, self).__init__()

    def _get_unique_letters_string(self, str):
        unique_chars = []
        new_str = ''
        for c in str:
            if c not in unique_chars:
                new_str += c
                unique_chars.append(c)
        return new_str

    """
        Parse the input file
    """
    def _parse_input_file(self, file_path):
        lines, key = super()._parse_input_file(file_path)
        key, shift = key.split(',')
        shift = int(shift.strip())
        self._key = super().get_unique_letters_key(key)
        return lines, shift

    def _fill_dicts(self, shift, new_letters):
        # get the size of the alphabet
        ab_size = len(self._letters)

        # init enc letters as letters
        self._enc_letters = '%s' % self._letters

        # replace enc_letters such that it is the key + the rest of alphabet with a shift
        for i, c in enumerate(self._letters):
            idx = (i + shift) % ab_size
            self._enc_letters = self._enc_letters.replace(self._letters[idx], new_letters[i])

        # print(self._enc_letters)

        # fill the dicts
        for i, c in enumerate(self._letters):
            # convention - plain text in lower case and cipher in upper case
            # insert the letters into the encrypt dict and decrypt dict
            c = str.lower(c)
            self._encrypt_dict[c] = self._enc_letters[i]
            self._decrypt_dict[self._enc_letters[i]] = c

    def _init_dicts(self, shift):
        enc_letters = ('%s' % self._letters).upper()
        # remove all letters of the key
        for c in self._key:
            enc_letters = enc_letters.replace(c, '')

        new_letters = '%s' % self._key
        new_letters += enc_letters

        self._fill_dicts(shift, new_letters)

    def encrypt(self, file_path):
        lines, shift = self._parse_input_file(file_path)
        self._init_dicts(shift)

        cipher = ''

        for line in lines:
            for c in line:
                c = c.lower()
                # skip letters not in the alphabet
                if c not in self._encrypt_dict.keys():
                    cipher += c
                    continue

                cipher += self._encrypt_dict[c]

        print(cipher)
        return cipher

    def decrypt(self, str):
        plain_text = ''

        for c in str:

            # skip letters not in the alphabet
            if c not in self._decrypt_dict.keys():
                plain_text += c
                continue

            plain_text += self._decrypt_dict[c]

        print(plain_text)
        return plain_text


encryptor = MonoAlphaBetEncryptor()
c = encryptor.encrypt("input_text")
print('\n')
p = encryptor.decrypt(c)


from utils import show_letters_distribute

show_letters_distribute('abcdefghijklmnopqrstuvwxyz', c)
