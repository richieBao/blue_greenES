# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:44:02 2024

@author: richiebao
"""
import warnings
warnings.filterwarnings('ignore')

import pyodbc
from sqlalchemy import create_engine
import pandas as pd
from utils.args import args

def accdb2df(db_fp,table_name):
    conn_str = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"Dbq={db_fp};"
    )
    # Create a connection to the database
    conn = pyodbc.connect(conn_str)
    query = f"SELECT * FROM {table_name}"
    # Read the data into a pandas DataFrame
    df = pd.read_sql(query, conn)
    # Close the connection
    conn.close()

    return df

if __name__=="__main__":
    DB_GLC_INFO_SOURCE=args.db.bng_db #r"C:\Users\richi\omen_richiebao\omen_github\blue_greenES\database\bng_accdb.accdb"
    table_name='glc_categories'
    accdb2df(DB_GLC_INFO_SOURCE,table_name)