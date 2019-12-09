from settings import *
import sqlalchemy

CONNECTION_STRING = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(
    DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_SCHEMA
)
ENGINE = sqlalchemy.create_engine(CONNECTION_STRING)

def drop_table(name):
    if exists_table(name):
        ENGINE.execute("DROP TABLE "+name)
        return True
    return False


def exists_table(name):
    result=ENGINE.execute( "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '%s' AND table_name = '%s'".format(DB_SCHEMA,name))
    f=result.first()
    return f[0]==1

