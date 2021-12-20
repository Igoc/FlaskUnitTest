# Flask Unit Test

#### &nbsp; Example for Flask unit test using pytest and MySQL

&nbsp; This project is an example for Flask unit test. <br/>
&nbsp; It shows how to use MySQL transaction for testing. <br/><br/>

## Requirements

### Python

&nbsp; Python 3.8 or later with all [requirements.txt](https://github.com/Igoc/FlaskUnitTest/blob/main/requirements.txt).

``` bash
pip install -r requirements.txt
```

<br/>

### MySQL

&nbsp; MySQL schema is defined in [database/database.sql](https://github.com/Igoc/FlaskUnitTest/blob/master/database/database.sql).

``` mysql
SOURCE database/database.sql;
```

<br/>

### Environment Variables

&nbsp; Need to set environment variables below.

``` bash
export MYSQL_USER="<MYSQL USER>"
export MYSQL_PASSWORD="<MYSQL PASSWORD>"
```

<br/>

## Usage

``` bash
# Run Flask application at localhost:5050
python application.py

# Test
python -m pytest -s test/
```

<br/>

## Results

### Flask Application

``` html
<!-- First request using localhost:5050/a -->
{
  "data": [
    {
      "id": 1,
      "text": "a"
    }
  ]
}

<!-- Second request using localhost:5050/b -->
{
  "data": [
    {
      "id": 1,
      "text": "a"
    },
    {
      "id": 2,
      "text": "b"
    }
  ]
}
```

&nbsp; If Flask application is not test mode, the transaction is commited. <br/><br/>

### Test

``` bash
# First test
============================= test session starts ==============================
...
test/test_application.py {'data': [{'id': 1, 'text': 'test'}]}
...
======================== 1 passed, 4 warnings in 0.23s =========================

# Second test
============================= test session starts ==============================
...
test/test_application.py {'data': [{'id': 2, 'text': 'test'}]}
...
======================== 1 passed, 4 warnings in 0.14s =========================
```

&nbsp; If Flask application is test mode, the transaction is rolled back. <br/>
&nbsp; But even if the transaction is rolled back, auto increment continues to accumulate.