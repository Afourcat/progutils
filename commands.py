""" Python class Command """

import toml
import os
import subprocess

class Command:
    """ Command class represent a command in a modules """

    def __init__(self, name, script_path):
        self.name = name
        self.path = script_path

    def __str__(self):
        return "Name: {} => Path: {}\n".format(self.name, self.path)

    def __repr__(self):
        print(self.__str__())

    def execute(self):
        subprocess.call(self.path);
