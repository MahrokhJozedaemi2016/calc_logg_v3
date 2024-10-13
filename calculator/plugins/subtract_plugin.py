import logging
from calculator.commands import Command

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        result = self.a - self.b
        logging.info(f"Subtract operation: {self.a} - {self.b} = {result}")
        return result

def register():
    return SubtractCommand
