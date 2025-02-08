import json
import sys


class Data:


    def __init__(self, values_path, tests_path, report_path):
        if self.__check_path(values_path, tests_path, report_path):
            self._values_path = values_path
            self._tests_path = tests_path
            self._report_path = report_path


    def __check_path(self, path_1, path_2, path_3):
        try:
            if not all(isinstance(obj, str) for obj in (path_1, path_2, path_3)):
                raise TypeError("Не правильно введены пути к файлам")
        except TypeError as e:
            print(e)
            return False
        return True

    def __load_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)


    def __save_json(self,data,  file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)


    def __fill_values(self, tests, values):
        if isinstance(tests, list):
            for test in tests:
                self.__fill_values(test, values)
        elif isinstance(tests, dict):
            if 'id' in tests and tests['id'] in values:
                tests['value'] = values[tests['id']]
            if 'values' in tests:
                self.__fill_values(tests['values'], values)


    def init(self):
        values_data = self.__load_json(self._values_path)
        tests_data = self.__load_json(self._tests_path)
        values_dict = {item['id']: item['value'] for item in values_data['values']}
        self.__fill_values(tests_data['tests'], values_dict)
        self.__save_json(tests_data, self._report_path)


def main():
    if len(sys.argv) != 4:
        print("Использование: python task3.py values.json tests.json report.json")
        return
    else:
        data = Data(sys.argv[1], sys.argv[2], sys.argv[3])
        data.init()


if __name__ == "__main__":
    main()
