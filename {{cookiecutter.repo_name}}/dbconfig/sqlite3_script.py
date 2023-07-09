import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(db_file=f"dbconfig/{builtins.sqldb}.db"):
    """
    Create a database connection to the SQLite database specified by db_file.

    :param db_file: database file. Defaults to f"dbconfig/{builtins.sqldb}.db".
    :type db_file: str, optional
    :return: Connection object or None
    :rtype: sqlite3.Connection or None
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
    """
    Execute a SQL query and return the results as a pandas DataFrame.

    :param sql: SQL query to be executed.
    :type sql: str
    :param db_file: database file. Defaults to f"dbconfig/{builtins.sqldb}.db".
    :type db_file: str, optional
    :return: DataFrame containing the results of the SQL query.
    :rtype: pandas.DataFrame
    """
    conn = create_connection(db_file)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df

def reindex_tbl(tbl):
    """
    Reindex a table in the SQLite database.

    :param tbl: Name of the table to be reindexed.
    :type tbl: str
    """
    sql = f""" REINDEX \'{tbl}\'; """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def create_user_logs(vals):
    """
    Insert a new record into the user_logs table.

    :param vals: Values to be inserted into the user_logs table.
    :type vals: list
    """
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
