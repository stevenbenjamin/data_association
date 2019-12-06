import pandas
import sqlalchemy
import sqlalchemy.types as types
#import pyodbc
import mysql.connector
from settings import *
from sqlalchemy.dialects import mysql 
def read_crash_event():
    f="/Users/steven/koffie/data_association/data/sample/MCMIS/crash/CrashEvent_Excerpt.txt"

    connection_string="mysql+mysqlconnector://{}:{}@{}:{}/{}".format(DB_USER,DB_PASS,DB_HOST,DB_PORT,DB_SCHEMA)

    engine = sqlalchemy.create_engine(connection_string)

    df = pandas.read_table(f, sep='\t', keep_default_na=False)
    # read csv data to dataframe with pandas
    # datatypes will be assumed
    # pandas is smart but you can specify datatypes with the `dtype` parameter
    # write to sql table... pandas will use default column names and dtypes

    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html?highlight=to_sql#pandas.DataFrame.to_sql
    df.to_sql('crash_event',engine, if_exists='fail', index=False, index_label="CRASH_EVENT_ID",
            dtype={"CRASH_EVENT_ID":types.INTEGER, "CRASH_ID":types.INTEGER, "SEQ_NO":types.INTEGER, "EVENT_ID":types.INTEGER, "EVENT_OTHER_DESC":types.VARCHAR(100)})


#https://stackoverflow.com/questions/15804685/sqlalchemy-integer-column-size
#              mysql.INTEGER(20),
#from sqlalchemy.dialects import mysql 
