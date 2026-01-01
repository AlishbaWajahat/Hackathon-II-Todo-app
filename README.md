# Enhanced Todo List Manager

An interactive command-line todo list application with rich UI and enhanced functionality.

## Features

- 📝 Add new tasks with title and description
- 📋 View all tasks with rich formatting
- ✏️ Update task details (title and description)
- 🗑️ Delete tasks with confirmation
- ✅ Toggle task completion status
- 🎨 Rich UI with colorful formatting
- ⬆️ Arrow key navigation for all selections
- 🔁 Automatic ID reuse after deletion

## Installation

1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install rich inquirer
   ```

## Usage

Run the application:
```bash
python src/todo.py
```

The application provides an interactive menu with the following options:
1. Add Task - Create a new task with title and description
2. View All Tasks - Display all tasks with status indicators
3. Update Task - Modify existing task details
4. Delete Task - Remove tasks with confirmation
5. Toggle Task Completion - Mark tasks as complete/incomplete
6. Exit - Quit the application

## Enhanced UI Features

- **Rich Formatting**: Colorful and styled output using the `rich` library
- **Arrow Navigation**: Use arrow keys to navigate menus and select tasks
- **Visual Indicators**: Clear status indicators for task completion
- **Interactive Prompts**: User-friendly input with validation
- **Confirmation Dialogs**: Prevent accidental deletions

## Technical Details

- **Data Storage**: In-memory storage (data is lost on exit)
- **ID Management**: Automatic ID reuse after task deletion
- **Dependencies**: `rich` for formatting, `inquirer` for interactive selection
- **Python Version**: 3.13+

## Project Structure

```
src/
├── data.py     # Global data storage (tasks, next_id)
├── todo.py     # Main application logic and UI
tests/
└── test_todo.py # Unit tests
```

## Testing

Run the test suite:
```bash
python -m pytest tests/ -v
```