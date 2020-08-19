#!/usr/bin/env python
# symstrs.py: symmetrize all structures in the same folder
# endwith "*.poscar"

from libxtlp import poslst, chk_tdir
from multiprocessing import Pool, cpu_count
import os
from subprocess import Popen, PIPE

def aflowsym(fpth, prim=True): 
    finp = open(fpth)
    proc1 = Popen(['aflow', '--wyccar=loose'], stdin=open(fpth),
                 stdout=PIPE, stderr=PIPE)
    stdo1, stde1 = proc1.communicate()
    finp.close()
    proc2 = Popen(['aflow', '--poscar'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdo2, stde2 = proc2.communicate(input=stdo1)
    if prim:
        proc3 = Popen(['aflow', '--sprim'], stdin=PIPE, 
                      stdout=PIPE, stderr=PIPE)
        stdo3, stde3 = proc3.communicate(input=stdo2)
        return stdo3
    else:
        return stdo2


if __name__ == '__main__':
    wdir = os.getcwd()
    plst = poslst(wdir)
    pool = Pool(processes=cpu_count())
    print "NUMBER OF PROCESSOR IS %i" % cpu_count()
    sfils = pool.map(aflowsym, plst)
    pool.close()
    tdir = chk_tdir(tdn="sydir")
    os.mkdir(tdir)
    print "WRITE STRUCTURES INTO %s" % tdir
    for i in range(len(sfils)):
        with open(os.path.join(tdir, plst[i]), 'w') as f:
            f.write(sfils[i])
    
