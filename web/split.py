"""Splitting string back to list"""
from typing import List


def back_to_list(string: str) -> List[str]:
    """Adding to list"""
    fight_list: List[str] = []
    sentence: str = ''
    for letter in string:
        sentence += letter
        if letter == '>':
            sentence.replace("<br>", "")
            fight_list.append(sentence)
            sentence = ''
    return fight_list
