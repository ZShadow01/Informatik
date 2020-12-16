"""
BWInf - 39. Wettbewerb [Wichteln] Objectoriented + pandas
"""
import pandas as pd
from random import randint


class Wichteln:
    def __init__(self):
        self.FILE_NAME = "wichteln.txt"
        self.RESULT_FILE = "wichteln_ergebnis_class.txt"

        self.DATA = {}
        self.presents = []

        self.amount_of_students = 0

    def open_file(self):
        lines = []
        with open(self.FILE_NAME, "r") as f:
            for line in f.readlines():
                lines.append(line.replace("\n", "").strip())

        return lines

    def update_data(self):
        data = self.open_file()

        self.amount_of_students = int(data.pop(0))

        self.presents = list(range(1, len(data) + 1))

        for line in data:
            wishes = line.split(" ")

            wishes = list(filter(None, wishes))

            self.DATA[str(len(self.DATA) + 1)] = {
                "WISHES": wishes,
                "RECEIVED": ""
            }

    def give(self, student_, ranked_wish):
        if ranked_wish == "random":
            present = randint(0, len(self.presents) - 1)
        else:
            present = self.presents.index(int(self.DATA[student_]["WISHES"][ranked_wish]))

        self.DATA[student_]["RECEIVED"] = str(self.presents.pop(present))

    def sort_students(self):
        for student in range(1, len(self.DATA) + 1):
            student_data = self.DATA[str(student)]
            student_wishes = student_data["WISHES"]

            if int(student_wishes[0]) in self.presents:
                self.give(str(student), 0)

            elif int(student_wishes[1]) in self.presents:
                self.give(str(student), 1)

            elif int(student_wishes[2]) in self.presents:
                self.give(str(student), 2)

            else:
                self.give(str(student), "random")

    def save_file(self):
        with open(self.RESULT_FILE, "w+") as f:
            for _student in self.DATA:
                f.write("Student " + _student + " kriegt Geschenk Nr. " + str(self.DATA[_student]["RECEIVED"]))
                f.write(" || Wunschliste: " + str(self.DATA[_student]["WISHES"]) + "\n\n")

    def run(self):
        print("[UPDATING]...")
        self.update_data()
        print("Done...")

        print("\n[SORTING ITEMS]...")
        self.sort_students()
        print("Done...")

        print("\n[SAVING]...")
        self.save_file()
        print("Done...")

    def pandas_version(self):
        pandas_data = {
            "Students": [],
            "Wishes": [],
            "Received": []
        }
        for student in self.DATA:
            pandas_data["Students"].append(student)
            pandas_data["Wishes"].append(self.DATA[student]["WISHES"])
            pandas_data["Received"].append(self.DATA[student]["RECEIVED"])

        dataframe = pd.DataFrame(pandas_data)

        with open("wichteln_ergebnis_pandas.txt", "w+") as f:
            f.write(str(dataframe))


if __name__ == "__main__":
    process = Wichteln()
    process.run()
    process.pandas_version()
