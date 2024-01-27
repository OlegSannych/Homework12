import os
import shutil

'''Домашнее задание.
Реализовать прототип консольной программы - проводника, для работы с файлами. 
Создать функции создания, удаления, перемещения, копирования(файла, папки) с использованием системы контроля версий git. 
Зарегистрироваться на Github и выгрузить с помощью git программу в созданный репозиторий. Прикрепить ссылку на репозиторий.'''

# Функция для создания файла
def create_file():
    file_neme = input('Введите название и тип файла через точку')
    with open(file_neme, 'w') as file:
        print(f'Файл с названием {file_neme} создан')

# Функция для создания папки
def create_folder():
        path_name = input("Введите адрес и название для новой папки: ")
        try:
            os.mkdir(path_name)
            print(f'Папка с названием {path_name} создана')
        except FileExistsError :
            print("Папка с таким названием уже существует")

# Функция для удаления файла
def remove_file():
    file_neme = input('Введите название и тип файла')
    try:
        os.remove(file_neme)
        print(f'Файл с названием {file_neme} удален')
    except PermissionError:
        print("Отсутствует или введен не верный тип файла")
    except FileNotFoundError:
        print("Файл с таким названием не существует")

# Функция для удаления папки
def remove_folder():
    path_name = input('Введите название папки')
    try:
        os.removedirs(path_name)
        print(f'Папка с названием {path_name} удалена')
    except FileNotFoundError:
        print(f"Папка с  названием {path_name} не существует")
    except OSError:
        print(f"Папка с названием {path_name} не пуста")

# Функция для перемещения файла\папки
def move_file_or_folder():
    old_location = input('Введите текущий путь к файлу\папке: ')
    new_location = input('Введите новый путь к файлу\папке: ')
    try:
        shutil.move(old_location,new_location)
    except FileNotFoundError:
        print('Начальный или конечный адрес не найден')

# Функция для копирования файла/папки
def copy_file_or_folder():
    old_location = input('Введите текущий путь к файлу\папке: ')
    new_location = input('Введите новый путь к файлу\папке: ')
    if os.path.isdir(old_location):
        shutil.copytree(old_location,new_location)
        print("Папка скопирована")
    elif os.path.isfile(old_location):
        shutil.copy2(old_location, new_location)
        print("Файл скопирован")
    else:
        print('Начальный адрес не верен')

# Функция для вызова основного меню
def main():
    while True:
        print('Вас приветствует программа проводник')
        print('"1" Создать файл')
        print('"2" Создать папку')
        print('"3" Удалить файл')
        print('"4" Удалить папку')
        print('"5" Переместить файл\папку')
        print('"6" Скопировать файл\папку')
        print('"0" Выход')
        comand_imput = input('Введите номер команды: ')
        if comand_imput == '1':
            create_file()
        elif comand_imput == '2':
            create_folder()
        elif comand_imput == '3':
            remove_file()
        elif comand_imput == '4':
            remove_folder()
        elif comand_imput == '5':
            move_file_or_folder()
        elif comand_imput == '6':
            copy_file_or_folder()
        elif comand_imput == '0':
            break
        else:
            print('Введена неверная команда')
main()

