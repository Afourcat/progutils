# python class modules

import os
import toml
from commands import *

class Module:
    """
    class modules representing a instance of a modules
    modules define a type of a command and all commands linked to it
    """

    def __init__(self, name):
        """Constructor of a module"""
        with open("modules/{}/mod.toml".format(name)) as f:
            to = toml.load(f)
        self.name = to["name"]
        self.cmds = {}
        for key, cmd in to["commands"].items():
            self.cmds[key] = Command(key, "modules/{}/{}".format(name, cmd))

    def __str__(self):
        output = "Module: {}\n".format(self.name)
        for key, cmd in self.cmds.items():
            output += "\t" + cmd.__str__()
        return output

    def __repr__(self):
        print(self.__str__())