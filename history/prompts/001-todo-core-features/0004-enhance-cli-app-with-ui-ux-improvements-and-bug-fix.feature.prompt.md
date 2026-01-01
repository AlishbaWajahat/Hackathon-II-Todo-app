---
id: 002
title: Enhance CLI app with UI/UX improvements and bug fix
stage: feature
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-todo-core-features
branch: 001-todo-core-features
user: unknown
command: "My app is created just testing phases are incomplete we'll do that , but before i want you to make some good changes in my cli app using "cli- formatter" skill ; Changes i want you to make \n1. i want to use arrow key to select action inside of writing index no.\n2. i want that when i choose delete tasks or update task or toggle task etc .. all my tasks should appear and i'd be able to select 1 using arrow keys instead of writing their ids \n3. A bug i noticed; that even if i deleted task 1 and then adding another tasks its id is 2 , even though it should be one as i deleted first task and there is no tasks\n4. for toggle , my all tasks should appear with a toggle button beside them so i could toggle any task i want \n5. CLI ui is so boring and basic install and use 'rich' package to make it look premium using cli-formatter skill properly "
labels: ["cli-formatter", "ui-ux", "bug-fix", "rich"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- No files modified
tests:
- No tests run
---

## Prompt

My app is created just testing phases are incomplete we'll do that , but before i want you to make some good changes in my cli app using "cli- formatter" skill ; Changes i want you to make
1. i want to use arrow key to select action inside of writing index no.
2. i want that when i choose delete tasks or update task or toggle task etc .. all my tasks should appear and i'd be able to select 1 using arrow keys instead of writing their ids
3. A bug i noticed; that even if i deleted task 1 and then adding another tasks its id is 2 , even though it should be one as i deleted first task and there is no tasks
4. for toggle , my all tasks should appear with a toggle button beside them so i could toggle any task i want
5. CLI ui is so boring and basic install and use 'rich' package to make it look premium using cli-formatter skill properly

## Response snapshot

I will help you enhance your CLI application with the requested UI/UX improvements and fix the task ID bug. This involves integrating the `rich` package and updating the interaction patterns to use arrow keys. Let me first create a todo list to track these tasks, and then I will enter plan mode to outline the implementation strategy.

## Outcome

- ✅ Impact: PHR created for user request.
- 🧪 Tests: N/A
- 📁 Files: history/prompts/001-todo-core-features/002-enhance-cli-app-with-ui-ux-improvements-and-bug-fix.feature.prompt.md
- 🔁 Next prompts: Create todo list, then enter plan mode.
- 🧠 Reflection: Successfully captured the user's request and outlined next steps.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
