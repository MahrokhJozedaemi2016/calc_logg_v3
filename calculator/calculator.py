import logging
import importlib
from calculator.commands import Command  # Import the Command class for command-based operations

class Calculator:
    def __init__(self):
        self.history = []  # Maintain a history of executed commands
        self.plugins = {}  # Dictionary to store loaded plugins
        logging.info("Calculator initialized with empty history and plugins.")

    def compute(self, command: Command):
        """Execute a command and store it in the history."""
        result = command.execute()  # Execute the provided command
        self.history.append(command)  # Store the command in history
        logging.info(f"Executed command: {command}. Result: {result}")
        return result  # Return the result of the command

    def load_plugin(self, plugin_name: str):
        """Dynamically load a plugin by its name from the plugins folder."""
        try:
            # Import the plugin module dynamically from the plugins folder
            plugin_module = importlib.import_module(f"calculator.plugins.{plugin_name}")
            # Register the command class from the plugin
            command_class = plugin_module.register()
            # Store the command class in the plugins dictionary
            self.plugins[plugin_name] = command_class
            logging.info(f"Plugin '{plugin_name}' loaded successfully.")
        except ImportError:
            logging.error(f"Failed to load plugin: {plugin_name}")
            raise ImportError(f"Failed to load plugin: {plugin_name}")

    def create_command(self, plugin_name: str, *args):
        """Create and return a command from the loaded plugin."""
        # Check if the plugin has been loaded
        if plugin_name in self.plugins:
            command_instance = self.plugins[plugin_name](*args)
            logging.info(f"Created command from plugin '{plugin_name}' with arguments {args}.")
            return command_instance
        else:
            logging.error(f"Plugin not found: {plugin_name}")
            raise ValueError(f"Plugin not found: {plugin_name}")
