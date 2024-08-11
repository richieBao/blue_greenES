# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:44:02 2024

@author: richiebao
"""
import warnings
warnings.filterwarnings('ignore')

# import pyodbc
# from sqlalchemy import create_engine
import pandas as pd
from utils.args import args

# def accdb2df(db_fp,table_name):
#     conn_str = (
#         r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
#         f"Dbq={db_fp};"
#     )
#     # Create a connection to the database
#     conn = pyodbc.connect(conn_str)
#     query = f"SELECT * FROM {table_name}"
#     # Read the data into a pandas DataFrame
#     df = pd.read_sql(query, conn)
#     # Close the connection
#     conn.close()

#     return df

def SQLite2df(db_fp,table):   
    '''
    function - pandas方法，从SQLite数据库中读取表数据
    
    Paras:
        db_fp - 数据库文件路径；string
        table - 所要读取的表；string

    Returns:
        读取的表；DataFrame        
    '''    
    
    return pd.read_sql_table(table, 'sqlite:///'+'\\\\'.join(db_fp.split('\\'))) #pd.read_sql_table从数据库中读取指定的表    



if __name__=="__main__":
    DB_GLC_INFO_SOURCE=args.db.bng_db #r"C:\Users\richi\omen_richiebao\omen_github\blue_greenES\database\bng_accdb.accdb"
    table_name='glc_categories'
    # df=accdb2df(DB_GLC_INFO_SOURCE,table_name)
    df=SQLite2df(DB_GLC_INFO_SOURCE,table_name)