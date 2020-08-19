#!/usr/bin/env python
# fnddup.py: this suppose to filter duplicate structures in 
# the same folder endwith "*.poscar"
from functools import partial
from libxtlp import poslst, chk_tdir, cp_str
from multiprocessing import Pool, cpu_count
import os
from subprocess import Popen, PIPE

tollst = [['0.2', '0.4'], ['0.3', '0.6'], ['0.5', '0.8']]

def xtlcmp(pos2, pos1, tol):
    # won't check error: do your own best to avoid it
    proc = Popen(['xtlcmp', pos1, pos2, tol[0], tol[1]], 
                 stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    return pos2 if "NOT" in stdout else False

def cmpfnc(plst, tol, pool, iplst=[], cyc=0):
    print "IN CYC %4i: %4i STR TO CMP" % (cyc, len(plst))
    if len(plst) == 0:
        return iplst 
    elif len(plst) == 1:
        iplst.append(plst[-1])
        return iplst
    else:
        iplst.append(plst[0])
        xcmp = partial(xtlcmp, pos1=plst[0], tol=tol)
        nplst = [x for x in pool.map(xcmp, plst[1:]) if x]
        cmpfnc(nplst, tol, pool, iplst, cyc+1)
        return iplst

if __name__ == "__main__":
    wdir = os.getcwd()
    plst = poslst(wdir)
    pool = Pool(processes=cpu_count())
    print "NUMBER OF PROCESSOR IS %i" % cpu_count()
    for tol in tollst:
        print "="*30
        print "CMP TOL=%5s %5s" % tuple(tol)
        print "%4i STR TO CMP" % len(plst)
        plst =  cmpfnc(plst, tol, pool=pool, iplst=[])
        print "%4i IDENTICAL STR" % len(plst)
    pool.close()
    print "="*30
    cp_str(plst, chk_tdir())
