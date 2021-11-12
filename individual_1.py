#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задание 1
# 3. Дано слово S1. Получить слово S2, образованное нечетными буквами слова S1.

if __name__ == '__main__':

    s1 = input('Enter the word: ')
    s2 = s1[1::2]

    print(s2)
