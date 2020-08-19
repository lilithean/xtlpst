#!/usr/bin/env python
# libxtlp.py: lib function for whatever it helps

import os
from shutil import copyfile
from multiprocessing import Pool, cpu_count

def poslst(dpth):
    return [x for x in os.listdir(dpth) if x.endswith(".poscar")]

def chk_tdir(tdn="xtdir", idx=1):
    while os.path.isdir('%s%i' % (tdn, idx)): idx += 1
    return '%s%i' % (tdn, idx)

def chk_tfil(tfn="xtmp", idx=1):
    while os.path.isfile('%s%i' % (tfn, idx)): idx += 1
    return '%s%i' % (tfn, idx)

def cp_str(plst, tdir):
    print "CP STR TO %10s" % tdir
    os.mkdir(tdir)
    (copyfile(x, os.path.join(tdir, x)) for x in plst)

