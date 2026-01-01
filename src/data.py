"""
Data storage module for the Todo application.

This module provides global data storage for tasks and the ID generator.
All task data is stored in memory and will be lost when the application exits.

Global Variables:
    tasks (list[dict]): List of all tasks, where each task is a dictionary
                        with keys: id, title, description, completed
    next_id (int): Counter for generating unique sequential task IDs
"""

# Global task storage - list of task dictionaries
tasks: list[dict] = []

# Global ID counter for generating unique sequential task IDs
next_id: int = 1
