import logging
from calculator.commands import Command

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a  # First operand
        self.b = b  # Second operand

    def execute(self):
        result = self.a * self.b
        logging.info(f"Multiply operation: {self.a} * {self.b} = {result}")
        return result

def register():
    return MultiplyCommand
