---
id: 0002
title: Phase I implementation planning
stage: plan
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-todo-core-features
branch: 001-todo-core-features
user: system
command: /sp.plan
labels: ["plan", "architecture", "design", "procedural", "single-file"]
links:
  spec: specs/001-todo-core-features/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-todo-core-features/plan.md
  - specs/001-todo-core-features/data-model.md
  - specs/001-todo-core-features/quickstart.md
  - CLAUDE.md (agent context updated)
tests:
  - Constitutional compliance check: PASS (all 11 principles satisfied)
  - Design simplicity validation: PASS (single file, procedural, no OOP)
  - User requirements check: PASS (1 file, simple, no OOP)
---

## Prompt

Plan implementation of phase 1 concisely and in clear steps, make sure we are not creating extra file and doing work mostly in 1 file, and code is of good quality simple and easy to understand not using oop.

## Response snapshot

Created comprehensive implementation plan for Phase I Todo Core Features with **single-file, procedural design** prioritizing simplicity over patterns.

**Key Design Decisions**:

1. **ADR-001: Single File, Procedural Implementation**
   - Entire app in `src/todo.py` (one file)
   - Procedural programming (no classes/OOP)
   - Logical sections for separation of concerns:
     - Data Operations (CRUD functions)
     - Business Logic (validation, ID generation)
     - UI Functions (menu, prompts, display)
     - Main (entry point loop)

2. **ADR-002: List of Dictionaries for Storage**
   - Tasks stored as `list[dict]` in global variable
   - Each task: `{'id': int, 'title': str, 'description': str, 'completed': bool}`
   - Auto-incrementing ID counter (global `next_id`)
   - No OOP, no external dependencies

3. **ADR-003: Menu-Driven CLI Pattern**
   - Infinite loop with numbered menu (1-6)
   - Separate flow functions for each operation
   - Graceful error handling (return to menu, never crash)

**Technical Context**:
- **Language**: Python 3.13+
- **Dependencies**: Python stdlib only (no external packages)
- **Storage**: In-memory (list of dicts)
- **Testing**: pytest (separate test file)
- **Structure**: Single file (`src/todo.py`)
- **Performance**: O(n) operations acceptable for 100+ tasks

**Function Contracts Defined**:
- **Data Operations**: `add_task()`, `delete_task()`, `update_task()`, `toggle_task_completion()`, `get_all_tasks()`, `find_task_by_id()`
- **Business Logic**: `generate_task_id()`, `validate_title()`
- **UI Functions**: `display_menu()`, `print_tasks()`, `add_task_flow()`, `view_tasks_flow()`, `update_task_flow()`, `delete_task_flow()`, `toggle_completion_flow()`, `main()`

**Data Model**:
```python
{
    'id': 1,                    # Auto-generated, sequential
    'title': 'Buy groceries',   # Required, non-empty
    'description': 'Milk...',   # Optional, can be ""
    'completed': False          # Boolean, default False
}
```

**Constitutional Compliance**: ✅ All 11 principles satisfied
- Separation of concerns via function grouping (not modules)
- Simple design meets extensibility (can split into modules later)
- Single file satisfies user requirement + constitutional modularity

**Documentation Created**:
- `plan.md` (703 lines) - Comprehensive architecture with ADRs
- `data-model.md` - Data structure, constraints, operations
- `quickstart.md` - User guide with examples and troubleshooting

## Outcome

- ✅ Impact: Implementation plan complete and ready for `/sp.tasks` phase
- 🧪 Tests: Constitutional compliance PASS (11/11 principles), Design simplicity PASS
- 📁 Files: plan.md, data-model.md, quickstart.md created; CLAUDE.md updated
- 🔁 Next prompts: Run `/sp.tasks` to generate detailed implementation tasks
- 🧠 Reflection: Design successfully balances user requirements (1 file, no OOP, simple) with constitutional principles (separation of concerns, extensibility). Single-file structure with logical sections enables clean code without module complexity. ADRs document tradeoffs and migration path for future phases.

## Evaluation notes (flywheel)

- Failure modes observed: None - plan meets all requirements and constraints
- Graders run and results (PASS/FAIL):
  - Constitutional compliance: PASS (all 11 principles satisfied)
  - User requirement "1 file": PASS (single src/todo.py)
  - User requirement "no OOP": PASS (procedural functions only)
  - User requirement "simple": PASS (list of dicts, linear search, clear flow)
  - Extensibility check: PASS (sections can become modules in Phase II)
  - Specification alignment: PASS (all 15 FRs covered by functions)
- Prompt variant (if applicable): User-constrained design (1 file, no OOP, simple)
- Next experiment (smallest change to try): Generate tasks.md and validate task granularity matches single-file constraint
