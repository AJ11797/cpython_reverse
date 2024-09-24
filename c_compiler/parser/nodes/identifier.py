import re


class Identifier():
    def __init__(self, name):
        self.name = name
        self.check_valid_name()

    def __str__(self):
        return self.name

    def check_valid_name(self):
        if re.search("^[a-zA-Z_]\\w*\\b", self.name) is None:
            raise Exception("Identifier is invalid")
