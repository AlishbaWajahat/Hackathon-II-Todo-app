<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0
- Amendment: Abstracted feature-specific details, added missing principles
- Principles modified:
  - Principle IV: "User-Centric CLI Experience" → "User-Centric Interface Design" (generalized)
  - Principle V: "Quality Assurance Through Testing" → removed Phase I specifics
  - Principle VII: "Constraints and Non-Goals" → split into "Development Constraints" (universal) and "Phase-Specific Scope" (phase-bound)
- Principles added:
  - Principle VIII: Error Handling & Resilience
  - Principle IX: Security & Data Integrity
  - Principle X: Performance & Efficiency
  - Principle XI: Observability & Logging
- Sections modified:
  - Preamble: Removed specific feature list (Add, Delete, Update, View, Mark Complete)
  - Project Structure: Generalized file organization (removed cli.py, core.py, models.py specifics)
- Templates status: ✅ Principles now phase-agnostic and reusable
- Follow-up: Feature-specific details moved to spec.md domain
-->

# Todo App Constitution

## Preamble

This constitution governs the development of a task management application built using the **Agentic Dev Stack**: a specification-driven approach where requirements flow through spec → plan → tasks → autonomous implementation by Claude Code.

**Core Philosophy**: All implementation is performed autonomously by AI agents following clearly defined specifications, architectural plans, and structured tasks. No manual code editing is permitted.

**Technology Foundation**: UV package manager, Python 3.13+, Claude Code AI agent, and Spec-Kit Plus framework for structured development artifacts.

**Evolutionary Design**: The project is designed for incremental enhancement across multiple phases. Each phase builds on the previous foundation without requiring architectural refactoring.

## Core Principles

### I. Spec-Driven Workflow (NON-NEGOTIABLE)

Every feature, change, or enhancement MUST follow the spec-driven development lifecycle:

1. **Specification First**: Requirements documented in `specs/<feature>/spec.md` before any implementation
2. **Architectural Planning**: Design decisions captured in `specs/<feature>/plan.md` with rationale
3. **Task Breakdown**: Implementation steps defined in `specs/<feature>/tasks.md` with acceptance criteria
4. **Autonomous Implementation**: Claude Code executes tasks without manual code intervention
5. **Iterative Refinement**: Quality reviews drive spec/plan/task updates, then re-implementation

**Rationale**: Prevents scope drift, ensures architectural consistency, creates auditable decision trail, and enables AI-driven development with clear constraints.

### II. Clean Code Standards

All Python code MUST adhere to:

- **PEP 8** style guide for formatting and naming conventions
- **Type hints** for function signatures and return values (Python 3.13+ syntax)
- **Docstrings** for modules, classes, and public functions (Google style)
- **Meaningful names**: descriptive variables/functions that reveal intent
- **Single Responsibility**: each function/class has one clear purpose
- **DRY principle**: eliminate duplication through abstraction where appropriate

**Rationale**: Ensures code readability, maintainability, and seamless AI agent understanding for future iterations.

### III. Modular Design for Extensibility

Architecture MUST support future enhancements without major refactoring:

- **Separation of Concerns**: UI layer, business logic, data layer clearly separated
- **Interface-Based Design**: define contracts between components
- **Minimal Coupling**: components depend on abstractions, not implementations
- **Plugin-Ready Architecture**: structure anticipates component swapping (persistence backends, UI frameworks, APIs)
- **Dependency Inversion**: high-level modules don't depend on low-level implementation details

**Rationale**: Early phases are foundations; architecture must accommodate future features without accumulating technical debt.

### IV. User-Centric Interface Design

User interfaces MUST be intuitive and forgiving:

- **Clear Communication**: every user interaction has descriptive context and feedback
- **Input Validation**: validate before processing, provide actionable error messages
- **Confirmation for Destructive Actions**: operations that delete or modify data require explicit confirmation
- **Graceful Degradation**: failures return users to a safe state, never crash
- **Accessibility**: interfaces work for users of varying technical skill levels

**Rationale**: User experience determines adoption; poor interface design creates friction regardless of technical excellence.

### V. Quality Assurance Through Testing

Testing standards apply across all phases:

- **Unit tests** for core business logic and isolated components
- **Edge case coverage**: boundary conditions, invalid inputs, error scenarios
- **Test isolation**: each test independent, no shared state between tests
- **Automated execution**: tests run via single command with clear pass/fail output
- **Coverage target**: minimum 80% for business logic modules
- **Test-Driven Development**: where appropriate, write tests before implementation

**Rationale**: Testing discipline established early prevents technical debt accumulation and enables confident refactoring.

### VI. Version Control Discipline

Every iteration MUST produce atomic, traceable commits:

- **Commit per iteration**: each spec → plan → tasks → implementation cycle produces one commit
- **Descriptive messages**: follow conventional commits format (`feat:`, `fix:`, `docs:`, `refactor:`)
- **Feature branches**: work on dedicated branches, merge via pull requests
- **Clean history**: squash WIP commits before merging to main
- **Semantic versioning**: tag releases following MAJOR.MINOR.PATCH convention

**Rationale**: Version control is project memory; clear history enables rollback, debugging, and learning from decisions.

### VII. Development Constraints (Universal)

**Hard Constraints Applied to All Phases**:
- NO manual code editing (all implementation via Claude Code)
- NO secrets or credentials in code (use environment variables)
- NO commented-out code in final commits (remove or document as TODOs)
- NO warnings or linter errors in committed code
- NO bypassing of quality gates without documented justification

**Rationale**: Constraints ensure consistency, security, and maintainability across the entire project lifecycle.

### VIII. Error Handling & Resilience

All code MUST handle errors gracefully and predictably:

- **Explicit Error Types**: use specific exception types, not generic exceptions
- **Error Propagation**: errors bubble up with context; catch only when you can handle
- **User-Facing Errors**: translate technical errors into actionable user messages
- **Logging on Failure**: all error paths log sufficient context for debugging
- **No Silent Failures**: errors are either handled or propagated, never swallowed
- **Recovery Paths**: provide mechanisms to recover from errors where feasible

**Rationale**: Robust error handling separates production-ready software from prototypes; users and developers need clear failure diagnostics.

### IX. Security & Data Integrity

Security and data integrity are non-negotiable:

- **Input Validation**: validate and sanitize all external inputs
- **Principle of Least Privilege**: components access only necessary data/operations
- **No SQL Injection**: use parameterized queries or ORMs (when applicable)
- **Secrets Management**: never hardcode credentials; use environment variables or secret managers
- **Data Validation**: validate data at system boundaries (user input, file reads, API responses)
- **Audit Trail**: log security-relevant operations (authentication, authorization, data access)

**Rationale**: Security vulnerabilities and data corruption destroy user trust; prevention is cheaper than remediation.

### X. Performance & Efficiency

Code MUST be efficient without premature optimization:

- **Measure Before Optimizing**: profile before claiming performance issues
- **Algorithmic Efficiency**: choose appropriate data structures and algorithms (O(n) vs O(n²) matters)
- **Resource Cleanup**: close files, connections, and resources promptly
- **Avoid Unnecessary Work**: cache where beneficial, avoid redundant computations
- **Scalability Awareness**: consider how code behaves with 10x, 100x, 1000x data

**Rationale**: Performance problems caught late are expensive to fix; thoughtful design prevents most issues.

### XI. Observability & Logging

Systems MUST be observable and debuggable:

- **Structured Logging**: use consistent log formats with context (timestamps, levels, module names)
- **Log Levels**: DEBUG for development, INFO for key operations, WARNING for anomalies, ERROR for failures
- **No Print Statements**: use logging framework, not print() for debugging
- **Actionable Messages**: logs answer "what happened" and "why it matters"
- **Performance Logging**: log operation durations for slow paths
- **Correlation IDs**: when applicable, track operations across components

**Rationale**: You cannot fix what you cannot observe; comprehensive logging enables rapid debugging and performance analysis.

## Phase-Specific Scope

### Phase I Boundaries

**In Scope**:
- Command-line interface implementation
- In-memory data storage (no persistence)
- Core task management operations
- Python standard library only (no external dependencies for core logic)
- Single-user, single-session usage model

**Out of Scope**:
- Data persistence across sessions
- Multi-user support or concurrent access
- Network operations or API endpoints
- Configuration file management
- Advanced features (scheduling, reminders, categories, undo/redo)

**Rationale**: Phase I validates the agentic development approach with minimal complexity; scope constraints prevent feature creep and enable focused implementation.

## Development Workflow

### Iteration Cycle

1. **Clarification**: If spec ambiguous, agent asks targeted questions (max 3) before planning
2. **Planning**: Generate architectural plan with design decisions documented
3. **Task Breakdown**: Decompose plan into testable tasks with acceptance criteria
4. **Implementation**: Claude Code executes tasks sequentially or in parallel where independent
5. **Validation**: Run tests, verify acceptance criteria met
6. **Review**: Assess quality against constitutional principles
7. **Commit**: Create atomic commit with descriptive message
8. **Repeat**: Iterate until feature complete

### Decision Documentation

- **Minor decisions**: captured in plan.md or inline comments
- **Architectural decisions**: create ADR in `history/adr/` when:
  - Decision impacts future phases or crosses component boundaries
  - Multiple viable options considered with significant tradeoffs
  - Cross-cutting concerns (error handling strategy, data structure choices, security model)
  - Decision is irreversible or costly to change

### Prompt History Records (PHR)

Every user interaction MUST produce a PHR in `history/prompts/`:
- Constitution changes → `history/prompts/constitution/`
- Feature work → `history/prompts/<feature-name>/`
- General interactions → `history/prompts/general/`

PHRs capture: user input (verbatim), stage, assistant response, files changed, tests run, outcomes.

## Quality Standards

### Code Quality Gates

Before considering any task complete:

- ✅ All tests pass
- ✅ No linter errors (ruff/pylint)
- ✅ Type checking passes (mypy)
- ✅ Code follows PEP 8
- ✅ Docstrings present for public API
- ✅ Error handling implemented per Principle VIII
- ✅ Security checklist validated per Principle IX
- ✅ Logging added per Principle XI
- ✅ Acceptance criteria met

### Documentation Requirements

- **README.md**: Installation, usage, features, examples
- **CLAUDE.md**: Agent-specific instructions, project context, active technologies
- **spec.md**: Feature requirements and success criteria
- **plan.md**: Architectural decisions and rationale
- **tasks.md**: Implementation tasks with acceptance tests
- **Inline comments**: For non-obvious logic only (code should be self-documenting)

```

## Governance

### Constitutional Authority

This constitution is the highest authority for development. All specifications, plans, tasks, and code reviews MUST verify compliance with these principles.

### Amendment Process

1. **Proposal**: Document proposed change with rationale in constitution PR
2. **Impact Analysis**: Identify affected specs, plans, tasks, and code
3. **Version Bump**:
   - MAJOR: backward-incompatible principle changes or removals
   - MINOR: new principles or sections added
   - PATCH: clarifications, typo fixes, non-semantic refinements
4. **Propagation**: Update dependent templates and documentation
5. **Approval**: User reviews and approves amendment
6. **Implementation**: Merge and tag new version

### Compliance Review

- Every PR checks: "Does this adhere to constitutional principles?"
- Violations require justification or constitution amendment
- Agent surfaces ADR suggestions for significant decisions (user consent required)
- Complexity must be justified against simplicity and YAGNI principles

### Living Document

This constitution evolves with the project. Ambiguities discovered during implementation trigger clarifying amendments. Lessons learned from each phase inform principle refinements for subsequent phases.

**Version**: 1.1.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
