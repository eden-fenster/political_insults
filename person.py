#!/usr/bin/env python3
import logging
import sys
import random

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


# This is an object describing the state of a person.
class Person:

    def __init__(self, gender: str, pronouns: str, age: int, skin_color: int, political_ideology: str):
        self._gender = gender
        self._pronouns = pronouns
        self._age = age
        self._skin_color = skin_color
        self._political_ideology = political_ideology
        if political_ideology != 'Left' and political_ideology != 'Right':
            logging.error(f"{political_ideology} is not a valid ideology")
            sys.exit(1)
        self._insult_list = Insults(political_ideology=political_ideology)

    def triggers_other_side(self, other_reaction: bool) -> bool:
        if other_reaction:
            return True
        return False

    def make_statement(self) -> str:
        return self._insult_list.get_insult()

    def triggered(self) -> bool:
        reactions: Reaction = Reaction()
        reaction: str = reactions.get_reaction()
        print(reaction)
        if reaction == '*shocked pikachu face*':
            return True
        return False



class Insults:
    def __init__(self, political_ideology: str):
        if political_ideology != 'Left' and political_ideology != 'Right':
            logging.error(f"{political_ideology} is not a valid ideology")
            sys.exit(1)
        self._political_ideology = political_ideology
        if political_ideology == 'Left':
            self._insults = ['Racist', 'Homophobic', 'Transphobic', 'Xenphobic', 'Nazi', 'Bigot', 'I give up']
        if political_ideology == 'Right':
            self._insults = ['Snowflake', 'Bootlicker', 'Sheep', 'NPC', 'I give up']

    def get_insult(self) -> str:
        return random.choice(self._insults)

class Reaction:
    def __init__(self):
        self._reactions = ['*eye roll*', '*shocked pikachu face*']

    def get_reaction(self) -> str:
        return random.choice(self._reactions)
