import json

from flask import Flask, request, logging

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
    people.append(request.get_json())
    # Put the people into Person objects, calling make_person.
    p1: Person = Person(gender=people[0]['Gender'], pronouns=people[0]['Pronouns'],
                        age=people[0]['Age'], skin_color=people[0]['Skin Color'],
                        political_ideology=people[0]['Political Ideology'])
    p2: Person = Person(gender=people[1]['Gender'], pronouns=people[1]['Pronouns'],
                        age=people[1]['Age'], skin_color=people[1]['Skin Color'],
                        political_ideology=people[1]['Political Ideology'])
    # Fight
    fight_string: str = fight(one_who_is_making_statement=p1, one_who_might_get_triggered=p2)
    logging.debug(f"fight is {fight_string}")
    # Put fight log inside string and return that.
    fight_log.append(fight_string)
    # Need to learn how to print in real time on webpage.
    return '', 204


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
