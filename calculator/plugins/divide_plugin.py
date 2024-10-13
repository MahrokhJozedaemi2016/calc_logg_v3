import logging
from calculator.commands import Command

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            logging.error("Attempted division by zero.")
            raise ValueError("Cannot divide by zero")
        result = self.a / self.b
        logging.info(f"Division operation: {self.a} / {self.b} = {result}")
        return result

def register():
    return DivideCommand
