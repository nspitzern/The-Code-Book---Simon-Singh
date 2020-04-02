import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

alphabet_letters = 'abcdefghijklmnopqrstuvwxyz'
english_distribution = [8.167, 1.492, 2.202, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 1.292, 4.025, .406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.356, 2.758, 0.978, 2.560 ,0.150, 1.994, 0.077]


def shift_letters(letters, shift=0):
    new_letters = letters[shift:]
    new_letters.extend(letters[0:shift])

    return new_letters


def _shift_letters_and_count(letters, count_list, shift):
    new_letters = letters[shift:]
    new_letters.extend(letters[0:shift])

    new_count_list = count_list[shift:]
    new_count_list.extend(count_list[0:shift])

    return new_letters, new_count_list


def calculate_text_distribution(text, letters, shift=0):
    # count the occurrences of each letter in the text
    count = Counter(text)

    count_list = []

    # manage all counts in a list in the order of the letters appearances
    for c in letters:
        if c in count.keys():
            count_list.append(count[c])
        else:
            count_list.append(0)

    # if we want to shift the bars of the chart
    if shift != 0:
        letters, count_list = _shift_letters_and_count(letters, count_list, shift)

    # normalize the counting to percentages
    for i in range(len(count_list)):
        count_list[i] = count_list[i] / len(text) * 100

    return count_list, letters


def show_letters_distribute(alphabet, text, shift=0, needs_upper=True):
    # convert regular alphabet to cipher alphabet (upper case)
    if needs_upper is True:
        alphabet = alphabet.upper()

    # split to letters
    letters = list(alphabet)

    y_pos = np.arange(len(letters))

    count_list, cipher_letters = calculate_text_distribution(text, letters, shift)

    plt.figure(figsize=(10, 7))

    plt.subplot(2, 1, 1)

    # create and plot the chart for the cipher text distribution
    plt.bar(y_pos, count_list, align='center', alpha=1)

    plt.xticks(y_pos, cipher_letters)
    plt.ylabel('Count %')
    plt.title('Cipher Letters Distribution')

    # create and plot the chart for the an english text distribution
    plt.subplot(2, 1, 2)

    plt.bar(y_pos, english_distribution, align='center', alpha=1)

    plt.xticks(y_pos, letters)
    plt.ylabel('Count %')
    plt.title('English Letters Distribution')

    plt.show()
