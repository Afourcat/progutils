#!/usr/bin/env python3.6

import sys
import os
from modules import Module

help = "OUAIS"

def open_modules():
    """ Function that will load all modules """
    dirs = os.listdir("modules/")
    modules = {}
    for dir in dirs:
        modules[dir] = Module(dir)
    return modules

def list_modules(modules):
    for key, mod in modules.items():
        print(mod)

def main():
    """ Main function of the program """
    modules = open_modules()
    if len(sys.argv) < 2:
        list_modules(modules)
        exit()

    try:
        modules[sys.argv[1]].cmds[sys.argv[2]].execute()
    except KeyError:
        list_modules(modules)
    except IndexError:
        modules[sys.argv[1]].list()

if __name__ == "__main__":
    main()
