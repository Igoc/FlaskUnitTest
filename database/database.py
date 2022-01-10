# -*- coding: utf-8 -*-
#
# Copyright (c) Sangsu Ryu
# Licensed under the terms of the MIT license

import os

config = {
    'host': 'localhost',
    'port': 3306,

    'user': os.getenv('MYSQL_USER'),
    'passwd': os.getenv('MYSQL_PASSWORD'),

    'database': 'flask_unit_test',
    'charset': 'utf8'
}