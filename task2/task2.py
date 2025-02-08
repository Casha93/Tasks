import sys

class Circle:

    def __init__(self, path_1, path_2):
        if self.__check_path(path_1, path_2):
            self._path_1 = path_1
            self._path_2 = path_2
            self._x0 = None
            self._y0 = None
            self._radius = None
            self._points = None

    def __check_path(self, path_1, path_2):
        try:
            if not all(isinstance(obj, str) for obj in (path_1, path_2)):
                raise TypeError("Не правильно введены пути к файлам")
        except TypeError as e:
            print(e)
            return False
        return True


    def __read_circle(self):
        with open(self._path_1, 'r') as file:
            x, y = map(float, file.readline().split())
            radius = float(file.readline())
            self._x0 = x
            self._y0 = y
            self._radius = radius


    def __read_points(self):
        with open(self._path_2, 'r') as file:
            points = [tuple(map(float, line.split())) for line in file]
            self._points = points


    def __point_position(self, point):
        x, y = point
        distance_squared = (x - self._x0) ** 2 + (y - self._y0) ** 2
        radius_squared = self._radius ** 2

        if distance_squared == radius_squared:
            return 0
        elif distance_squared < radius_squared:
            return 1
        else:
            return 2

    def init(self):
        self.__read_circle()
        self.__read_points()

        for point in self._points:
            position = self.__point_position(point)
            print(position)


def main():
    if len(sys.argv) !=3:
        print("Использование: python task2.py circle.txt dot.txt")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    circle = Circle(circle_file, points_file)
    circle.init()

if __name__ == "__main__":
    main()