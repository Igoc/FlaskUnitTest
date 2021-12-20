# -*- coding: utf-8 -*-
#
# Copyright (c) Sangsu Ryu
# Licensed under the terms of the MIT license

from flask import Flask, jsonify

from database.database import connection

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TESTING=False
)

@app.route('/<text>', methods=['GET'])
def index(text):
    with connection.cursor(dictionary=True) as cursor:
        # Start transaction
        connection.start_transaction()

        # Execute queries
        cursor.execute('INSERT INTO data VALUES(NULL, %s)', [text])
        cursor.execute('SELECT * FROM data')

        # Fetch data
        data = cursor.fetchall()

        # If Flask application is not test mode, then commit transaction
        if app.testing == False:
            connection.commit()

    return jsonify({
        'data': data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)