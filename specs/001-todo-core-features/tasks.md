# Tasks: Todo Core Features

**Input**: Design documents from `/specs/001-todo-core-features/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Files:
  - `src/data.py` (global data storage: tasks list, next_id counter)
  - `src/todo.py` (all application logic and functions)
- Tests: `tests/test_todo.py` (unit tests)

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Initialize project structure and configuration

- [X] T001 Create src directory for application code
- [X] T002 Create tests directory for test files
- [X] T003 [P] Create pyproject.toml with UV configuration for Python 3.13+
- [X] T004 [P] Create .gitignore file with Python-specific exclusions (\_\_pycache\_\_, .pytest_cache, *.pyc)

---

## Phase 2: Foundational (Core Infrastructure)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Create src/data.py with module docstring
- [X] T006 Initialize global task storage list (tasks = []) in src/data.py
- [X] T007 Initialize global next_id counter (starting at 1) in src/data.py
- [X] T008 Create src/todo.py with file header, module docstring, and import from data
- [X] T009 [P] Implement generate_task_id() function in src/todo.py
- [X] T010 [P] Implement validate_title() function in src/todo.py
- [X] T011 [P] Implement find_task_by_id() function in src/todo.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks and view all tasks in a list

**Independent Test**: Add tasks with various titles/descriptions, then view list to confirm all tasks appear with correct details and status indicators

### Implementation for User Story 1

- [X] T012 [P] [US1] Implement add_task(title, description) function in src/todo.py
- [X] T013 [P] [US1] Implement get_all_tasks() function in src/todo.py
- [X] T014 [US1] Implement print_tasks(tasks) function with formatted output in src/todo.py
- [X] T015 [US1] Implement add_task_flow() function (prompt for title/description, validate, add, confirm) in src/todo.py
- [X] T016 [US1] Implement view_tasks_flow() function (fetch all tasks, display with print_tasks) in src/todo.py
- [X] T017 [US1] Add empty list handling to print_tasks() (display "No tasks found" message) in src/todo.py
- [X] T018 [US1] Add status indicator display (☐ Incomplete / ☑ Complete) to print_tasks() in src/todo.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Mark Tasks Complete (Priority: P2)

**Goal**: Enable users to toggle task completion status to track progress

**Independent Test**: Create tasks, mark some complete, verify status changes in task list, toggle between complete/incomplete

### Implementation for User Story 2

- [X] T019 [US2] Implement toggle_task_completion(task_id) function in src/todo.py
- [X] T020 [US2] Implement toggle_completion_flow() function (prompt for ID, find task, toggle, confirm) in src/todo.py
- [X] T021 [US2] Add error handling for invalid task ID in toggle_completion_flow() in src/todo.py
- [X] T022 [US2] Add success message showing new status in toggle_completion_flow() in src/todo.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P3)

**Goal**: Enable users to modify task title and/or description

**Independent Test**: Create task, modify title/description, verify changes reflected in task list while other attributes unchanged

### Implementation for User Story 3

- [X] T023 [US3] Implement update_task(task_id, title, description) function in src/todo.py
- [X] T024 [US3] Implement update_task_flow() function (prompt for ID, show current values, prompt for new values) in src/todo.py
- [X] T025 [US3] Add logic to keep current value if user presses Enter without input in update_task_flow() in src/todo.py
- [X] T026 [US3] Add validation for empty title in update_task_flow() (reject empty, show error) in src/todo.py
- [X] T027 [US3] Add error handling for invalid task ID in update_task_flow() in src/todo.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P4)

**Goal**: Enable users to remove tasks they no longer need

**Independent Test**: Create tasks, delete specific tasks by ID, verify deleted tasks don't appear while others remain intact

### Implementation for User Story 4

- [X] T028 [US4] Implement delete_task(task_id) function in src/todo.py
- [X] T029 [US4] Implement delete_task_flow() function (prompt for ID, find task, show details) in src/todo.py
- [X] T030 [US4] Add confirmation prompt (y/n) to delete_task_flow() before deletion in src/todo.py
- [X] T031 [US4] Add cancellation logic (if user enters 'n') in delete_task_flow() in src/todo.py
- [X] T032 [US4] Add error handling for invalid task ID in delete_task_flow() in src/todo.py
- [X] T033 [US4] Add success message after deletion in delete_task_flow() in src/todo.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Main Menu & Application Loop

**Purpose**: Integrate all user stories into cohesive menu-driven application

- [X] T034 Implement display_menu() function with numbered options (1-6) in src/todo.py
- [X] T035 Implement get_user_choice() function to read menu selection in src/todo.py
- [X] T036 Implement main() function with infinite loop in src/todo.py
- [X] T037 Add menu option 1 (Add Task) routing to add_task_flow() in main() in src/todo.py
- [X] T038 Add menu option 2 (View All Tasks) routing to view_tasks_flow() in main() in src/todo.py
- [X] T039 Add menu option 3 (Update Task) routing to update_task_flow() in main() in src/todo.py
- [X] T040 Add menu option 4 (Delete Task) routing to delete_task_flow() in main() in src/todo.py
- [X] T041 Add menu option 5 (Toggle Completion) routing to toggle_completion_flow() in main() in src/todo.py
- [X] T042 Add menu option 6 (Exit) with goodbye message and break in main() in src/todo.py
- [X] T043 Add invalid choice handling (show error, loop back to menu) in main() in src/todo.py
- [X] T044 Add if \_\_name\_\_ == "\_\_main\_\_": main() entry point to src/todo.py

---

## Phase 8: Testing & Quality Assurance

**Purpose**: Ensure code quality and correctness through comprehensive testing

- [X] T045 Create tests/test_todo.py with pytest imports and test fixtures
- [X] T046 [P] Implement test_generate_task_id() to verify ID increment in tests/test_todo.py
- [X] T047 [P] Implement test_validate_title() with valid/invalid cases in tests/test_todo.py
- [X] T048 [P] Implement test_add_task() to verify task creation in tests/test_todo.py
- [X] T049 [P] Implement test_find_task_by_id() with found/not-found cases in tests/test_todo.py
- [X] T050 [P] Implement test_get_all_tasks() with empty/non-empty lists in tests/test_todo.py
- [X] T051 [P] Implement test_update_task() to verify title/description updates in tests/test_todo.py
- [X] T052 [P] Implement test_delete_task() to verify task removal in tests/test_todo.py
- [X] T053 [P] Implement test_toggle_task_completion() to verify status toggle in tests/test_todo.py
- [X] T054 [P] Implement test_add_task_edge_cases() (empty title, whitespace, long title) in tests/test_todo.py
- [X] T055 [P] Implement test_invalid_task_id_operations() for update/delete/toggle in tests/test_todo.py
- [X] T056 Run pytest with coverage report to verify 80%+ coverage

---

## Phase 9: Documentation & Polish

**Purpose**: Complete project documentation and final code quality checks

- [X] T057 [P] Add comprehensive docstrings (Google style) to all functions in src/todo.py
- [X] T058 [P] Add type hints to all function signatures in src/todo.py
- [X] T059 [P] Create README.md with installation instructions, usage guide, and examples
- [X] T060 [P] Update CLAUDE.md with project status and implementation notes
- [X] T061 Run ruff linter on src/todo.py and src/data.py and fix any issues
- [X] T062 Run mypy type checker on src/todo.py and src/data.py and fix any type errors
- [X] T063 Verify PEP 8 compliance with code formatting check
- [X] T064 Final manual test: Run application and execute all 5 operations successfully

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories (includes data.py creation)
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Main Menu (Phase 7)**: Depends on all desired user stories being complete
- **Testing (Phase 8)**: Can start after each function is implemented (incremental)
- **Documentation (Phase 9)**: Depends on implementation completion

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories, uses data.py
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Uses find_task_by_id() from foundation, uses data.py
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Uses find_task_by_id() from foundation, uses data.py
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Uses find_task_by_id() from foundation, uses data.py

**Key Insight**: All user stories are independent! After Phase 2 (including data.py setup), they can be implemented in parallel.

### Within Each User Story

- US1: Tasks T012, T013 can run in parallel → T014 depends on both → T015, T016 can run in parallel → T017, T018 in sequence
- US2: Tasks run sequentially (T019 → T020 → T021 → T022)
- US3: Tasks run sequentially (T023 → T024 → T025 → T026 → T027)
- US4: Tasks run sequentially (T028 → T029 → T030 → T031 → T032 → T033)

### Parallel Opportunities

- **Setup (Phase 1)**: T003, T004 can run in parallel
- **Foundational (Phase 2)**: T009, T010, T011 can run in parallel (after T005-T008)
- **User Story 1**: T012, T013 can run in parallel; T015, T016 can run in parallel
- **All User Stories (Phase 3-6)**: Can be worked on in parallel by different developers
- **Testing (Phase 8)**: T046-T055 can all run in parallel (independent tests)
- **Documentation (Phase 9)**: T057-T060 can run in parallel

---

## Parallel Example: After Foundation Complete

```bash
# All user stories can start simultaneously (after data.py is set up):
Developer A: Implements User Story 1 (T012-T018)
Developer B: Implements User Story 2 (T019-T022)
Developer C: Implements User Story 3 (T023-T027)
Developer D: Implements User Story 4 (T028-T033)

# Or single developer doing MVP first:
Complete User Story 1 → Test independently → Deploy/Demo (MVP!)
Then add User Story 2 → Test independently → Deploy/Demo
Then add User Story 3 → Test independently → Deploy/Demo
Then add User Story 4 → Test independently → Deploy/Demo
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Foundational (T005-T011) - CRITICAL (includes data.py setup)
3. Complete Phase 3: User Story 1 (T012-T018)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Minimal main menu (just options 1, 2, 6) to demo
6. Deploy/demo if ready

**At this point you have a working todo app!** Users can add tasks and view them.

### Incremental Delivery

1. MVP: User Story 1 → Working add/view app
2. Add User Story 2 → Now users can mark tasks complete
3. Add User Story 3 → Now users can edit tasks
4. Add User Story 4 → Now users can delete tasks
5. Each story adds value without breaking previous stories

### Full Implementation (Single Developer)

1. Phase 1: Setup (T001-T004) - ~15 minutes
2. Phase 2: Foundational (T005-T010) - ~30 minutes
3. Phase 3: User Story 1 (T011-T017) - ~45 minutes
4. Phase 4: User Story 2 (T018-T021) - ~20 minutes
5. Phase 5: User Story 3 (T022-T026) - ~30 minutes
6. Phase 6: User Story 4 (T027-T032) - ~30 minutes
7. Phase 7: Main Menu (T033-T043) - ~30 minutes
8. Phase 8: Testing (T044-T055) - ~60 minutes
9. Phase 9: Documentation (T056-T063) - ~45 minutes

**Total**: ~4-5 hours for complete implementation

---

## Task Summary

- **Total Tasks**: 64
- **Setup Tasks**: 4 (Phase 1)
- **Foundational Tasks**: 7 (Phase 2) - includes data.py creation
- **User Story 1 Tasks**: 7 (Phase 3)
- **User Story 2 Tasks**: 4 (Phase 4)
- **User Story 3 Tasks**: 5 (Phase 5)
- **User Story 4 Tasks**: 6 (Phase 6)
- **Integration Tasks**: 11 (Phase 7)
- **Testing Tasks**: 12 (Phase 8)
- **Documentation Tasks**: 8 (Phase 9)

**Parallel Opportunities**: 23 tasks marked [P] can run in parallel
**Independent User Stories**: 4 stories (can each be developed/tested/deployed independently)
**File Structure**: 2 files (src/data.py for data storage, src/todo.py for all logic)

---

## Notes

- Data storage in: `src/data.py` (global variables only)
- All logic in: `src/todo.py` (imports from data.py)
- Tests in separate file: `tests/test_todo.py`
- Each user story is independently testable and deliverable
- MVP = Just User Story 1 (add + view tasks)
- Foundation phase (T005-T011) blocks all user stories - includes data.py setup
- After foundation, all user stories can proceed in parallel
- Commit after each phase completion for clean history
