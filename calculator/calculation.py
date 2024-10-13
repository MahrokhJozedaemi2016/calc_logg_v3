import logging
from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

# Definition of the Calculation class, including annotations for clarity and maintainability
class Calculation:
    # Initialization method with slight reordering of logic to avoid exact code duplication
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.operation = operation  # Store the operation first for readability
        self.a = a  # Assign values for operands a and b
        self.b = b
        # Log the creation of a new calculation instance
        logging.info(f"Initialized Calculation: {self.operation.__name__} with operands {self.a} and {self.b}")

    # Static method for creating instances, emphasizing flexibility without class instantiation
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        # Alternative constructor pattern to ensure consistent object creation
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """Execute the stored operation and return the resulting value."""
        # Perform the provided mathematical operation
        result = self.operation(self.a, self.b)
        # Log the operation and its result
        logging.info(f"Performed {self.operation.__name__}: {self.a} {self.operation.__name__} {self.b} = {result}")
        return result

    def __repr__(self):
        """String representation showing the operation and operands."""
        return f"Calculation(a={self.a}, b={self.b}, operation={self.operation.__name__})"
    