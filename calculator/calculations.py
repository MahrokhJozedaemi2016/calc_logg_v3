import logging
from decimal import Decimal
from typing import Callable, List
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []  # Class-level attribute for storing calculation history

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)
        logging.info(f"Added calculation to history: {calculation}")

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire calculation history."""
        # Log the retrieval of the history
        logging.info(f"Retrieving calculation history with {len(cls.history)} items.")
        # Return a copy of the history to avoid accidental modification
        return cls.history.copy()

    @classmethod
    def clear_history(cls):
        """Completely clear the stored history of calculations."""
        logging.info("Clearing calculation history.")
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if no history exists."""
        if cls.history:
            logging.info(f"Retrieving latest calculation: {cls.history[-1]}")
            return cls.history[-1]
        else:
            logging.info("No calculations in history to retrieve.")
            return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        # Log the search for specific operations in history
        results = [calc for calc in cls.history if calc.operation.__name__ == operation_name]
        logging.info(f"Found {len(results)} calculations with operation '{operation_name}'.")
        return results
