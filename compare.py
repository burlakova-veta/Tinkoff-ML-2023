import sys
from lev import lev


def metric(str1, str2):
    return (len(str1) - lev(str1, str2)) / len(str1)
    # делим редакционное расстояние на длину текста


if __name__ == '__main__':
    read, write = sys.argv[1:]
    file_r = open(read, 'r', encoding='utf8')
    file = file_r.read().split()
    i = 0
    size = ''
    for i in range(0, len(file), 2):
        string1 = ''.join(file[i])
        string2 = ''.join(file[i])
        size += str(metric(string1, string2)) + '\n'
    file_w = open(write, 'w')
    file_w.write(size)
    file_w.close()