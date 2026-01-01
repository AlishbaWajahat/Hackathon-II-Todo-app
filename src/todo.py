"""
Enhanced Todo List Manager with Rich UI and Interactive Selection

A command-line todo list application with:
- Arrow key navigation for all selections
- Visual task toggling
- Rich formatting and styling
- Reused task IDs after deletion
- Interactive selection for all operations

Author: Todo App Team
Date: 2026-01-02
Version: 2.0.0 (Enhanced)
"""

import inquirer
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table

from data import next_id, tasks

# ==============================================================================
# BUSINESS LOGIC FUNCTIONS
# ==============================================================================

def generate_task_id() -> int:
    """
    Generate a unique task ID, reusing deleted IDs when possible.

    Instead of always incrementing, this function finds the smallest
    available ID to reuse after deletion.

    Returns:
        int: A unique positive integer ID for a new task
    """
    global next_id

    # Find the smallest available ID
    used_ids = {task['id'] for task in tasks}
    current = 1
    while current in used_ids:
        current += 1

    # Update next_id if we're setting a new maximum
    if current >= next_id:
        next_id = current + 1

    return current


def validate_title(title: str) -> bool:
    """
    Validate that a task title is non-empty after stripping whitespace.

    A valid title must:
    - Not be None
    - Not be an empty string after strip()
    - Contain at least one non-whitespace character

    Args:
        title: The title string to validate

    Returns:
        bool: True if the title is valid, False otherwise

    Examples:
        >>> validate_title("Buy groceries")
        True
        >>> validate_title("   ")
        False
        >>> validate_title("")
        False
    """
    if title is None:
        return False
    if title.strip() == "":
        return False
    return True


def find_task_by_id(task_id: int) -> dict | None:
    """
    Find a task by its unique ID.

    Performs a linear search through the tasks list to find a task
    with the matching ID.

    Args:
        task_id: The unique ID of the task to find

    Returns:
        dict | None: The task dictionary if found, None otherwise

    Examples:
        >>> task = find_task_by_id(1)
        >>> task['title'] if task else "Not found"
        'Buy groceries'
        >>> find_task_by_id(999)
        None
    """
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None


# ==============================================================================
# DATA OPERATIONS
# ==============================================================================

def add_task(title: str, description: str = "") -> dict:
    """
    Create and add a new task to the task list.

    Generates a unique ID for the task and adds it to the global tasks list
    with the provided title and description. The task is initially marked
    as incomplete.

    Args:
        title: The task title (should be validated before calling)
        description: Optional task description (defaults to empty string)

    Returns:
        dict: The newly created task dictionary

    Examples:
        >>> task = add_task("Buy groceries", "Milk, eggs, bread")
        >>> task['title']
        'Buy groceries'
        >>> task['completed']
        False
    """
    new_task = {
        'id': generate_task_id(),
        'title': title.strip(),
        'description': description,
        'completed': False
    }
    tasks.append(new_task)
    return new_task


def get_all_tasks() -> list[dict]:
    """
    Retrieve all tasks from the task list.

    Returns:
        list[dict]: A list of all task dictionaries

    Examples:
        >>> all_tasks = get_all_tasks()
        >>> len(all_tasks)
        3
    """
    return tasks


def toggle_task_completion(task_id: int) -> bool:
    """
    Toggle the completion status of a task.

    Changes the task's completed status from True to False or False to True.

    Args:
        task_id: The unique ID of the task to toggle

    Returns:
        bool: True if task was found and toggled, False if task not found

    Examples:
        >>> toggle_task_completion(1)
        True
        >>> task = find_task_by_id(1)
        >>> task['completed']
        True
    """
    task = find_task_by_id(task_id)
    if task:
        task['completed'] = not task['completed']
        return True
    return False


def update_task(task_id: int, title: str | None = None, description: str | None = None) -> bool:
    """
    Update a task's title and/or description.

    Updates the specified fields of a task. If a field is None, it remains unchanged.

    Args:
        task_id: The unique ID of the task to update
        title: New title (None to keep current)
        description: New description (None to keep current)

    Returns:
        bool: True if task was found and updated, False if task not found

    Examples:
        >>> update_task(1, title="New title")
        True
        >>> update_task(1, description="New description")
        True
        >>> update_task(999)
        False
    """
    task = find_task_by_id(task_id)
    if not task:
        return False

    if title is not None:
        task['title'] = title.strip()
    if description is not None:
        task['description'] = description

    return True


def delete_task(task_id: int) -> bool:
    """
    Delete a task from the task list.

    Removes the task with the specified ID from the global tasks list.

    Args:
        task_id: The unique ID of the task to delete

    Returns:
        bool: True if task was found and deleted, False if task not found

    Examples:
        >>> delete_task(1)
        True
        >>> delete_task(999)
        False
    """
    task = find_task_by_id(task_id)
    if not task:
        return False

    tasks.remove(task)
    return True


# ==============================================================================
# UI FUNCTIONS
# ==============================================================================

def print_tasks(task_list: list[dict]) -> None:
    """
    Display tasks in a formatted rich table with status indicators.

    Args:
        task_list: List of task dictionaries to display
    """
    console = Console()

    if not task_list:
        console.print(Panel("[yellow]No tasks found. Add your first task to get started![/yellow]",
                           title="Info"))
        return

    table = Table(title="Todo List", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=5)
    table.add_column("Status", width=10)
    table.add_column("Title", width=30)
    table.add_column("Description", width=40)

    for task in task_list:
        status_tag = "C COMPLETE" if task['completed'] else "I INCOMPLETE"
        status_style = "green" if task['completed'] else "red"
        title_style = "strike" if task['completed'] else "normal"

        table.add_row(
            str(task['id']),
            f"[{status_style}]{status_tag}[/{status_style}]",
            f"[{title_style}]{task['title']}[/{title_style}]",
            task['description']
        )

    console.print(table)
    console.print(f"\n[yellow]Total tasks: {len(task_list)}[/yellow]")


def add_task_flow() -> None:
    """
    Interactive flow for adding a new task with rich formatting.
    """
    console = Console()
    console.print(Panel("Add New Task", style="bold blue"))

    title = Prompt.ask("Enter task title")

    if not validate_title(title):
        console.print(Panel("[red]Error: Task title cannot be empty[/red]",
                           title="Validation Error"))
        return

    description = Prompt.ask("Enter task description (optional)", default="")

    task = add_task(title, description)
    console.print(Panel(f"[green]✓ Task created successfully![/green] (ID: {task['id']})",
                       title="Success"))


def view_tasks_flow() -> None:
    """
    Interactive flow for viewing all tasks with rich formatting.
    """
    console = Console()
    console.print(Panel("All Tasks", style="bold blue"))
    all_tasks = get_all_tasks()
    print_tasks(all_tasks)


def select_task_interactive(operation: str) -> dict | None:
    """
    Interactive task selection using arrow keys.

    Args:
        operation: The operation being performed (for display purposes)

    Returns:
        Optional[Dict]: The selected task or None if cancelled
    """
    console = Console()

    if not tasks:
        console.print(Panel("[red]No tasks available![/red]", title="Error"))
        return None

    # Create choices for the selection with visual status tags
    choices = []
    for task in tasks:
        if task['completed']:
            status_tag = "COMPLETE"
        else:
            status_tag = "INCOMPLETE"
        choice_text = f"[{task['id']}] {task['title']} [{status_tag}]"
        choices.append(choice_text)

    choices.append("Cancel")

    questions = [
        inquirer.List('task',
                     message=f"Select task to {operation}",
                     choices=choices,
                     carousel=True)
    ]

    answers = inquirer.prompt(questions)

    if not answers or answers['task'] == "Cancel":
        return None

    # Extract task ID from the selection
    selected_text = answers['task']
    task_id = int(selected_text.split(']')[0][1:])  # Extract ID from "[ID] ..."

    return find_task_by_id(task_id)


def toggle_completion_flow() -> None:
    """
    Interactive flow for toggling task completion status with visual selection.
    """
    console = Console()
    console.print(Panel("Toggle Task Completion", style="bold blue"))

    selected_task = select_task_interactive("toggle")
    if not selected_task:
        console.print(Panel("[yellow]Operation cancelled[/yellow]", title="Info"))
        return

    # Toggle the task completion status
    toggle_result = toggle_task_completion(selected_task['id'])

    if toggle_result:
        status_after = "completed" if selected_task['completed'] else "incomplete"
        console.print(Panel(f"[green]✓ Task marked as {status_after}![/green]",
                           title="Success"))
    else:
        console.print(Panel("[red]Error: Failed to toggle task[/red]", title="Error"))


def update_task_flow() -> None:
    """
    Interactive flow for updating task details with arrow key selection.
    """
    console = Console()
    console.print(Panel("Update Task", style="bold blue"))

    selected_task = select_task_interactive("update")
    if not selected_task:
        console.print(Panel("[yellow]Operation cancelled[/yellow]", title="Info"))
        return

    # Show current values and prompt for new ones
    console.print(f"[blue]Current title:[/blue] {selected_task['title']}")
    new_title = Prompt.ask("Enter new title (press Enter to keep current)",
                          default=selected_task['title'])

    console.print(f"[blue]Current description:[/blue] {selected_task['description']}")
    new_description = Prompt.ask("Enter new description (press Enter to keep current)",
                                default=selected_task['description'])

    # Validate and update
    if new_title != selected_task['title']:
        if not validate_title(new_title):
            console.print(Panel("[red]Error: Task title cannot be empty[/red]",
                               title="Validation Error"))
            return
        update_task(selected_task['id'], title=new_title)

    if new_description != selected_task['description']:
        update_task(selected_task['id'], description=new_description)

    console.print(Panel("[green]✓ Task updated successfully![/green]", title="Success"))


def delete_task_flow() -> None:
    """
    Interactive flow for deleting a task with arrow key selection and confirmation.
    """
    console = Console()
    console.print(Panel("Delete Task", style="bold blue"))

    selected_task = select_task_interactive("delete")
    if not selected_task:
        console.print(Panel("[yellow]Operation cancelled[/yellow]", title="Info"))
        return

    # Show task details before deletion
    status = "✅ Complete" if selected_task['completed'] else "❌ Incomplete"
    table = Table(title="Task Details", show_header=False)
    table.add_column("Field", style="bold")
    table.add_column("Value")
    table.add_row("ID", str(selected_task['id']))
    table.add_row("Title", selected_task['title'])
    table.add_row("Description", selected_task['description'])
    table.add_row("Status", status)

    console.print(table)

    # Confirmation prompt
    confirmation = Confirm.ask("Are you sure you want to delete this task?")

    if confirmation:
        delete_task(selected_task['id'])
        console.print(Panel("[green]✓ Task deleted successfully![/green]", title="Success"))
    else:
        console.print(Panel("[yellow]Deletion cancelled[/yellow]", title="Info"))


# ==============================================================================
# MAIN MENU AND APPLICATION LOOP
# ==============================================================================

def display_menu() -> None:
    """
    Display the main menu with rich formatting and styling.
    """
    console = Console()
    console.print(Panel(
        "[bold blue]Todo List Manager[/bold blue]\n\n"
        "[1] Add Task\n"
        "[2] View All Tasks\n"
        "[3] Update Task\n"
        "[4] Delete Task\n"
        "[5] Toggle Task Completion\n"
        "[6] Exit",
        title="Main Menu",
        expand=False
    ))


def get_user_choice() -> str:
    """
    Get user's menu selection using interactive selection with arrow keys.

    Returns:
        str: The user's choice as a string ('1'-'6')
    """
    choices = [
        "Add Task",
        "View All Tasks",
        "Update Task",
        "Delete Task",
        "Toggle Task Completion",
        "Exit"
    ]

    questions = [
        inquirer.List('choice',
                     message="Choose an option",
                     choices=choices,
                     carousel=True)
    ]

    answers = inquirer.prompt(questions)

    if not answers:
        return '6'  # Default to exit if cancelled

    choice_map = {
        "Add Task": '1',
        "View All Tasks": '2',
        "Update Task": '3',
        "Delete Task": '4',
        "Toggle Task Completion": '5',
        "Exit": '6'
    }

    return choice_map.get(answers['choice'], '6')


def main() -> None:
    """
    Enhanced main application loop with rich formatting and interactive selection.
    """
    console = Console()
    console.print("[bold green]Welcome to the Enhanced Todo List Manager![/bold green]")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            add_task_flow()
        elif choice == '2':
            view_tasks_flow()
        elif choice == '3':
            update_task_flow()
        elif choice == '4':
            delete_task_flow()
        elif choice == '5':
            toggle_completion_flow()
        elif choice == '6':
            console.print("[bold green]\nGoodbye![/bold green]")
            break
        else:
            console.print(Panel("[red]Invalid choice. Please try again.[/red]", title="Error"))

        # Pause to let user see results before showing menu again
        if choice != '6':
            console.print("\n[bold]Press Enter to continue...[/bold]", end="")
            input()


if __name__ == "__main__":
    main()
