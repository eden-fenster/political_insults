#!/usr/bin/env python3
"""Political Insults Game - Processor"""
import json
import logging
import re
from typing import List

from flask import Flask, request

from main import fight
from person import Person

app = Flask(__name__)

# Opening page to input details.
# List to store received people.
people: List[dict] = []
# List to store fight
fight_log: List[str] = []


# Returns the results

# How to return webpages in delay - read about it.
@app.route('/fight')
def get_fight():
    """Return fight"""
    # Return results.
    printing_fight = json.dumps(fight_log)
    formatted_fight = re.sub(r"[\[\]]", "", printing_fight)
    return json.dumps(formatted_fight)


@app.route('/people', methods=['POST'])
def add_grids():
    """Create objects for fight"""
    # Add person to list.
    logging.debug("Received")
    people.append(request.get_json())

    # Put the people into Person objects, calling make_person.
    p_1: Person = Person(gender=people[0]['Gender 1'], pronouns=people[0]['Pronouns 1'],
                         age=people[0]['Age 1'], skin_color=people[0]['Skin Color 1'],
                         political_ideology=people[0]['Political Ideology 1'])
    p_2: Person = Person(gender=people[0]['Gender 2'], pronouns=people[0]['Pronouns 2'],
                         age=people[0]['Age 2'], skin_color=people[0]['Skin Color 2'],
                         political_ideology=people[0]['Political Ideology 2'])
    # Fight
    fight_string: str = \
        fight(one_who_is_making_statement=p_1, one_who_might_get_triggered=p_2, return_string='')
    logging.debug("fight is %s", fight_string)
    # Put fight log inside string and return that.
    fight_log.append(fight_string)
    # Need to learn how to print in real time on webpage.
    # for every line in return string, return what we have up until now + new line.
    return '', 204


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='political_insults_processor')
