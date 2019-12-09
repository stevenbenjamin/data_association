from unittest import TestCase
import os
from importer.pandas_importer import *
import importer.config as config
import importer.db as db

def curr_dir():
    return os.path.dirname(os.path.realpath(__file__))


def db_import_to_rand(import_file, config_file, f):

        conf=config.read(curr_dir()+config_file)
        test_table_name=conf["name"]+"_test"
        conf["name"]=test_table_name
        data_file=curr_dir()+import_file

        #drop table if it exists and insert into test table
        db.drop_table(test_table_name)
        f(data_file,conf)

        return test_table_name

class TestCrashFileImport(TestCase):
    
    def test_import(self):
        name = db_import_to_rand("/../data/sample/MCMIS/crash/CrashEvent_Excerpt.txt","/../config/crash_event.yaml",process_crash_event)
        print (name)
        # test_table_name="test_crash_events"
                          
        # test_table_name="test_crash_events"
        # conf=config.read(curr_dir()+"/../config/crash_event.yaml")
        # conf["name"]=test_table_name
        # crash_test_file=curr_dir()+"/../data/sample/MCMIS/crash/CrashEvent_Excerpt.txt"

        # #drop table if it exists and insert into test table
        # db.drop_table(test_table_name)
        # process_crash_event(crash_test_file,conf)
        
        result=db.ENGINE.execute("Select count(*) from "+name)
        print(result.first()[0])
        
