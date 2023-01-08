def update(number_char, size=None, array=None):
    arr = []
    if array is None:
        for i in range(size+1):
            arr.append(i)
    else:
        arr.append(array)
        size = len(array)
    s = [0] * size
    arr.append(s)
    arr[1][0] += number_char
    return arr, number_char + 1


def lev(word1, word2):
    k = 1
    arr, k = update(number_char=k, size=len(word2))
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] != word2[j]:
                arr[1][j + 1] = min([arr[0][j + 1] + 1, arr[1][j] + 1, arr[0][j] + 1])
            else:
                arr[1][j + 1] = min([arr[0][j + 1] + 1, arr[1][j] + 1, arr[0][j]])
        arr, k = update(number_char=k, array=arr[1])
    return arr[0][-1]


def large(func):
    def shell(word1, word2):
        size1, size2 = len(word1), len(word2)
        if size1 == 0 or size2 == 0:
            if size1 >= size2:
                return size1
            else:
                return size2
        else:
            if size1 >= size2:
                return func(word1, word2)
            else:
                return func(word2, word1)
    return shell


if __name__ == '__main__':
    print(lev('проверка расстояния', 'проверка системы'))
