import json
import re

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
    printing_fight = json.dumps(fight_log)
    formatted_fight = re.sub(r"[\[\]]", "", printing_fight)
    return json.dumps(formatted_fight)


@app.route('/people', methods=['POST'])
def add_grids():
    # Add person to list.
    print("Received")
    people.append(request.get_json())

    # Put the people into Person objects, calling make_person.
    p1: Person = Person(gender=people[0]['Gender 1'], pronouns=people[0]['Pronouns 1'],
                        age=people[0]['Age 1'], skin_color=people[0]['Skin Color 1'],
                        political_ideology=people[0]['Political Ideology 1'])
    p2: Person = Person(gender=people[0]['Gender 2'], pronouns=people[0]['Pronouns 2'],
                        age=people[0]['Age 2'], skin_color=people[0]['Skin Color 2'],
                        political_ideology=people[0]['Political Ideology 2'])
    # Fight
    fight_string: str = fight(one_who_is_making_statement=p1, one_who_might_get_triggered=p2, return_string='')
    print(f"fight is {fight_string}")
    # Put fight log inside string and return that.
    fight_log.append(fight_string)
    # Need to learn how to print in real time on webpage.
    # for every line in return string, return what we have up until now + new line.
    return '', 204


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')
