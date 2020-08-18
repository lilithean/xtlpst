#!/usr/bin/env python
# findup.py: this suppose to filter duplicate structures in 
# the same folder endwith "*.poscar"
#from multiprocessing import Pool
from subprocess import Popen, PIPE
from datetime import datetime
import os
import sys

tollst = [['0.1', '0.2'], ['0.2', '0.4'], ['0.3', '0.6'], ['0.5', '0.8']]

def poslst(dpth):
    return [x for x in os.listdir(dpth) if x.endswith(".poscar")]

def xtlcmp(pos1, pos2, tol):
    #print('CMP %16s %16s    TOL %5s %5s' % (pos1, pos2, tol[0], tol[1]))
    # won't check error: do your own best to avoid it
    proc = Popen(['xtlcmp', pos1, pos2, tol[0], tol[1]], 
                 stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    return False if "NOT" in stdout else True

def chk_tmpdir(tdn="xtdir", idx=1):
    while os.path.isdir('%s%i' % (tdn, idx)): idx += 1 
    return '%s%i' % (tdn, idx)

def cmpfnc(plst, tol, iplst=[]):
    #print plst, iplst
    if len(plst) <= 1:
        iplst.append(plst[-1])
        return iplst
    else:
        iplst.append(plst[0])
        nplst = [x for x in plst[1:] if not xtlcmp(plst[0], x, tol)]
        cmpfnc(nplst, tol, iplst)
        return iplst

if __name__ == "__main__":
    wdir = os.getcwd()
    plst = poslst(wdir)
    for tol in tollst:
        print "CMP TOL=%5s %5s" % tuple(tol)
        plst =  cmpfnc(plst, tol, iplst=[])
        print "%4i IDENTICAL STR" % len(plst)
        #print plst
    tdir = chk_tmpdir()
    print "CP STR TO %10s" % tdir
    os.mkdir(tdir)
        
