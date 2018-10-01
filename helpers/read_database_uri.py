import os


def read_database_uri():
    with open(os.path.join(os.path.dirname(__file__), "database_uri.txt"), "r") as file:
        for line in file:
            return str(line)
