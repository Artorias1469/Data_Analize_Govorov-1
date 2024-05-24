#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def get_total_file_size(directory):
    total_size = 0

    # Проходимся по всем файлам и поддиректориям в указанной директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Получаем полный путь к файлу
            file_path = os.path.join(root, file)
            # Получаем размер файла и добавляем его к общему размеру
            total_size += os.path.getsize(file_path)

    return total_size

if __name__ == "__main__":
    # Указываем директорию, для которой хотим определить размер файлов
    directory = "D:\The Sims 4"

    # Получаем общий размер всех файлов в указанной директории
    total_size = get_total_file_size(directory)

    # Выводим результат
    print(f"Общий размер всех файлов в директории '{directory}': {total_size} байт.")

