import mysql.connector
from settings import *
from logger import log
from typing import List


def connect():
    """connect to mysql and return the connection"""
    try:
        return mysql.connector.connect(
            host=DB_HOST,
            database=DB_SCHEMA,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT,
        )
    except mysql.connector.Error as err:
        log.exception(err)


def columns(filename: str, delim_f=lambda s: s.split()) -> List[str]:
    r"""take a file and return a list of columns.

      :delim_f
         func to split delim header into fields or whitespace if left blank
    """

    with open(filename, "r") as f:
        line = f.readline()
        return delim_f(line)



