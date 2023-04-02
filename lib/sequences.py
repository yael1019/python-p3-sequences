#!/usr/bin/env python3

def print_fibonacci(length):
    list = []
    if length > 0:
        list.append(0)
        if length > 1:
            list.append(1)
            if length > 2:
                for i in range(2, length):
                    list.append(
                        list[i - 1] + list[i - 2]
                    )
    print(list)