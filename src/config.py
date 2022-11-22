import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

TASKS = os.getenv("TASKS_FILENAME") or "tasks.csv"
TASKS_FILE_PATH = os.path.join(dirname, "..", "data", TASKS)

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "data.sqlite"