#!/usr/bin/env python3
"""Political Insults Game - Web"""
import logging
from typing import List

from split import back_to_list
import requests
from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)

# Opening page to input details.


# First player
@app.route('/')
def input_first():
    """Input the players"""
    return render_template('index.html')


@app.route('/fight', methods=['GET', 'POST'])
def fight():
    """The actual fight"""
    # Input the two players.
    gender_1 = request.form.get('gender1')
    pronouns_1 = request.form.get('pronouns1')
    age_1 = request.form.get('age1')
    skin_color_1 = request.form.get('skincolor1')
    political_ideology_1 = request.form.get('politicalideology1')
    print\
        (f"Input is {gender_1} \n {pronouns_1} \n {age_1}"
         f" \n {skin_color_1} \n {political_ideology_1}")

    gender_2 = request.form.get('gender2')
    pronouns_2 = request.form.get('pronouns2')
    age_2 = request.form.get('age2')
    skin_color_2 = request.form.get('skincolor2')
    political_ideology_2 = request.form.get('politicalideology2')
    print\
        (f"Input is {gender_2} \n {pronouns_2} \n {age_2}"
         f" \n {skin_color_2} \n {political_ideology_2}")
    # Put into dict.
    dict_to_send: dict = {'Gender 1': gender_1, 'Pronouns 1': pronouns_1, 'Age 1': age_1,
                          'Skin Color 1': skin_color_1,
                          'Political Ideology 1': political_ideology_1, 'Gender 2': gender_2,
                          'Pronouns 2': pronouns_2, 'Age 2': age_2, 'Skin Color 2': skin_color_2,
                          'Political Ideology 2': political_ideology_2}
    # Sent to processor.
    requests.post('http://political_insults_processor:8000/people', json=dict_to_send, timeout=10)
    logging.debug("Sent")
    # Fight !
    response = requests.get('http://political_insults_processor:8000/fight', timeout=10)
    logging.debug("Got Response")
    to_print: List[str] = back_to_list(string=response.json())
    return render_template('style.html', Title='Fight Log', Content='Here is the fight log', List=to_print)


if __name__ == "__main__":
    app.run(debug=True, host='political_insults_web')
