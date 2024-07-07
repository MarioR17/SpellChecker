#!/usr/bin/env python3

def load_dict(file_path):
    with open(file_path, "r") as file_in:
        return [line.strip() for line in file_in]

arr = load_dict("dictionary.txt")

print(len(arr))
