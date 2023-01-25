# Assignment Management

This is a backend service for a classroom. The service is described in detail [here](./Application.md)


## Run Locally

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

3. Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```

4. Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```

5. Start Server

```
bash run.sh
```

6. Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov --cov-report=html
# open htmlcov/index.html
```


## Test Results

![Output-1](https://github.com/Gopi1422/AssignmentManagement/blob/e987567a38bce1739f04ad6684abce6d2b9ec467/screenshots/1.png)
![Output-2](https://github.com/Gopi1422/AssignmentManagement/blob/e987567a38bce1739f04ad6684abce6d2b9ec467/screenshots/2.png)
![Output-3](https://github.com/Gopi1422/AssignmentManagement/blob/8f93d435157d5afe5edf62e65ad6656a4eaef5b7/screenshots/3.png)

