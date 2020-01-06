# класс Database, представляет из себя базу данных для хранения истории вычислений
import json


class Database:

    def __init__(self):
        self.list_expressions = []
        self.list_results = []
        # print("Database was initialize")
        pass

    def add_expression(self, expression):
        if len(self.list_expressions) == 10:
            self.list_expressions.pop(0)
        self.list_expressions.append(expression)

    def add_result(self, result):
        if len(self.list_results) == 10:
            self.list_results.pop(0)
        self.list_results.append(result)

    def print(self):
        for i in range(len(self.list_expressions)):
            print(f'Expression: {str(self.list_expressions[i])}')
            print(f'Result:  {str(self.list_results[i])}')

    def save_to_file(self):
        try:
            with open('Database_expressions.json', 'w') as f:
                json.dump(self.list_expressions, f)
            with open('Database_results.json', 'w') as f:
                json.dump(self.list_results, f)
        except Exception as e:
            print(e)

    def load_from_file(self):
        try:
            with open('Database_expressions.json', 'r') as f:
                self.list_expressions = json.load(f)
            with open('Database_results.json', 'r') as f:
                self.list_results = json.load(f)
        except Exception as e:
            print(e)

    def clear(self):
        self.list_expressions = []
        self.list_results = []

