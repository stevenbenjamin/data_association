from unittest import TestCase
import os
from importer.file_import import *


def files(dirname, filter_f):
    fs = []
    for r, d, f in os.walk(dirname):
        for file in f:
            if filter_f(file):
                #                print ("%s--%s--%s" % (r,d,f))
                fs.append(os.path.join(r, file))
    return fs


def curr_dir():
    return os.path.dirname(os.path.realpath(__file__))


def sample_file(s: str) -> str:
    return curr_dir() + "/../data/sample/" + s


class TestImport(TestCase):
    def test_read_header(self):
        # MCMIS data is space delimited
        mcmis = curr_dir() + "/../data/sample/MCMIS"
        for f in files(mcmis, lambda f: f.endswith(".txt")):
            c = columns(f)
            print("%s %s" % (f, len(c)))

        landi = curr_dir() + "/../data/sample/L_AND_I"
        for f in files(landi, lambda f: f.endswith(".txt")):
            c = columns(f, lambda s: s.split("~"))
            print("%s %s" % (f, len(c)))
