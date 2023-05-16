import json
import logging
from flask import Flask, request

from main import fight
from person import Person

app = Flask(__name__)

# Opening page to input details.
# List to store received people.
people = []
# List to store fight
fight_log = []


# Returns the results
@app.route('/people')
def get_grids():
    # Return results.
    return json.dumps(people)


@app.route('/fight')
def get_fight():
    # Return results.
    return json.dumps(fight_log)


@app.route('/people', methods=['POST'])
def add_grids():
    # Add person to list.
    logging.debug("Received")
    people.append(request.get_json())

    # Put the people into Person objects, calling make_person.
    p1: Person = Person(gender=people['Gender 1'], pronouns=people['Pronouns 1'],
                        age=people['Age 1'], skin_color=people['Skin Color 1'],
                        political_ideology=people['Political Ideology 1'])
    p2: Person = Person(gender=people['Gender 2'], pronouns=people['Pronouns 2'],
                        age=people['Age 2'], skin_color=people['Skin Color 2'],
                        political_ideology=people['Political Ideology 2'])
    # Fight
    fight_string: str = fight(one_who_is_making_statement=p1, one_who_might_get_triggered=p2)
    logging.debug(f"fight is {fight_string}")
    # Put fight log inside string and return that.
    fight_log.append(fight_string)
    # Need to learn how to print in real time on webpage.
    return '', 204


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
