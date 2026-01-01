# Todo App Quick Start

**Feature**: 001-todo-core-features
**Version**: Phase I (In-Memory)
**Date**: 2026-01-01

## Prerequisites

- **Python**: Version 3.13 or higher ([Download](https://www.python.org/downloads/))
- **UV Package Manager**: Latest version ([Installation](https://github.com/astral-sh/uv#installation))
- **Terminal/Command Line**: Any shell (bash, zsh, PowerShell, cmd)

## Installation

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd Todo-app
```

### Step 2: Verify Python Version

```bash
python --version
# Should show: Python 3.13.x or higher
```

### Step 3: Install Dependencies

```bash
uv sync
```

**Note**: Phase I has no external dependencies - uses Python standard library only.

## Running the Application

### Start the App

```bash
python src/todo.py
```

You should see the main menu:

```
=== Todo List Manager ===
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Toggle Task Completion
6. Exit

Choose an option (1-6):
```

## Usage Guide

### 1. Add a New Task

**Menu Option**: `1`

**Steps**:
1. Enter task title (required)
2. Enter description (optional - press Enter to skip)
3. Task created with auto-generated ID

**Example**:
```
Choose an option (1-6): 1

Enter task title: Buy groceries
Enter task description (optional): Milk, eggs, bread, coffee

✓ Task created successfully! (ID: 1)
```

**Tips**:
- Title cannot be empty or whitespace-only
- Description is optional (can be blank)
- Special characters and emoji are supported
- Task automatically marked as incomplete

### 2. View All Tasks

**Menu Option**: `2`

**Output**: Displays all tasks with:
- Task ID (in brackets)
- Title
- Description (if provided)
- Status (☐ Incomplete or ☑ Complete)

**Example**:
```
Choose an option (1-6): 2

=== All Tasks ===
[1] Buy groceries
    Description: Milk, eggs, bread, coffee
    Status: ☐ Incomplete

[2] Call dentist
    Description: Schedule cleaning appointment
    Status: ☑ Complete

[3] Finish report
    Description:
    Status: ☐ Incomplete

Total tasks: 3
```

**Empty List**:
```
=== All Tasks ===
No tasks found. Add your first task to get started!
```

### 3. Update a Task

**Menu Option**: `3`

**Steps**:
1. Enter task ID
2. Enter new title (or press Enter to keep current)
3. Enter new description (or press Enter to keep current)
4. Task updated with confirmation

**Example**:
```
Choose an option (1-6): 3

Enter task ID to update: 1

Current title: Buy groceries
Enter new title (press Enter to keep current): Buy groceries and cook dinner

Current description: Milk, eggs, bread, coffee
Enter new description (press Enter to keep current): Milk, eggs, bread, coffee, pasta sauce

✓ Task updated successfully!
```

**Tips**:
- Can update title only, description only, or both
- Press Enter without typing to keep current value
- New title cannot be empty (will show error)
- Status (complete/incomplete) remains unchanged

### 4. Delete a Task

**Menu Option**: `4`

**Steps**:
1. Enter task ID to delete
2. Confirm deletion (y/n)
3. Task permanently removed

**Example**:
```
Choose an option (1-6): 4

Enter task ID to delete: 2

Task details:
[2] Call dentist
    Description: Schedule cleaning appointment
    Status: ☑ Complete

Are you sure you want to delete this task? (y/n): y

✓ Task deleted successfully!
```

**Safety Features**:
- Confirmation required before deletion
- Shows task details before confirming
- Can cancel by entering 'n'
- Deletion is permanent (cannot undo)

### 5. Toggle Task Completion

**Menu Option**: `5`

**Steps**:
1. Enter task ID
2. Status toggled automatically (incomplete ↔ complete)
3. Confirmation shown

**Example - Mark Complete**:
```
Choose an option (1-6): 5

Enter task ID to toggle: 1

✓ Task marked as complete!
```

**Example - Mark Incomplete**:
```
Choose an option (1-6): 5

Enter task ID to toggle: 1

✓ Task marked as incomplete!
```

**Tips**:
- Toggles between complete and incomplete
- No confirmation required (easily reversible)
- View tasks to see current status

### 6. Exit Application

**Menu Option**: `6`

**Behavior**:
- Displays "Goodbye!" message
- Closes application
- **All data lost** (in-memory storage only)

```
Choose an option (1-6): 6

Goodbye!
```

## Example Session

Complete workflow from start to finish:

```
$ python src/todo.py

=== Todo List Manager ===
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Toggle Task Completion
6. Exit

Choose an option (1-6): 1

Enter task title: Buy groceries
Enter task description (optional): Milk, eggs, bread

✓ Task created successfully! (ID: 1)

Choose an option (1-6): 1

Enter task title: Call dentist
Enter task description (optional): Schedule appointment

✓ Task created successfully! (ID: 2)

Choose an option (1-6): 2

=== All Tasks ===
[1] Buy groceries
    Description: Milk, eggs, bread
    Status: ☐ Incomplete

[2] Call dentist
    Description: Schedule appointment
    Status: ☐ Incomplete

Total tasks: 2

Choose an option (1-6): 5

Enter task ID to toggle: 2

✓ Task marked as complete!

Choose an option (1-6): 2

=== All Tasks ===
[1] Buy groceries
    Description: Milk, eggs, bread
    Status: ☐ Incomplete

[2] Call dentist
    Description: Schedule appointment
    Status: ☑ Complete

Total tasks: 2

Choose an option (1-6): 6

Goodbye!
```

## Common Error Messages

### "Error: Input cannot be empty"
**Cause**: Entered empty task title
**Solution**: Provide a non-empty title

### "Error: Task {ID} not found"
**Cause**: Referenced non-existent task ID
**Solution**: Use "View All Tasks" to see valid IDs

### "Error: Please enter a valid number"
**Cause**: Entered non-numeric value for task ID
**Solution**: Enter a number (e.g., 1, 2, 3)

### "Error: ID must be positive"
**Cause**: Entered zero or negative number
**Solution**: Use positive task ID from task list

### "Invalid choice. Please try again."
**Cause**: Entered menu option outside 1-6
**Solution**: Choose a number between 1 and 6

## Testing

Run the test suite:

```bash
pytest tests/test_todo.py -v
```

Run tests with coverage report:

```bash
pytest tests/test_todo.py --cov=src --cov-report=term-missing
```

## Troubleshooting

### Problem: "python: command not found"
**Solution**:
- Ensure Python 3.13+ is installed
- Try `python3` instead of `python`
- Add Python to system PATH

### Problem: "No module named pytest"
**Solution**:
```bash
uv add --dev pytest
```

### Problem: Tasks disappear after closing app
**Solution**: This is **expected behavior** in Phase I
- Data stored in memory only (not saved to disk)
- All tasks lost when app closes
- Persistence will be added in Phase II

### Problem: Cannot delete/update task
**Causes & Solutions**:
1. Wrong task ID → Use "View All Tasks" to get correct ID
2. Task already deleted → Check task list
3. Typo in ID → Enter number carefully

## Tips & Best Practices

1. **View tasks first**: Use option 2 to see all task IDs before updating/deleting
2. **Descriptive titles**: Keep titles concise but meaningful
3. **Use descriptions**: Add context in description field for complex tasks
4. **Check before delete**: Review task details shown before confirming deletion
5. **Toggle freely**: Completion status is easily reversible
6. **Session-based**: Plan to complete work in one session (data not persistent)

## Limitations (Phase I)

- **No persistence**: Data lost when app closes
- **Single user**: No multi-user support
- **No categories**: Cannot organize tasks into groups
- **No due dates**: No scheduling or reminders
- **No search**: Must view all tasks to find specific one
- **No undo**: Deleted tasks cannot be recovered

These limitations will be addressed in future phases.

## Next Steps

- **Phase II**: Add file-based persistence (save/load tasks)
- **Phase III**: Add categories and tags
- **Phase IV**: Add due dates and reminders

## Support

For issues or questions:
1. Check this quickstart guide
2. Review error messages carefully
3. Consult README.md for detailed documentation
4. Open an issue on GitHub (if available)
