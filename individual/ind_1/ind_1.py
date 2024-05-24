#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Считываем текст из файла
    with open("text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Разбиваем текст на слова
    words = text.split()

    # Меняем местами каждые два соседних слова
    for i in range(0, len(words) - 1, 2):
        words[i], words[i + 1] = words[i + 1], words[i]

    # Выводим измененный текст на экран
    modified_text = ' '.join(words)
    print(modified_text)
