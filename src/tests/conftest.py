from initialize_db import initialize_db

def pytest_configure():
    initialize_db()