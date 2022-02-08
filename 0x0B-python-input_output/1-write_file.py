#!/usr/bin/python3
# 1-number_of_lines.py
def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(text)
    return len(text)
