import string
from math import *
import os





def analisis(filename):
    frequency = {}
    document_text = open(filename, 'r',encoding=('ansi'))
    text_string = document_text.read()

    for char in text_string:
        count = frequency.get(char, 0)
        frequency[char] = count + 1

    frequency_list = frequency.keys()
    entrop = 0


    for char in frequency_list:
        task1 = frequency[char] / len(text_string)
        entrop = entrop + task1 * log(task1, 2)

    entrop = entrop * -1
    inform = entrop * len(text_string) / 8
    print("File name:", filename)
    print("File size:", os.stat(filename).st_size, "bytes")
 #   print("Character amount:", len(text_string))
 #   print("Unique Character amount:", len(frequency_list))
#    print("Entropy:", entrop)
    print("Information quantity:", inform, " bytes")
    #entrop = 0
   # for char in frequency_list:
    #    task1 = frequency[char] / len(text_string)
    #    entrop = entrop + task1 * log(task1, 2)
    #    print(char, frequency[char],task1)
    return filename

def main():

    analisis('entropy.rar')
    analisis('entropy.zip')
    analisis('entropy.7z')
    analisis('entropy.tar.gz')
    analisis('entropy.tar.bz2')

    analisis('C++.rar')
    analisis('C++.zip')
    analisis('C++.7z')
    analisis('C++.tar.gz')
    analisis('C++.tar.bz2')

    analisis('the-art-of-computer-hacking-2.rar')
    analisis('the-art-of-computer-hacking-2.zip')
    analisis('the-art-of-computer-hacking-2.7z')
    analisis('the-art-of-computer-hacking-2.tar.gz')
    analisis('the-art-of-computer-hacking-2.tar.bz2')

    analisis('based64_entropy.txt')
    analisis('based64_C++.txt')
    analisis('based64_the-art-of-computer-hacking-2.txt')
    analisis('based64_entropy.tar.bz2')
    analisis('based64_C++.tar.bz2')
    analisis('based64_the-art-of-computer-hacking-2.tar.bz2')

if __name__ == "__main__":
    main()

