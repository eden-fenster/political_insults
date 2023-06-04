#!/usr/bin/env python3
"""Political Insults - Database"""
import json
import logging
from log_database import Database
from create_database import create
from flask import Flask, request

app = Flask(__name__)

# pylint: disable=invalid-name

# List to store received response.
responses = []
db = Database(database_name='political_insults_logs')


# Returns the results
@app.route('/database')
def get_database():
    """Getting from database"""
    return json.dumps(db.show_all())


@app.route('/database', methods=['POST'])
def add_to_database():
    """Adding to database"""
    # Adding to list.
    responses.append(request.get_json())
    time = responses[len(responses) - 1]["Time"]
    date = responses[len(responses) - 1]["Date"]
    log = responses[len(responses) - 1]["Log"]
    # Create database.
    create(database_name='political_insults_logs')
    logging.debug("created")
    # Adding to database
    db.add_one(time=time, date=date, log=log)
    return '', 204


# Delete previous records.
@app.route('/database', methods=['DELETE'])
def delete_records(id_to_delete: str):
    """Deleting from database"""
    db.delete_one(id=id_to_delete)
    logging.debug("record deleted")
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='political_insults_database')
