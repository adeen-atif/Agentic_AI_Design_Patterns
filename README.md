# Red Turtles Paint Murals — 4 Foundational Agentic AI Design Patterns

This repo accompanies the blog post that breaks down four foundational patterns in agentic AI system design—each inspired by how humans solve problems, and powered by runnable code.

These four patterns form the mnemonic:

**Red Turtles Paint Murals**  
→ **Reflection**, **Tool Use**, **Planning**, **Multi-Agent Systems**

---

## What's Inside

Each `.py` file corresponds to one of the patterns (or sub-patterns) explored in the blog:

| Pattern               | File(s)                                                                 | Description                                                                 |
|----------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Reflection           | `Reflection.py`                                                         | Self-evaluating agents that revise their own outputs                        |
| Tool Use             | `ToolUse.py`                                                            | Agents that use tools like search, math, and APIs                           |
| Planning             | `PlanningAndReasoning.py`                                               | Agents that break down tasks before executing                               |
| Multi-Agent Systems  | `Multi-Sequential.py`, `Multi-Hierarchical.py`, `Multi-Parallel.py`, `Multi-Asynchronous.py` | Four styles of agent collaboration and delegation |

---

## Why It Matters

Monolithic agents only get you so far. These patterns let you:

- Build smarter workflows  
- Structure more capable AI agents  
- Improve scalability, maintainability, and reliability of LLM-powered systems  

---

## Try It Out

Each file is self-contained and runnable. Just clone the repo and run any `.py` file using:

```bash
python Multi-Sequential.py
