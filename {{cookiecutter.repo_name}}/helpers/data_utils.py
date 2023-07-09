import re, os
import pandas as pd
import numpy as np
import psycopg2
from app import app, cache
from dash_table.Format import Format, Scheme, Sign, Symbol
import dash_table.FormatTemplate as FormatTemplate
from helpers.currency_list import cl

#####################################################################################################################################
""" LAYOUT custom specifications """

# the postgres database name. is required for only local dev.
db_name = "postgresdb"

# the max number of scenarios to be supported
num_scenarios = 10

"""
# Currency symbol parameters
1. refer to the json in currency_list.py for the relevant currency you need and specify it as either
    suffix or prefix depending on the general convention for that specific currency.
2. if suffix, initialize prefix as empty string and vice-versa.
"""
currency = cl["USD"]["symbol"]
currency_suffix = ""
currency_prefix = f"{currency}"

## FOR POSTGRES DB SETUP
# def dbconn(pgdb=os.environ.get('POSTGRES_DB', dtcg.db_name)):
#     pgdb = pgdb
#     pguser = os.environ.get('POSTGRES_USER', 'postgres')
#     pgpswd = os.environ.get('POSTGRES_PASSWORD', 'secret')
#     pghost = os.environ.get('POSTGRES_HOST', 'localhost')
#     pgport = os.environ.get('POSTGRES_PORT', '5432')
#     return psycopg2.connect(database=pgdb, user=pguser, password=pgpswd,
#                             host=pghost, port=pgport)

###########################################################################################################################

# the format template for percentage fields
format_perc = Format(
    precision=1, scheme=Scheme.fixed, symbol=Symbol.yes, symbol_suffix="%"
)

# the format template for monetary fields
format_num = Format(
    group=",",
    precision=0,
    scheme=Scheme.fixed,
    symbol=Symbol.yes,
    symbol_suffix=dtcg.currency_suffix,
    symbol_prefix=dtcg.currency_prefix,
)

# the format template for non-monetary fields
format_num_raw = Format(group=",", precision=0, scheme=Scheme.fixed)
