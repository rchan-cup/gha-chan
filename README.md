![coverage](https://img.shields.io/static/v1?label=coverage&message=52%25&color=orangeorange&logo=python)




## How to Test

Install the requirements.txt first:

`sudo pip install -r requirements.txt`

From this directory, the following will run the unit-tests:

`python3 -m pytest`


To run the tests in `pipeline-tests` or `notebook-tests`, uncomment them in `pytest.ini` and then re-run:

`python3 -m pytest`

Note: the IP addresses in `sample-click-logs.csv` are not real IP addresses (for confidentiality reasons).
However, the IP addresses included in the unit tests are real IP addresses.

