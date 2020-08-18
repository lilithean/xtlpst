#!/usr/bin/env python
# symtrz.py: manipulate structures in a list

import os
from multiprocessing import Pool
from strlt import StrLt

asympth='/projects/academic/ezurek/xiaoyu/xtalopt/xtalpost/aflowsym.sh'

class Symtrz(object):

    def __init__(self, strlt):
        self.strlt = strlt

    @staticmethod
    def aflow_sym(s, ts): 
        os.system("%s %s %s" % (asympth, s, ts))

if __name__ == '__main__':
    Symtrz.aflow_sym('CONTCAR', 'sym-CONTCAR')
