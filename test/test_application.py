# -*- coding: utf-8 -*-
#
# Copyright (c) Sangsu Ryu
# Licensed under the terms of the MIT license

import pytest

from application       import app
from database.database import connection

@pytest.fixture
def client():
    # Set Flask application to test mode
    app.config['TESTING'] = True

    # Generate Flask test client
    with app.test_client() as client:
        yield client

def test_index(client):
    # Get response
    response = client.get('/test').json

    # Rollback transaction
    connection.rollback()

    # Print response
    print(response)

    # Test response
    assert response['data'][-1]['text'] == 'test'