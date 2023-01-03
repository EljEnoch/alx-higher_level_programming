#!/usr/bin/python3

"""
Text indentation
prints a text with 2 lines

"""


def text_indentation(text):
    """
    prints a text with lines after each . ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    marks = [".", "?", ":"]

    x = 0
    while x < len(text):
        if text[x] in marks:
            print(text[x] + "\n")
            if x + 1 == len(text):
                break
            x += 1
            while text[x] == ' ':
                x += 1

        else:
            print(text[x], end="")
            x += 1
