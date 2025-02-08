import sys

class OneNumberElements:

    def __init__(self, file_path):
        if self.__check_path(file_path):
            self._file_path = file_path
            self._numbers = None


    def __check_path(self, path):
        try:
            if type(path) != str:
                raise TypeError("Не правильно введены пути к файлам")
        except TypeError as e:
            print(e)
            return False
        return True

    def __read_numbers(self):
        with open(self._file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            self._numbers = numbers

    def to_equal(self):
        self.__read_numbers()
        self._numbers.sort()
        median = self._numbers[len(self._numbers) // 2]
        moves = sum(abs(num - median) for num in self._numbers)
        print(moves)


def main():
    if len(sys.argv) !=2:
        print("Использование: python task4.py numbers.txt")
        return

    file_path = sys.argv[1]

    moves = OneNumberElements(file_path)
    moves.to_equal()

if __name__ == "__main__":
    main()