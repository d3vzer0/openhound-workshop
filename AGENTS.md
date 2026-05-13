# AGENTS.md - Agent Guidance

## Before Editing

- Read `.agents/standards/openhound.md` to learn more about the OpenHound framework.
- Read `.agents/standards/workflow.md` to understand the workflow on creating a new OpenHound collector.
- Load the `openhound` skill from `.agents/skills/openhound/` for task-specific workflows.

## OpenHound Task Skill

Use `openhound` for all OpenHound collector work. The skill routes tasks to action-specific references.

| Task                                                                                   | Skill       | Reference |
|----------------------------------------------------------------------------------------|-------------|---|
| Plan a new collector from target service requirements or API docs                      | `openhound` | `.agents/skills/openhound/references/plan-collector.md` |
| Add or modify a collected asset/model                                                  | `openhound` | `.agents/skills/openhound/references/add-asset.md` |
| Implement API collection resources, transformers, auth and DLT source wiring           | `openhound` | `.agents/skills/openhound/references/source-collection.md` |
| Define base graph node/edge dataclasses and ID generation behavior                     | `openhound` | `.agents/skills/openhound/references/graph-schema.md` |
| Add DuckDB transforms or lookup methods                                                | `openhound` | `.agents/skills/openhound/references/preproc-lookup.md` |
| Wire phase registration (collect, preproc, convert), metadata, or package entry points | `openhound` | `.agents/skills/openhound/references/register-extension.md` |
| Validate a collector before finishing                                                  | `openhound` | `.agents/skills/openhound/references/validate-extension.md` |


## General Rules

Behavioral guidelines. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:

- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:

- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:

- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:

- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

