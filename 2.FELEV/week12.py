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

create_file()