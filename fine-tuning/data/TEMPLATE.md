# Training Data Template

Add examples to `training_data.json` in this format:

## Example 1: Code Generation
```json
{
  "instruction": "Create a [component/function/class] for [purpose]",
  "input": "",
  "output": "[Your ideal code output with explanation]"
}
```

## Example 2: Code Explanation
```json
{
  "instruction": "Explain [concept/code]",
  "input": "[Optional code snippet]",
  "output": "[Clear explanation]"
}
```

## Example 3: Debugging
```json
{
  "instruction": "Find the bug in this code",
  "input": "[Buggy code]",
  "output": "[Explanation of bug and fix]"
}
```

## Example 4: Best Practices
```json
{
  "instruction": "What are best practices for [topic]",
  "input": "",
  "output": "[List of best practices with examples]"
}
```

---

## Where to Get Training Data

1. **Your existing code** - Document your best code
2. **Stack Overflow** - Q&A pairs
3. **GitHub** - Code examples with comments
4. **Your documentation** - Convert to Q&A
5. **API logs** - Real user questions
6. **Code reviews** - Common issues and fixes

---

## Quality > Quantity

- 50 excellent examples > 500 mediocre ones
- Focus on YOUR specific use cases
- Include edge cases and error handling
- Show your preferred coding style
- Add domain-specific knowledge

---

## Example Categories for CodePilot

- React components (forms, buttons, modals)
- API endpoints (CRUD operations)
- Database queries (SQL, MongoDB)
- Authentication (JWT, OAuth)
- Error handling patterns
- Testing examples
- Deployment configs
- Security best practices
