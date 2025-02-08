import sys


class CircularArray:


    def __init__(self, n, m):
        if self.__check_value(n, m):
            self._n = int(n)
            self._m = int(m)
            self._array = list(range(1, self._n + 1))
            self._path = []
            self._index = 0

    def __check_value(self, n, m):
        try:
            if not all(isinstance(obj, str) and obj.isdigit() for obj in (n, m)):
                raise TypeError("Ошибка: n и m должны быть целыми числами")
        except TypeError as e:
            print(e)
            return False
        return True


    def init(self):

        while True:
            self._path.append(self._array[self._index])
            self._index = (self._index + self._m - 1) % self._n

            if self._index == 0:
                break

        return "".join(map(str, self._path))


def main():
    if len(sys.argv) !=3:
        print("Использование: python task1.py <n> <m>")
        return

    circular_array = CircularArray(sys.argv[1], sys.argv[2])
    result = circular_array.init()

    print(result)

if __name__ == "__main__":
    main()