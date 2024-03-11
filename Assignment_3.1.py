"""
Sebi Magyar-Samoila
101223588
"""

import psycopg2


def connection():
    """
    Creates connection to the postgress database
    """
    return psycopg2.connect(
        host = "",
        database = "",
        user = "",
        password = ""
        )