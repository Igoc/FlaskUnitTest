# -*- coding: utf-8 -*-
#
# Copyright (c) Sangsu Ryu
# Licensed under the terms of the MIT license

from flask import g

import pytest

from application import app

@pytest.fixture
def client():
    # Set Flask application to test mode
    app.config['TESTING'] = True

    # Generate Flask test client
    with app.test_client() as client:
        yield client

    # Reset Flask application mode
    app.config['TESTING'] = False

def test_index(client):
    # Get response
    response = client.get('/test').json

    # Rollback transaction
    g.database.rollback()

    # Print response
    print(response)

    # Test response
    assert response['data'][-1]['text'] == 'test'