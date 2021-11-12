#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задание 2
# Дан текст. Определить количество букв и в первом предложении. Рассмотреть два случая:
#   * известно, что буквы и в этом предложении есть;
#   * букв и в тексте может не быть

if __name__ == '__main__':
    s = input("Enter the word: ")
    n = s.count("и")

    if n > 0:
        print(f"Count letter \"и\": {n}")
    else:
        print(f"Letter \"и\" not detected.")