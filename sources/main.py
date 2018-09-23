#!/usr/bin/env python3

import sys
import os
from modules import Module

def open_modules():
    """ Function that will load all modules """
    dirs = os.listdir("modules/")
    modules = {}
    for dir in dirs:
        modules[dir] = Module(dir)
        print(modules[dir])

def main():
    """ Main function of the program """
    open_modules()

if __name__ == "__main__":
    main()
