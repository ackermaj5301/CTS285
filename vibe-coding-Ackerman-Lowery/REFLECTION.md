# Reflection

## 1. The AI as Collaborator
**When did the AI help most?**  
It was most helpful generating a working starting point quickly. I went from nothing to a playable game in one prompt. It also sped up polish steps like keyboard shortcuts and ARIA labels.

**When did it frustrate me most?**  
On small details like copy text and pluralization, and when I needed a different UX, I still had to read and tweak code. The AI occasionally missed edge cases until I spelled them out.

**What surprised me?**  
How fast a decent prototype comes together. Also, accessibility improvements (aria-live, labels) were easy once I asked—reminding me to specify these requirements early.

## 2. The Framework Experiment
**What did the AI recommend and why?**  
It recommended React, Vue, or Svelte and picked **React** for component model and state hooks, while admitting vanilla JS is simpler here.

**What was different about building an SPA?**  
More ceremony and code. Even using React via CDN (no tooling), I still had to think in components and state and include extra scripts.

**Which approach felt better for this game? Why?**  
Vanilla HTML+JS felt better—fewer moving parts, immediate results, and simpler to reason about. For a bigger app (routing, complex state), I’d switch to React.

## 3. The “Vibe Coding Ceiling”
**Did you hit a point where AI couldn’t help anymore?**  
Not a hard ceiling, but I still needed to understand state and event flow to adjust behavior. The AI won’t always guess the UX decisions I want.

**When did you realize you needed to understand the code yourself?**  
When debugging validation and stats; I had to trace variables and conditions. Reading the code mattered.

**What would you do differently next time?**  
State detailed requirements up front (validation rules, accessibility), and test edge cases early. Keep iterations small and named clearly.

## 4. Growth Moment
**What did this teach you about AI tools?**  
They’re great accelerators for scaffolding and incremental improvements, but not a substitute for understanding how the code flows.

**What did this teach you about web development?**  
Even tiny apps benefit from good UX, accessibility, and clear state. Frameworks are powerful but add overhead.

**What question do you have now that you didn’t have before?**  
How to structure larger React apps (routing, data fetching) without overwhelming setup—what’s the lightest path from CDN to a maintainable project?
