#!/usr/bin/env python3
"""Person object"""
import logging
import sys
import random

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


# This is an object describing the state of a person.
class Person:
    """The Person class"""
    def __init__(self, gender: str, pronouns: str,
                 age: int, skin_color: str, political_ideology: str):
        self._gender = gender
        self._pronouns = pronouns
        self._age = age
        self._skin_color = skin_color
        self._political_ideology = political_ideology
        if political_ideology not in ('Left', 'Right'):
            logging.error("%s is not a valid ideology", political_ideology)
            sys.exit(1)
        self._insult_list = Insults(political_ideology=political_ideology)

    def triggers_other_side(self, other_reaction: bool) -> bool:
        """Is the other side triggered ?"""
        if other_reaction:
            return True
        return False

    def make_statement(self) -> str:
        """Let's make a statement"""
        return self._insult_list.get_insult()

    def triggered(self) -> bool:
        """Is triggered ?"""
        reactions: Reaction = Reaction()
        reaction: str = reactions.get_reaction()
        print(reaction)
        if reaction == '*shocked pikachu face*':
            return True
        return False


class Insults:
    """Insults class"""
    def __init__(self, political_ideology: str):
        """Attributes"""
        if political_ideology not in ('Left', 'Right'):
            logging.error("%s is not a valid ideology", political_ideology)
            sys.exit(1)
        self._political_ideology = political_ideology
        if political_ideology == 'Left':
            self._insults = ['Racist', 'Homophobic', 'Transphobic',
                             'Xenphobic', 'Nazi', 'Bigot', 'I give up']
        if political_ideology == 'Right':
            self._insults = ['Snowflake', 'Bootlicker',
                             'Sheep', 'NPC', 'I give up']

    def get_insult(self) -> str:
        """Get an insult"""
        return random.choice(self._insults)


class Reaction:
    """Reaction class"""
    def __init__(self):
        """Attributes"""
        self._reactions = ['*eye roll*', '*shocked pikachu face*']

    def get_reaction(self) -> str:
        """Get reaction"""
        return random.choice(self._reactions)
