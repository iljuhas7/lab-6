#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задание повышенной сложности
# 3. Дано слово. Определить, сколько различных букв в нем.

if __name__ == '__main__':

    s = input("Введите слово:")
    k = 0

    for i in range(1, len(s)):
        n = 0

        for j in range(1, len(s) - 1):
            if s[i] == s[j+1]:
                n += 1

        if n == 0:
            k += 1

    print(f"количество различных символов = {k}")
