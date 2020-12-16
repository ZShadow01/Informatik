"""
BWInf - 39. Wettbewerb [Wichteln]
"""
from random import randint

FILE_NAME = "wichteln.txt"
RESULT_FILE = "wichteln_ergebnis.txt"
DATA = {}


# Datei öffnen und in "lines" speichern
lines = []
with open(FILE_NAME, "r") as f:
    for line in f.readlines():
        lines.append(line.replace("\n", "").strip())


# Anzahl der Schüler / innen
amount_of_students = int(lines.pop(0))

# Vorhandene Wichtelgeschenke / Gegenstände
presents = list(range(1, amount_of_students + 1))


for line in lines:
    # Wünsche einteilen
    wishes = line.split(" ")

    # Entferne leere Strings wie ""
    wishes = list(filter(None, wishes))

    # Alle bisherigen Informationen von Schüler / in in "DATA" speichern
    DATA[str(len(DATA) + 1)] = {
        "WISHES": wishes,
        "RECEIVED": ""
    }


# Methode / Funktion um Schüler / innen ihre Geschenke zu geben
def give(student_, ranked_wish):
    # Zufälliges Geschenk
    if ranked_wish == "random":
        present = randint(0, len(presents) - 1)
    else:
        present = presents.index(int(DATA[student_]["WISHES"][ranked_wish]))

    # Schenken
    DATA[student_]["RECEIVED"] = str(presents.pop(present))


# Für alle Schüler / innen...
for student in range(1, amount_of_students + 1):
    student_data = DATA[str(student)]
    student_wishes = student_data["WISHES"]


    # Falls das 1. gewünschte Gegenstand noch verfügbar ist...
    if int(student_wishes[0]) in presents:

        # Schenken
        give(str(student), 0)


    # Sonst, falls das 2. gewünschte Gegenstand noch verfügbar ist...
    elif int(student_wishes[1]) in presents:

        # Schenken
        give(str(student), 1)


    # Sonst, falls das 3. gewünschte Gegenstand noch verfügbar ist...
    elif int(student_wishes[2]) in presents:

        # Schenken
        give(str(student), 2)


    # Sonst, ein zufälliges Gegenstand schenken
    else:
        give(str(student), "random")


# In einer .txt Datei speichern
with open(RESULT_FILE, "w+") as f:
    for _student in DATA:
        f.write("Student " + _student + " kriegt Geschenk Nr. " + str(DATA[_student]["RECEIVED"]))
        f.write(" || Wunschliste: " + str(DATA[_student]["WISHES"]) + "\n\n")
