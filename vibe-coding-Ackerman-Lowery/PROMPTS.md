# My Vibe Coding Prompts (Number Guessing Game)

> Student: Joey Ackerman-Lowery  
> Date: 2025-11-09

## Prompt 1: Initial Build
**What I asked:**  
"Build me a complete, working Number Guessing Game that runs in a web browser as a single HTML file. Include all CSS and JavaScript inline. The game should pick a random number from 1 to 100, accept guesses, give higher/lower hints, show attempt count, and have a Reset button."

**What the AI did:**  
Generated `attempt1.html` with a random number, Guess and Reset buttons, attempts display, and basic feedback text.

**What worked:**  
The file opened and ran on first try; guessing and resetting worked.

**What didn't work:**  
No input validation; if I typed letters or left it blank, it still incremented attempts. There was no guess history.

**What I learned:**  
Start super simple to confirm the core loop works before adding UX.

---

## Prompt 2: Add Validation + History + Stats
**What I asked:**  
"Improve the Number Guessing Game: block invalid input, keep a guess history with arrows (↑/↓), and track games played and best (fewest attempts) using localStorage. Dark theme and nicer styling, still one HTML file."

**What the AI did:**  
Created `attempt2.html` with validation, history pills, localStorage-based stats, and dark UI.

**What worked:**  
Validation and history worked; stats updated after a win.

**What didn't work:**  
Edge case: best score text didn't pluralize; needed polish on accessibility text.

**What I learned:**  
LocalStorage is easy for lightweight persistence; test edge copy like pluralization and screen reader text.

---

## Prompt 3: Polish for Final
**What I asked:**  
"Polish the UI and accessibility: add instructions, keyboard shortcuts (Enter to guess, R to reset), ARIA/live regions for feedback, and a help button. Keep it as a standalone HTML file."

**What the AI did:**  
Generated `number-guess-final.html` with improved layout, aria-live feedback, keyboard shortcuts, and a help dialog.

**What worked:**  
Everything functioned; app felt friendly and self-explanatory.

**What didn't work:**  
None functionally—just minor CSS tweaks I could change later.

**What I learned:**  
Small UX touches (ARIA, shortcuts, instructions) make a big difference in usability.

---

## Prompt 4: Explain SPAs and Recommend a Framework
**What I asked:**  
"What is a Single Page Application? What frameworks are commonly used? For a small Number Guessing Game, which framework would you pick and why?"

**What the AI did:**  
Explained SPAs; suggested React, Vue, Svelte, or vanilla JS. Recommended **React** for familiarity and component/state model, while noting that for a tiny app vanilla JS is simpler.

**What worked:**  
The tradeoff description made sense: React is overkill for this tiny app but good practice.

**What didn't work:**  
None—was conceptual.

**What I learned:**  
Frameworks add ceremony and power, but also complexity not needed for tiny projects.

---

## Prompt 5: Build a React SPA Version (No Build Tools)
**What I asked:**  
"Rebuild the Number Guessing Game as a SPA using React 18 via CDN (no build step). Put everything in a single `index.html` that I can open directly. Re-create validation, history, attempts, localStorage stats, and reset."

**What the AI did:**  
Created `spa-version/index.html` with React + ReactDOM CDNs, a single `App` component using hooks for state, and equivalent features.

**What worked:**  
It ran by opening the file; no `npm` required.

**What didn't work:**  
Bundle size is larger; code is more verbose compared to vanilla JS.

**What I learned:**  
CDN React is a middle ground to try SPA concepts without tooling, but still heavier than needed.
