# Code Style & Engineering Principles

Write code that a competent, practical human developer would naturally write: **simple, readable, idiomatic, and easy to maintain.**

Your priority is clarity over cleverness. The goal is not to write the fewest lines possible, but to solve the problem with the least unnecessary complexity.

## 1. Keep the Code Simple
- Use the simplest solution that correctly solves the problem.
- Prefer straightforward control flow over clever tricks, deeply nested ternaries, or unnecessarily compact expressions.
- Do not overengineer simple features.
- Avoid unnecessary classes, design patterns, abstractions, wrappers, factories, interfaces, and utility functions.
- Do not create a helper function for a trivial operation unless it meaningfully improves readability or is reused.
- Avoid introducing dependencies when the language or existing project already provides a suitable solution.
- Do not build features or infrastructure that the task does not require.

## 2. Write Readable, Natural Code
- Use descriptive, natural variable and function names.
- Keep functions focused, but do not split every few lines into another function.
- Prefer obvious code over code that requires mental gymnastics to understand.
- Follow the naming conventions, formatting, and coding patterns already used in the project.
- Use the existing language's idioms instead of forcing patterns from another language.
- Write code so a developer can understand what it does without having to read the entire codebase first.
- Avoid unnecessary comments explaining obvious operations.

## 3. Avoid AI-Style Overengineering
- Do not rewrite working code just to make it look more sophisticated.
- Do not add excessive defensive checks for impossible or irrelevant scenarios.
- Do not add redundant fallback logic, duplicate validation, or multiple layers of error handling for the same failure.
- Avoid excessive configuration options when a sensible default is sufficient.
- Do not introduce generic systems when a direct implementation solves the actual problem.
- Do not add lengthy docstrings, comments, or type annotations that repeat information already obvious from the code, unless the project requires them.
- Do not optimize performance without a real, relevant reason.
- Never sacrifice correctness, security, or necessary error handling just to reduce line count.

## 4. Respect the Existing Codebase
Before making changes:
- Inspect the relevant files and understand the existing implementation.
- Reuse existing functions, utilities, dependencies, and conventions where appropriate.
- Identify the smallest set of changes needed to complete the task.
- Avoid unrelated refactoring and do not modify files that do not need to change.
- Preserve existing behavior unless the task explicitly requires changing it.

## 5. Handle Errors and Edge Cases Properly
- Validate untrusted input at appropriate boundaries.
- Handle realistic failure cases explicitly and clearly.
- Keep error handling close to the operation that can fail when practical.
- Avoid swallowing exceptions or returning fake success results.
- Preserve security-sensitive checks, permissions, and input validation.
- Handle relevant edge cases without turning every function into a collection of defensive checks.

## 6. Comments and Documentation
- Write comments to explain why something is done, not merely what the code does.
- Document non-obvious business rules, workarounds, and important assumptions.
- Do not add comments to every function or block of code.
- Keep documentation consistent with the actual implementation.

## 7. Make Focused Changes
- Implement only what is necessary to satisfy the request.
- Prefer a small, complete change over a large rewrite.
- Avoid changing public APIs, database schemas, configuration formats, or existing interfaces unless necessary.
- Do not silently remove existing functionality.
- Do not create extra files unless they serve a real purpose.

## 8. Verify the Result
- Run the relevant tests, linting, or type checks when available and practical.
- Fix errors introduced by your changes.
- Do not claim tests passed unless you actually ran them.
- If a check cannot be run, say so explicitly.

## 9. Final Review
Before finishing, ask yourself:
1. Is there a simpler way to achieve the same result?
2. Did I introduce an abstraction or dependency that is not needed?
3. Can another developer understand this code quickly?
4. Did I preserve existing behavior and handle realistic failure cases?
5. Did I make any unrelated changes?

If the implementation can be made meaningfully simpler without sacrificing correctness, security, or maintainability, simplify it before finishing.

**Golden rule:** Write boring, obvious, maintainable code. Prefer code that is easy to read six months from now over code that looks impressive today.
