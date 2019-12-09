import importer.config as config
import importer.db as db
import pandas

import sqlalchemy.types as types
#import mysql.connector
# import pyodbc

from sqlalchemy.dialects import mysql



# read csv data to dataframe with pandas
# datatypes will be assumed
# pandas is smart but you can specify datatypes with the `dtype` parameter
# write to sql table... pandas will use default column names and dtypes

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html?highlight=to_sql#pandas.DataFrame.to_sql




def process_crash_event(f,yaml_config=None):
    conf = yaml_config or config.read("config/crash_event.yaml")
        
    df = pandas.read_table(
        f, sep=conf["file_separator"], keep_default_na=conf["keep_default_na"]
    )

    df.to_sql(
        conf["name"],
        db.ENGINE,
        if_exists="fail",
        index=conf["index"],
        index_label=conf["index_label"],
        dtype=conf["dtypes"]
    )
