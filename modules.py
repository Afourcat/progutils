# python class modules

import os
import toml
from commands import *

class Module:
    """
    class modules representing a instance of a modules
    modules define a type of a command and all commands linked to it
    """

    def __init__(self, name, path):
        """Constructor of a module"""
        with open(path + "modules/{}/mod.toml".format(name)) as f:
            to = toml.load(f)
        self.name = to["name"]
        self.cmds = {}
        try:
            self.description = to["description"]
        except KeyError:
            self.description = "No description"
        for key, cmd in to["commands"].items():
            self.cmds[key] = Command(key, path + "modules/{}/{}".format(name, cmd))

    def list(self):
        print(self.__str__())

    def __str__(self):
        output = "Module: {}\nDescription: {}\n".format(self.name, self.description)
        for key, cmd in self.cmds.items():
            output += "\t" + cmd.__str__()
        return output

    def __repr__(self):
        print(self.__str__())
