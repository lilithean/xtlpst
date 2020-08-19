#!/usr/bin/env python
# xtlpst.py: the main program that call other functions

from colrslt import CollectResult
from rmvdplct import RemoveDuplicate
from optimize_structure import OptimizeStructure

def main():
    opt_dir = "./opt/"
    struct_list = CollectResults('./local/results.txt', symm='AFlow')
    struct_list = RemoveDuplicate(struct_list)


if __name__ == "__main__":
    main()
