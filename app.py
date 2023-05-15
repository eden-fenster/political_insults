import json
import logging

import requests
from flask import Flask, render_template, request

import main
from main import make_person, fight
from person import Person

app = Flask(__name__)

# Opening page to input details.
# List to store received people.
people = []
# List to store fight
fight_log = []


# First player
@app.route('/')
def input_first():
    return render_template('index.html')


@app.route('/get_second', methods=['GET', 'POST'])
def get_second():
    # Input first.
    gender = request.form.get('gender')
    pronouns = request.form.get('pronouns')
    age = request.form.get('age')
    skin_color = request.form.get('skincolor')
    political_ideology = request.form.get('politicalideology')
    logging.debug(f"Input is {gender} \n {pronouns} \n {age} \n {skin_color} \n {political_ideology}")
    # Put into dict.
    dict_to_send: dict = {'Gender': gender, 'Pronouns': pronouns, 'Age': age, 'Skin Color': skin_color,
                          'Political Ideology': political_ideology}
    # Sent to processor.
    requests.post('http://127.0.0.1:8000', json=dict_to_send)
    logging.debug("Sent")
    return render_template('index_2.html')


def fight():
    # Input second.
    # Put into dict.
    # Sent to processor.
    # Fight !
    pass


if __name__ == "__main__":
    app.run(debug=True)
