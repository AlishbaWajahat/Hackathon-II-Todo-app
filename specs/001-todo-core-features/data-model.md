# Data Model: Todo Core Features

**Feature**: 001-todo-core-features
**Date**: 2026-01-01
**Status**: Approved

## Overview

Simple in-memory data model using Python built-in types (list of dictionaries) with procedural access patterns. No OOP, no external dependencies.

## Primary Entity: Task

### Structure

```python
{
    'id': int,           # Unique identifier (auto-generated, sequential)
    'title': str,        # Task title (required, non-empty)
    'description': str,  # Task details (optional, can be empty string)
    'completed': bool    # Completion status (default: False)
}
```

### Field Specifications

#### id (int)
- **Type**: Positive integer
- **Constraints**:
  - Must be unique across all tasks
  - Auto-generated, sequential (1, 2, 3, ...)
  - Never reused within a session
  - Immutable once assigned
- **Generation**: Auto-incrementing global counter
- **Example**: `1`, `42`, `100`

#### title (str)
- **Type**: String
- **Constraints**:
  - Required (cannot be None)
  - Non-empty (cannot be "")
  - Not whitespace-only (cannot be "   ")
  - Max length: No hard limit (Python string max)
- **Validation**: `.strip()` applied, result must be non-empty
- **Examples**:
  - Valid: `"Buy groceries"`, `"Call mom"`, `"Fix bug #123"`
  - Invalid: `""`, `"   "`, `None`

#### description (str)
- **Type**: String
- **Constraints**:
  - Optional (can be empty string)
  - No validation required
  - Whitespace preserved as-is
- **Default**: Empty string `""`
- **Examples**:
  - `"Milk, eggs, bread"`
  - `""`
  - `"Remember to check prices"`

#### completed (bool)
- **Type**: Boolean
- **Constraints**: Must be exactly `True` or `False`
- **Default**: `False` for new tasks
- **State Transitions**:
  - New task → `False`
  - Mark complete → `True`
  - Mark incomplete → `False`

### Example Tasks

```python
# Minimal task (just created)
{
    'id': 1,
    'title': 'Buy milk',
    'description': '',
    'completed': False
}

# Complete task with description
{
    'id': 2,
    'title': 'Finish project report',
    'description': 'Include graphs and analysis section',
    'completed': True
}

# Task with special characters
{
    'id': 3,
    'title': 'Email John re: meeting 📧',
    'description': 'Discuss Q1 budget',
    'completed': False
}
```

## Storage Model

### Global State

```python
# Task storage
tasks: list[dict] = []

# ID generator
next_id: int = 1
```

### Operations

#### Create (Add Task)
```python
# Pseudocode
new_task = {
    'id': generate_task_id(),  # Auto-increment next_id
    'title': validated_title,   # Must be non-empty after strip()
    'description': description or "",  # Default to empty string
    'completed': False
}
tasks.append(new_task)
```

#### Read (Find/Get Tasks)
```python
# Get all tasks
all_tasks = tasks  # Return entire list

# Find by ID
task = next((t for t in tasks if t['id'] == task_id), None)
```

#### Update (Modify Task)
```python
# Find task
task = find_task_by_id(task_id)
if task:
    if new_title is not None:
        task['title'] = new_title  # Must be validated first
    if new_description is not None:
        task['description'] = new_description
```

#### Delete (Remove Task)
```python
# Remove from list
tasks = [t for t in tasks if t['id'] != task_id]
# OR
task = find_task_by_id(task_id)
if task:
    tasks.remove(task)
```

#### Toggle Completion
```python
task = find_task_by_id(task_id)
if task:
    task['completed'] = not task['completed']
```

## Validation Rules

### Title Validation
```python
def validate_title(title: str) -> bool:
    """
    Title is valid if:
    - Not None
    - After strip(), not empty string
    """
    if title is None:
        return False
    if title.strip() == "":
        return False
    return True
```

### ID Validation
```python
def validate_id(task_id: int) -> bool:
    """
    ID is valid if:
    - Positive integer (> 0)
    """
    return isinstance(task_id, int) and task_id > 0
```

## Data Integrity Constraints

### Uniqueness
- **Task IDs**: Guaranteed unique via auto-increment (no manual ID assignment)
- **Titles**: No uniqueness constraint (duplicate titles allowed)

### Referential Integrity
- No foreign keys (single entity)
- No relationships to other entities

### Consistency
- Task list always valid (no orphaned tasks)
- ID counter never decrements (monotonically increasing)
- Completed status always boolean (never null/undefined)

## Performance Characteristics

### Time Complexity
- **Add task**: O(1) - append to list
- **Find by ID**: O(n) - linear search
- **Get all tasks**: O(1) - return reference
- **Update task**: O(n) - find + O(1) modify
- **Delete task**: O(n) - find + O(n) remove
- **Toggle completion**: O(n) - find + O(1) toggle

### Space Complexity
- **Per task**: ~100-500 bytes (depends on title/description length)
- **100 tasks**: ~10-50 KB total

### Scalability
- Acceptable performance for 100-1000 tasks
- Linear search sufficient for spec'd scale
- No indexing needed

## Migration Path (Future Phases)

### Phase II: Persistence
Current dict structure maps naturally to JSON:
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}
```

### Phase III: Database
Current dict structure maps to SQL schema:
```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT DEFAULT '',
    completed BOOLEAN DEFAULT FALSE
);
```

## Edge Cases Handled

1. **Empty task list**: Returns empty list `[]`, not error
2. **Task not found**: Returns `None`, not error
3. **Duplicate delete**: No error (already gone)
4. **ID collision**: Impossible (auto-increment never reuses)
5. **Concurrent access**: N/A (single-user, single-thread)
6. **Special characters in strings**: Accepted as-is (no escaping needed)
7. **Very long strings**: No truncation (Python handles it)

## Assumptions

- Single-threaded access (no race conditions)
- Data lost on program exit (in-memory only)
- No persistence required
- Max 1000 tasks (sufficient for linear search)
- Task IDs never need to be reused
- No audit trail needed (no created_at/updated_at fields)
