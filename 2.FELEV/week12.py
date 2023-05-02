# 1.feladat: Fájlok megnyitása
def open_file():
    f = open("python_text_file.txt", "r", encoding="utf8")
    print(f.read())
    f.close()

# 2.feladat: Fájlok megnyitása (jobb módon)
def open_file_with():
    with open("python_text_file.txt", "r", encoding="utf8") as f:
        print(f.read())

# 3.feladat: Fájlok létrehozása
def create_file():
    with open("my_new_file.txt", "w", encoding="utf8") as f:
        f.write("Hello világ!")

# 4.feladat: Soronkénti feldolgozás
def file_rows():
    with open("python_text_file.txt", "r", encoding="utf8") as source:
        class_names = []
        for name in source.readlines():
            name = name.replace("\n", "")
            class_names.append(name)

    print(class_names)

# 5.feladat: Feldolgozás tuple-ökké
def class_tuples():
    with open("class_marks.txt", "r", encoding="utf8") as source:
        students = []
        for student in source.readlines():
            student = student.replace("\n", "").split(",")
            student[1] = int(student[1])
            students.append(tuple(student))
        return students

# 6.feladat: Kiírás fájlba
def write_into_file(file_name, text):
    with open(file_name, "w", encoding="utf8") as f:
        f.write(text)

# 7.feladat: Hozzáírás fájlhoz
def append_to_file(file_name, text):
    with open(file_name, "a", encoding="utf8") as f:
        f.write(text)

# 8.feladat: Listák kiírása fájlba
def list_to_file(file_name, list_to_write):
    with open(file_name, "w", encoding="utf8") as f:
        f.writelines(list_to_write)

# 9.feladat: Navigálás fájlban
def append_to_beginning():
    with open("class_marks.txt", "r+", encoding="utf8") as f:
        f.seek(0)
        f.write("Adrienn,5\n")

#10.feladat: Fájl törlése
import os
def delete_file(file_name):
    os.remove(file_name)

    
delete_file("kiscica.txt")