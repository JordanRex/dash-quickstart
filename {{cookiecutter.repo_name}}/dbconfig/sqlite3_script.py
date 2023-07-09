import sqlite3
from sqlite3 import Error
import pandas as pd

##########################################################################################################################


def create_connection(db_file=f"dbconfig/{builtins.sqldb}.db"):
    """create a database connection to the SQLite database
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file, isolation_level=None)
        # Set journal mode to WAL.
        conn.execute("pragma journal_mode=wal;")
    except Error as e:
        print(e)
    return conn


def pd_from_sql(sql, db_file=f"dbconfig/{builtins.sqldb}.db"):
    conn = create_connection(db_file)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df


##########################################################################################################################


def reindex_tbl(tbl):
    sql = f""" REINDEX '{tbl}'; """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return None


def create_user_logs(vals):
    sql = """ INSERT INTO user_logs (
                         username,
                         timestamp_recorded,
                         trigger
                     )
                     VALUES (
                         ?,?,?
                     ); """
    conn = create_connection()
    params = tuple(item for sublist in vals for item in sublist.values())
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    return None
