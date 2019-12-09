import yaml
import sqlalchemy.types as types

def read(f):
    with open(f) as file:
        conf=  yaml.load(file, yaml.Loader)
        conf["dtypes"]=datatypes_to_sqltypes(conf["types"])
        return conf


def datatypes_to_sqltypes(dtypes):
    """ from e.g.
    [{'CRASH_EVENT_ID': 'types.INTEGER,'}, 
    {'CRASH_ID': 'types.INTEGER,'}, 
    {'EVENT_OTHER_DESC': 'types.VARCHAR(100),'}] to

    "CRASH_EVENT_ID": types.INTEGER,
    "CRASH_ID": types.INTEGER,
    "EVENT_OTHER_DESC": types.VARCHAR(100),
    """
    out = {}
    for t in dtypes:
        kv=t.popitem()
        print( kv)
        out[kv[0]] = eval("types."+kv[1])
    return out

# https://stackoverflow.com/questions/15804685/sqlalchemy-integer-column-size
#              mysql.INTEGER(20),
