"""
Unit tests for the Todo application.

Tests all core functionality including task creation, retrieval, update,
deletion, and completion toggling.
"""

import sys
from pathlib import Path

# Add src directory to path so we can import modules
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
import data
import todo


@pytest.fixture(autouse=True)
def reset_tasks():
    """
    Reset global state before each test.

    This fixture automatically runs before every test to ensure
    clean state and avoid test interdependencies.
    """
    data.tasks.clear()
    data.next_id = 1
    yield
    data.tasks.clear()
    data.next_id = 1


# ==============================================================================
# BUSINESS LOGIC TESTS
# ==============================================================================

def test_generate_task_id():
    """Test that task IDs are generated correctly through add_task function."""
    # Reset data for this specific test
    data.tasks.clear()
    data.next_id = 1

    # Test initial sequential generation through add_task
    task1 = todo.add_task("Task 1", "Description 1")
    task2 = todo.add_task("Task 2", "Description 2")
    task3 = todo.add_task("Task 3", "Description 3")

    assert task1['id'] == 1
    assert task2['id'] == 2
    assert task3['id'] == 3


def test_id_reuse_after_deletion():
    """Test that task IDs are reused after deletion."""
    # Reset data for this specific test
    data.tasks.clear()
    data.next_id = 1

    # Add some tasks
    task1 = todo.add_task("Task 1", "Description 1")
    task2 = todo.add_task("Task 2", "Description 2")
    assert task1['id'] == 1
    assert task2['id'] == 2

    # Delete first task
    result = todo.delete_task(1)
    assert result is True

    # Next task should reuse ID 1
    task3 = todo.add_task("Task 3", "Description 3")
    assert task3['id'] == 1


def test_validate_title():
    """Test title validation with valid and invalid cases."""
    # Valid titles
    assert todo.validate_title("Buy groceries") is True
    assert todo.validate_title("   Task with spaces   ") is True
    assert todo.validate_title("A") is True

    # Invalid titles
    assert todo.validate_title("") is False
    assert todo.validate_title("   ") is False
    assert todo.validate_title("  \t\n  ") is False
    assert todo.validate_title(None) is False


def test_find_task_by_id():
    """Test finding tasks by ID with found and not-found cases."""
    # Add test tasks
    todo.add_task("Task 1", "Description 1")
    todo.add_task("Task 2", "Description 2")

    # Found cases
    task = todo.find_task_by_id(1)
    assert task is not None
    assert task['id'] == 1
    assert task['title'] == "Task 1"

    task = todo.find_task_by_id(2)
    assert task is not None
    assert task['id'] == 2
    assert task['title'] == "Task 2"

    # Not found cases
    assert todo.find_task_by_id(999) is None
    assert todo.find_task_by_id(0) is None
    assert todo.find_task_by_id(-1) is None


# ==============================================================================
# DATA OPERATION TESTS
# ==============================================================================

def test_add_task():
    """Test task creation and verify task structure."""
    # Add task with description
    task = todo.add_task("Buy milk", "From the store")
    assert task['id'] == 1
    assert task['title'] == "Buy milk"
    assert task['description'] == "From the store"
    assert task['completed'] is False

    # Add task without description
    task2 = todo.add_task("Call mom")
    assert task2['id'] == 2
    assert task2['title'] == "Call mom"
    assert task2['description'] == ""
    assert task2['completed'] is False

    # Verify tasks are in the global list
    assert len(data.tasks) == 2


def test_get_all_tasks():
    """Test retrieving all tasks with empty and non-empty lists."""
    # Empty list
    assert todo.get_all_tasks() == []

    # Add tasks
    todo.add_task("Task 1", "Desc 1")
    todo.add_task("Task 2", "Desc 2")
    todo.add_task("Task 3", "Desc 3")

    # Non-empty list
    all_tasks = todo.get_all_tasks()
    assert len(all_tasks) == 3
    assert all_tasks[0]['title'] == "Task 1"
    assert all_tasks[1]['title'] == "Task 2"
    assert all_tasks[2]['title'] == "Task 3"


def test_update_task():
    """Test updating task title and description."""
    # Create initial task
    todo.add_task("Original Title", "Original Description")

    # Update title only
    result = todo.update_task(1, title="New Title")
    assert result is True
    task = todo.find_task_by_id(1)
    assert task['title'] == "New Title"
    assert task['description'] == "Original Description"

    # Update description only
    result = todo.update_task(1, description="New Description")
    assert result is True
    task = todo.find_task_by_id(1)
    assert task['title'] == "New Title"
    assert task['description'] == "New Description"

    # Update both
    result = todo.update_task(1, title="Final Title", description="Final Description")
    assert result is True
    task = todo.find_task_by_id(1)
    assert task['title'] == "Final Title"
    assert task['description'] == "Final Description"

    # Update non-existent task
    result = todo.update_task(999, title="Should Fail")
    assert result is False


def test_delete_task():
    """Test task deletion."""
    # Add tasks
    todo.add_task("Task 1", "Desc 1")
    todo.add_task("Task 2", "Desc 2")
    todo.add_task("Task 3", "Desc 3")
    assert len(data.tasks) == 3

    # Delete middle task
    result = todo.delete_task(2)
    assert result is True
    assert len(data.tasks) == 2
    assert todo.find_task_by_id(2) is None
    assert todo.find_task_by_id(1) is not None
    assert todo.find_task_by_id(3) is not None

    # Try to delete non-existent task
    result = todo.delete_task(999)
    assert result is False
    assert len(data.tasks) == 2


def test_toggle_task_completion():
    """Test toggling task completion status."""
    # Create task (default: incomplete)
    todo.add_task("Test Task", "Test Description")
    task = todo.find_task_by_id(1)
    assert task['completed'] is False

    # Toggle to complete
    result = todo.toggle_task_completion(1)
    assert result is True
    assert task['completed'] is True

    # Toggle back to incomplete
    result = todo.toggle_task_completion(1)
    assert result is True
    assert task['completed'] is False

    # Toggle non-existent task
    result = todo.toggle_task_completion(999)
    assert result is False


# ==============================================================================
# EDGE CASE TESTS
# ==============================================================================

def test_add_task_edge_cases():
    """Test task creation with edge cases."""
    # Task with whitespace in title (should be stripped)
    task = todo.add_task("   Task with spaces   ", "Description")
    assert task['title'] == "Task with spaces"

    # Task with long title
    long_title = "A" * 1000
    task = todo.add_task(long_title, "")
    assert task['title'] == long_title
    assert len(task['title']) == 1000

    # Task with special characters
    task = todo.add_task("Buy groceries 🛒", "Milk, eggs, bread 🥛🥚🍞")
    assert task['title'] == "Buy groceries 🛒"
    assert task['description'] == "Milk, eggs, bread 🥛🥚🍞"

    # Task with empty description
    task = todo.add_task("Task", "")
    assert task['description'] == ""


def test_invalid_task_id_operations():
    """Test operations with invalid task IDs."""
    # Create one task
    todo.add_task("Valid Task", "Description")

    # Update with invalid IDs
    assert todo.update_task(0, title="Should Fail") is False
    assert todo.update_task(-1, title="Should Fail") is False
    assert todo.update_task(999, title="Should Fail") is False

    # Delete with invalid IDs
    assert todo.delete_task(0) is False
    assert todo.delete_task(-1) is False
    assert todo.delete_task(999) is False

    # Toggle with invalid IDs
    assert todo.toggle_task_completion(0) is False
    assert todo.toggle_task_completion(-1) is False
    assert todo.toggle_task_completion(999) is False

    # Verify original task is unchanged
    task = todo.find_task_by_id(1)
    assert task is not None
    assert task['title'] == "Valid Task"


# ==============================================================================
# INTEGRATION TESTS
# ==============================================================================

def test_full_task_lifecycle():
    """Test complete task lifecycle: create, view, update, toggle, delete."""
    # Create
    task = todo.add_task("Complete project", "Finish by Friday")
    assert task['id'] == 1
    assert task['completed'] is False

    # View/Find
    found_task = todo.find_task_by_id(1)
    assert found_task == task

    # Update
    todo.update_task(1, title="Complete project (URGENT)", description="Finish by Thursday")
    updated_task = todo.find_task_by_id(1)
    assert updated_task['title'] == "Complete project (URGENT)"
    assert updated_task['description'] == "Finish by Thursday"

    # Toggle completion
    todo.toggle_task_completion(1)
    assert updated_task['completed'] is True

    # Delete
    todo.delete_task(1)
    assert todo.find_task_by_id(1) is None
    assert len(data.tasks) == 0


def test_multiple_tasks_independence():
    """Test that operations on one task don't affect others."""
    # Create multiple tasks
    todo.add_task("Task 1", "Desc 1")
    todo.add_task("Task 2", "Desc 2")
    todo.add_task("Task 3", "Desc 3")

    # Update task 2
    todo.update_task(2, title="Updated Task 2")

    # Verify others unchanged
    task1 = todo.find_task_by_id(1)
    task3 = todo.find_task_by_id(3)
    assert task1['title'] == "Task 1"
    assert task3['title'] == "Task 3"

    # Toggle task 1
    todo.toggle_task_completion(1)

    # Verify others unchanged
    task2 = todo.find_task_by_id(2)
    task3 = todo.find_task_by_id(3)
    assert task2['completed'] is False
    assert task3['completed'] is False

    # Delete task 3
    todo.delete_task(3)

    # Verify others still exist
    assert len(data.tasks) == 2
    assert todo.find_task_by_id(1) is not None
    assert todo.find_task_by_id(2) is not None
