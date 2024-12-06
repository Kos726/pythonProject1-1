import os
import time
directory = '.'
print(f'\n', os.getcwd())
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        #filetime = os.stat(file).st_mtime #больше нравится этот метод
        filetime = os.path.getmtime(root)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        #filesize = os.stat(file).st_size #больше нравится этот метод
        filesize = os.path.getsize(root)
        parent_dir = os.pardir
        print(f'Обнаружен файл: {file},'
              f' Путь: {filepath},'
              f' Размер: {filesize} байт,'
              f' Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')
