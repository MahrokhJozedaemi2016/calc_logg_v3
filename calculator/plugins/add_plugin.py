import logging
from calculator.commands import Command

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a + self.b
        logging.info(f"Add operation: {self.a} + {self.b} = {result}")
        return result

def register():
    return AddCommand