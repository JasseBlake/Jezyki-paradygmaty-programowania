import os
import shutil
import time


def listOfFiles(path):
    return os.listdir(path)


def main():
    os.system('cls')
    while True:

        path = input("Wprowadz ścieżke do folderu: ")
        if os.path.isdir(path):  # sprawdzanie czy path istnieje
            break

        else:
            print("Zla ścieżka")
            time.sleep(1)
            os.system('cls')

    lista = listOfFiles(path)
    slownik = {"nazwa": '', "rozszerzenie": ''}

    print(f'W podanej ścieżce wykryto następujące foldery i pliki: {lista}')

    for el in lista:
        nazwa, rozszerzenie = os.path.splitext(el)
        # print(os.path.splitext(lista[el]))
        # print(f"N: {nazwa} R: {rozszerzenie}")

        if rozszerzenie != '':

            if os.path.isdir(path + "\\" + rozszerzenie) == False:
                # print(os.path.isdir(path+"\\"+rozszerzenie))
                os.mkdir(path + "\\" + rozszerzenie)

            print("Przenosze plik: " + nazwa + rozszerzenie + " Do folderu " + path + "\\" + rozszerzenie)
            shutil.copy(path + "\\" + nazwa + rozszerzenie, path + "\\" + rozszerzenie)


main()

# E:\Python folder
