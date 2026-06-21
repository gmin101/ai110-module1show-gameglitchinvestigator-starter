# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  When I first ran the game, it looked fine on the surface. The UI was simple and clean. The buttons and text that
  appeared on the screen were easy to follow.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  I noticed that the number of attempts allowed (8) and the number of attempts left (7) at the beginning of the game were 
  different. Additionally, I had to click "Submit Guess" twice for the hint to appear on my screen but each time I click on 
  the button, the number of attempts decreased by 1.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|           Input          | Expected Behavior |  Actual Behavior | Console Output / Error |
|--------------------------|-------------------|------------------|------------------------|
|        Guess of 50       |      Go Lower     |     Go Higher    |          None          |
|        Guess of 110      |   Error message   | Nothing happened |          None          |
|Changed difficulty to easy|   Change secret   |   Secret number  |          None          |
|                          |number to something|   didn't change  |                        |
|                          | within the range  |                  |                        |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude for this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  One suggestion that Claude gave me was when a user tries to attempt a guess but is "too high" or "too low" from the secret number, when the hint given is "Too High" then the player is awarded 5 points whereas when the attempt is "Too Low" this subtracts 5. It pointed out the fact that a wrong guess should not increase the score and the different types of wrong outcomes should not have different effects to the score; they are both wrong, hence no points should be added. I verified this result by checking the logic of update_score in app.py and noticed that the code does do this. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
