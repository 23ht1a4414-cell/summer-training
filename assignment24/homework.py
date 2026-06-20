#Problem 1: Student Result Processor (STUPROC)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        return self.marks >= 40
count = 0
try:
    with open("students.txt", "r") as file:
        for line in file:
            try:
                name, marks = line.strip().split(",")
                marks = int(marks)

                student = Student(name, marks)

                if student.is_pass():
                    count += 1

            except ValueError:
                pass

    print(count)

except FileNotFoundError:
    print("File Not Found")

#Problem 2: Word Frequency Analyzer (WORDEX)

class WordAnalyzer:
    def __init__(self):
        self.words = []

    def load_words(self):
        try:
            with open("words.txt", "r") as file:
                for line in file:
                    word = line.strip()

                    if word != "":
                        self.words.append(word)

        except FileNotFoundError:
            print("File Not Found")
            return False

        return True

    def get_frequency(self, word):
        return self.words.count(word)


obj = WordAnalyzer()

if obj.load_words():
    try:
        query = input("Enter word: ")

        if not query.isalpha():
            raise ValueError

        print(obj.get_frequency(query))

    except ValueError:
        print("Invalid Query")

#Problem 3: Employee Directory Search (EMPSEARCH)
class EmployeeDirectory:
    def __init__(self):
        self.employees = []

    def load_data(self):
        try:
            with open("employees.txt", "r") as file:
                for line in file:
                    self.employees.append(line.strip())

            return True

        except FileNotFoundError:
            print("File Not Found")
            return False

    def search_by_letter(self, ch):
        found = False

        for name in self.employees:
            if name.lower().startswith(ch.lower()):
                print(name)
                found = True

        if not found:
            print("No Match")


obj = EmployeeDirectory()

if obj.load_data():
    try:
        ch = input("Enter character: ")

        if len(ch) != 1 or not ch.isalpha():
            raise ValueError

        obj.search_by_letter(ch)

    except ValueError:
        print("Invalid Input")            