#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    A = tuple(map(int, input().split()))
    # count 5
    print(f"{A.count(5)} - столько учеников имеют оценку 5")
    