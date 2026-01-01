# Implementation Plan: Todo Core Features

**Branch**: `001-todo-core-features` | **Date**: 2026-01-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-core-features/spec.md`

## Summary

Build a command-line todo application with in-memory storage supporting 5 core operations: Add, Delete, Update, View, and Mark Complete. Implementation will use a **simple, procedural approach in a single Python file** to maximize clarity and minimize complexity. All data stored in memory using basic Python data structures (list of dictionaries), with a menu-driven CLI for user interaction.

**Key Design Decision**: Single-file, procedural implementation (no OOP) prioritizing simplicity and readability over architectural patterns. This aligns with Phase I constraints (in-memory only, stdlib only) and enables rapid development with clear, understandable code.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Python standard library only (no external packages)
**Storage**: In-memory (list of dictionaries)
**Testing**: pytest for unit tests (test file separate from main code)
**Target Platform**: Cross-platform (Windows, macOS, Linux) - any system with Python 3.13+
**Project Type**: Single file CLI application
**Performance Goals**: Handle 100+ tasks without noticeable latency (<100ms per operation)
**Constraints**:
  - Single file implementation (main logic in one file)
  - No OOP (procedural functions only)
  - No external dependencies (stdlib only)
  - In-memory storage (data lost on exit)
**Scale/Scope**: Single-user, single-session, 100+ tasks capacity

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Principle I: Spec-Driven Workflow ✅
- Plan follows spec.md requirements exactly
- All design decisions will be documented here
- Tasks.md will break down implementation steps

### Principle II: Clean Code Standards ✅
- PEP 8 compliance required
- Type hints for all functions
- Docstrings for all functions (Google style)
- Descriptive function/variable names
- Single responsibility per function

### Principle III: Modular Design for Extensibility ✅
- Functions grouped by concern (UI, business logic, data operations)
- Clear separation even within single file:
  - Data operations (add_task, delete_task, etc.)
  - Business logic (validate_input, generate_id, etc.)
  - UI layer (display_menu, get_user_input, print_tasks, etc.)
- Future enhancement path: easy to split into modules if needed

### Principle IV: User-Centric Interface Design ✅
- Clear menu with numbered options
- Descriptive prompts for all inputs
- Confirmation for delete operations
- Error messages with actionable guidance
- Never crash - return to main menu on errors

### Principle V: Quality Assurance Through Testing ✅
- Unit tests for all core functions (separate test file)
- Edge case coverage (empty inputs, invalid IDs, etc.)
- Test isolation (each test independent)
- Target: 80%+ coverage for business logic

### Principle VI: Version Control Discipline ✅
- Atomic commit after implementation
- Conventional commit format
- Feature branch: 001-todo-core-features

### Principle VII: Development Constraints ✅
- No manual coding (Claude Code implements)
- No secrets/credentials (N/A for this feature)
- No commented-out code in final version
- No linter/type checker errors

### Principle VIII: Error Handling & Resilience ✅
- Explicit error messages for invalid operations
- Input validation before processing
- Graceful handling of edge cases
- Errors logged to console with context

### Principle IX: Security & Data Integrity ✅
- Input validation (empty strings, invalid IDs)
- No injection vulnerabilities (N/A - no external systems)
- Data integrity maintained (unique IDs, consistent state)

### Principle X: Performance & Efficiency ✅
- Linear search acceptable for 100 tasks (O(n) is fine)
- No premature optimization
- Simple data structure (list of dicts) sufficient

### Principle XI: Observability & Logging ✅
- Console output for all operations
- Clear success/error messages
- Operation confirmations visible to user

**Constitution Check Result**: ✅ PASS - All principles satisfied

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-core-features/
├── spec.md              # Feature specification
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (design decisions)
├── data-model.md        # Phase 1 output (data structure)
├── quickstart.md        # Phase 1 output (how to run)
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── data.py              # Global data storage (tasks list, next_id counter)
└── todo.py              # All application logic and functions

tests/
└── test_todo.py         # Unit tests for todo.py functions

pyproject.toml           # UV project configuration
README.md                # Setup and usage instructions
CLAUDE.md                # Agent development instructions
```

**Structure Decision**: **Two-file implementation** with data separation.

- `src/data.py`: Contains only global variables (tasks list, next_id counter)
- `src/todo.py`: Contains all functions organized in sections:

1. **Data Operations Section**: Functions that manipulate the task list
2. **Business Logic Section**: Validation, ID generation, helper functions
3. **UI Section**: Menu display, user input, output formatting
4. **Main Section**: Application entry point with main loop

This structure satisfies:
- User requirement: Data in separate file (requested change from single-file approach)
- Constitutional separation of concerns (data vs logic separation)
- Easy to understand and maintain
- Clean separation makes testing easier
- Straightforward to enhance later (can add persistence to data.py in Phase II)

## Complexity Tracking

No constitutional violations - all principles satisfied with simple design.

---

## Phase 0: Research & Design Decisions

### Research Questions

1. **Data Structure**: What's the simplest way to store tasks in memory?
2. **ID Generation**: How to ensure unique task IDs?
3. **Menu Flow**: Best UX pattern for console menu?
4. **Input Validation**: Where and how to validate user inputs?
5. **Error Handling**: How to handle errors without crashing?

### Design Decisions

#### Decision 1: Data Structure

**Chosen**: List of dictionaries

```python
tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, eggs, bread',
        'completed': False
    },
    # ... more tasks
]
```

**Rationale**:
- Simple, no OOP required
- Direct dict access for task properties
- Easy to iterate, filter, and modify
- Familiar to all Python developers
- Sufficient for 100+ tasks (performance acceptable)

**Alternatives Considered**:
- NamedTuple: Requires defining types, more complex
- Dataclass: Violates "no OOP" requirement
- Separate lists for each field: Complex synchronization, error-prone

#### Decision 2: ID Generation Strategy

**Chosen**: Auto-incrementing counter (global variable)

```python
next_id = 1  # Global counter

def generate_task_id() -> int:
    global next_id
    task_id = next_id
    next_id += 1
    return task_id
```

**Rationale**:
- Simple, predictable IDs (1, 2, 3, ...)
- No collisions possible
- Easy for users to reference tasks
- Meets requirement: "sequential numeric IDs starting from 1"

**Alternatives Considered**:
- UUID: Overkill for in-memory app, hard to type
- Hash-based: Unpredictable, unnecessary complexity
- Max ID + 1: Works but slightly more complex

#### Decision 3: Menu Flow Pattern

**Chosen**: Infinite loop with numbered menu + exit option

```python
def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            add_task_flow()
        elif choice == '2':
            view_tasks_flow()
        # ... other options
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```

**Rationale**:
- Familiar pattern (most CLI apps use this)
- Easy to understand control flow
- User stays in menu until explicit exit
- Error-safe (invalid choices loop back)

**Alternatives Considered**:
- State machine: Overly complex for simple menu
- Recursive calls: Risk stack overflow, harder to reason about

#### Decision 4: Input Validation Strategy

**Chosen**: Validate at input point, show errors immediately

```python
def get_non_empty_input(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please try again.")

def get_task_id() -> int | None:
    try:
        task_id = int(input("Enter task ID: "))
        if task_id <= 0:
            print("Error: ID must be positive.")
            return None
        return task_id
    except ValueError:
        print("Error: Please enter a valid number.")
        return None
```

**Rationale**:
- Immediate feedback to user
- Prevents invalid data from entering system
- Clear error messages with guidance
- Graceful handling (no crashes)

**Alternatives Considered**:
- Validate after collection: Delayed feedback, poor UX
- Exception-based: Harder to reason about control flow

#### Decision 5: Error Handling Pattern

**Chosen**: Return None for errors, check before using

```python
def find_task_by_id(task_id: int) -> dict | None:
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

# Usage:
task = find_task_by_id(task_id)
if task is None:
    print(f"Error: Task {task_id} not found.")
    return
# ... proceed with task
```

**Rationale**:
- Explicit error handling (no hidden exceptions)
- Easy to read and understand
- Prevents crashes
- Aligns with procedural style

**Alternatives Considered**:
- Exceptions: More complex, harder to predict flow
- Sentinel values (-1): Less clear than None

---

## Phase 1: Data Model & Contracts

### Data Model

#### Task Entity

**Structure**:
```python
{
    'id': int,           # Unique identifier (auto-generated, sequential)
    'title': str,        # Task title (required, non-empty)
    'description': str,  # Task details (optional, can be empty string)
    'completed': bool    # Completion status (default: False)
}
```

**Constraints**:
- `id`: Must be unique, positive integer, auto-generated
- `title`: Required, cannot be empty or whitespace-only
- `description`: Optional, defaults to empty string if not provided
- `completed`: Boolean only, defaults to False

**State Transitions**:
- New task: `completed = False`
- Mark complete: `completed = True`
- Mark incomplete: `completed = False`
- Update: `completed` unchanged unless explicitly toggled
- Delete: Task removed from list entirely

### Function Contracts

#### Data Operations

```python
def add_task(title: str, description: str = "") -> dict:
    """
    Create new task and add to task list.

    Args:
        title: Task title (required, non-empty)
        description: Task details (optional)

    Returns:
        dict: The created task

    Raises:
        ValueError: If title is empty or whitespace-only
    """

def delete_task(task_id: int) -> bool:
    """
    Remove task from task list by ID.

    Args:
        task_id: Unique task identifier

    Returns:
        bool: True if deleted, False if not found
    """

def update_task(task_id: int, title: str = None, description: str = None) -> bool:
    """
    Update task title and/or description.

    Args:
        task_id: Unique task identifier
        title: New title (optional)
        description: New description (optional)

    Returns:
        bool: True if updated, False if not found

    Raises:
        ValueError: If title provided but empty
    """

def toggle_task_completion(task_id: int) -> bool:
    """
    Toggle task completion status.

    Args:
        task_id: Unique task identifier

    Returns:
        bool: True if toggled, False if not found
    """

def get_all_tasks() -> list[dict]:
    """
    Get all tasks.

    Returns:
        list[dict]: List of all tasks (empty list if none)
    """

def find_task_by_id(task_id: int) -> dict | None:
    """
    Find task by ID.

    Args:
        task_id: Unique task identifier

    Returns:
        dict | None: Task if found, None otherwise
    """
```

#### Business Logic

```python
def generate_task_id() -> int:
    """
    Generate unique sequential task ID.

    Returns:
        int: Next available task ID
    """

def validate_title(title: str) -> bool:
    """
    Check if title is valid (non-empty, not whitespace-only).

    Args:
        title: Title to validate

    Returns:
        bool: True if valid, False otherwise
    """
```

#### UI Functions

```python
def display_menu() -> None:
    """Display main menu options."""

def get_user_choice() -> str:
    """
    Get user menu choice.

    Returns:
        str: User's choice (raw input)
    """

def print_tasks(tasks: list[dict]) -> None:
    """
    Display all tasks in formatted list.

    Args:
        tasks: List of tasks to display
    """

def add_task_flow() -> None:
    """Execute add task workflow (prompt, validate, add, confirm)."""

def view_tasks_flow() -> None:
    """Execute view tasks workflow (fetch, display)."""

def update_task_flow() -> None:
    """Execute update task workflow (prompt ID, prompt changes, update, confirm)."""

def delete_task_flow() -> None:
    """Execute delete task workflow (prompt ID, confirm, delete)."""

def toggle_completion_flow() -> None:
    """Execute toggle completion workflow (prompt ID, toggle, confirm)."""
```

### Quickstart Guide

**File**: `quickstart.md`

```markdown
# Todo App Quick Start

## Prerequisites
- Python 3.13 or higher
- UV package manager

## Installation

1. Clone repository:
   ```bash
   git clone <repo-url>
   cd Todo-app
   ```

2. Install dependencies (currently none, stdlib only):
   ```bash
   uv sync
   ```

## Running the Application

```bash
python src/todo.py
```

## Usage

### Main Menu
The application presents a menu with 6 options:

1. **Add Task**: Create a new task
2. **View All Tasks**: Display all tasks with status
3. **Update Task**: Modify task title/description
4. **Delete Task**: Remove a task
5. **Toggle Completion**: Mark task complete/incomplete
6. **Exit**: Close the application

### Example Session

```
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

Choose an option (1-6): 2

=== All Tasks ===
[1] Buy groceries
    Description: Milk, eggs, bread
    Status: ☐ Incomplete

Total tasks: 1

Choose an option (1-6): 5

Enter task ID to toggle: 1

✓ Task marked as complete!

Choose an option (1-6): 6

Goodbye!
```

## Testing

Run tests:
```bash
pytest tests/test_todo.py -v
```

## Troubleshooting

**Problem**: "python: command not found"
**Solution**: Ensure Python 3.13+ is installed and in PATH

**Problem**: Tasks disappear after closing app
**Solution**: This is expected behavior - Phase I uses in-memory storage only
```

---

## Architecture Decisions

### ADR-001: Two-File Procedural Implementation with Data Separation

**Status**: Accepted (Updated)

**Context**: User requested "not using oop" and later requested "store data in separate file". Constitution requires separation of concerns and extensibility.

**Decision**: Implement application in two files using procedural programming:
- `src/data.py`: Global variables only (tasks list, next_id counter)
- `src/todo.py`: All functions (data operations, business logic, UI) with imports from data.py

**Consequences**:
- ✅ Clear data/logic separation
- ✅ Easy to understand (data in one place, functions in another)
- ✅ Simple imports (from data import tasks, next_id)
- ✅ Easier testing (can reset data module between tests)
- ✅ Constitutional separation of concerns
- ✅ Easy migration path: data.py can become persistence layer in Phase II
- ✅ Still procedural (no OOP)
- ⚠️ Two files instead of one (user-requested tradeoff)

**Alternatives Rejected**:
- OOP with classes: Violates user requirement
- Single file: User requested data separation
- Multi-module structure: Too complex for Phase I
- Mixed approach (some OOP): Inconsistent, confusing

### ADR-002: List of Dictionaries for Storage

**Status**: Accepted

**Context**: Need simple in-memory storage for tasks without OOP.

**Decision**: Use Python list containing task dictionaries with global task list variable.

**Consequences**:
- ✅ Simple, no OOP required
- ✅ Built-in Python, no dependencies
- ✅ Easy CRUD operations
- ✅ Adequate performance for 100+ tasks
- ✅ Easy to test
- ⚠️ Global state (acceptable for single-file app)

**Alternatives Rejected**:
- SQLite: Overkill, violates "in-memory" constraint
- Dataclasses: Requires OOP
- NamedTuples: More complex, less flexible

### ADR-003: Menu-Driven CLI Pattern

**Status**: Accepted

**Context**: Console application needs intuitive user interface.

**Decision**: Infinite loop with numbered menu, separate flow functions for each operation.

**Consequences**:
- ✅ Familiar UX pattern
- ✅ Clear control flow
- ✅ Easy error recovery
- ✅ Testable (each flow function isolated)
- ✅ Graceful exit mechanism

**Alternatives Rejected**:
- Command-line arguments: Less interactive, steeper learning curve
- REPL-style: More complex parsing
- State machine: Overengineered for simple menu

---

## Implementation Phases

### Phase 0: Setup ✅
- [x] Create plan.md (this file)
- [x] Document design decisions (research.md equivalent inline)
- [x] Define data model
- [x] Define function contracts

### Phase 1: Core Data Operations (tasks.md will detail)
- [ ] Implement task storage (list + next_id counter)
- [ ] Implement add_task()
- [ ] Implement find_task_by_id()
- [ ] Implement get_all_tasks()
- [ ] Implement delete_task()
- [ ] Implement update_task()
- [ ] Implement toggle_task_completion()

### Phase 2: Business Logic (tasks.md will detail)
- [ ] Implement generate_task_id()
- [ ] Implement validate_title()

### Phase 3: UI Functions (tasks.md will detail)
- [ ] Implement display_menu()
- [ ] Implement print_tasks()
- [ ] Implement add_task_flow()
- [ ] Implement view_tasks_flow()
- [ ] Implement update_task_flow()
- [ ] Implement delete_task_flow()
- [ ] Implement toggle_completion_flow()
- [ ] Implement main() loop

### Phase 4: Testing (tasks.md will detail)
- [ ] Unit tests for data operations
- [ ] Unit tests for business logic
- [ ] Integration tests for flows
- [ ] Edge case tests

### Phase 5: Documentation (tasks.md will detail)
- [ ] Add docstrings to all functions
- [ ] Create README.md
- [ ] Update CLAUDE.md
- [ ] Type hints verification

---

## Next Steps

1. Run `/sp.tasks` to generate detailed implementation tasks from this plan
2. Implement tasks sequentially by phase
3. Run tests after each phase
4. Review against constitutional principles
5. Create commit after successful implementation

---

## Notes

- **Simplicity First**: Design prioritizes clarity over patterns
- **No Premature Optimization**: Linear search acceptable for spec'd scale
- **Constitutional Compliance**: All principles satisfied despite simple design
- **Extension Path**: data.py can add persistence in Phase II (JSON/SQLite) without changing todo.py
- **User Requirements Met**: Data in separate file ✅, no OOP ✅, simple & understandable ✅
