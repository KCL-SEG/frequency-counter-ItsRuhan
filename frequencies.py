"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):

    frequencies = {}

    for item in items:
        item = str(item)

        if item not in frequencies:
            frequencies[item] = 0

        frequencies[item] += 1

    return frequencies