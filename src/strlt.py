#!/usr/bin/env python
# strlt.py: structure that create store structure list

import os

class StrLt(object):
    # TODO: clean all ugly things.... I don't have time right now

    def __init__(self, strlist=[]):
        # nproc: number of threads
        # wdir: directory to store output structures
        # strlist: a list of structures
        self.sl = strlist

    @classmethod
    def from_xtlopt(cls, fpath, xdpath, 
                    enpmax=5., 
                    nsmax=120):
        # xdpath is the folder contains all xtalopt runs
        # fpath is pointing to the "results.txt" file of an xtalopt run
        # enpmax is the maximum RELATIVE enthalpy above enpmin
        # nsmax is the maximum number of structure chosen
        strlist = []
        with open(fpath, 'r') as f:
            rdat = f.readlines()

        # in this case let's neglect the hardness stuff:
        # Rank Gen ID Enthalpy/FU FU SpaceGroup Status
        # 0    1   2  3           4  5          6+
        ns = 0; enpmin = float(rdat[1].split()[3])
        for i in rdat[1:]:
            enp = float(i.split()[3])
            tdir = (
                xdpath 
                + ("00000%s" % i.split()[1])[-5:]
                + ("00000%s" % i.split()[2])[-5:]
            )
            if ns >= nsmax or enp >= enpmin + enpmax:
                break
            elif os.path.isfile(tdir+"CONTCAR"):
                print "CONTCAR is missing from %s" % tdir
                continue
            else:
                strlist.append(tdir+"CONTCAR")

        return cls(strlist)

