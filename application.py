# -*- coding: utf-8 -*-
#
# Copyright (c) Sangsu Ryu
# Licensed under the terms of the MIT license

from flask import Flask, g, jsonify

import mysql.connector

from database.database import config

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TESTING=False
)

@app.before_request
def beforeRequest():
    # Create database connection
    g.database = mysql.connector.connect(**config)

@app.teardown_request
def teardownRequest(exception):
    # Close database connection
    if hasattr(g, 'database') == True:
        g.database.close()

@app.route('/<text>', methods=['GET'])
def index(text):
    with g.database.cursor(dictionary=True) as cursor:
        # Start transaction
        g.database.start_transaction()

        # Execute queries
        cursor.execute('INSERT INTO data VALUES(NULL, %s)', [text])
        cursor.execute('SELECT * FROM data')

        # Fetch data
        data = cursor.fetchall()

        # If Flask application is not test mode, then commit transaction
        if app.testing == False:
            g.database.commit()

    return jsonify({
        'data': data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)