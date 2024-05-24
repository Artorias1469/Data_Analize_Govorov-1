#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Открываем файл и считываем текст
    with open("text.txt", "r", encoding="utf-8") as file:
        all_text = file.read()

        # Разбиваем текст на слова
        words = all_text.split()

        # Находим длину самого длинного слова
        max_length = max(len(word) for word in words)

        # Создаем список самых длинных слов
        longest_words = [word for word in words if len(word) == max_length]

        # Выводим результат
        print("Длина самого длинного слова:", max_length)
        print("Самые длинные слова:", longest_words)
