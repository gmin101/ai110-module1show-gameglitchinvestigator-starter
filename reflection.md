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
  One suggestion that Claude gave me was when a user tries to attempt a guess but is "too high" or "too low" from the secret number, when the hint given is "Too High" then the player is awarded 5 points whereas when the attempt is "Too Low" this subtracts 5. It pointed out the fact that a wrong guess should not increase the score and the different types of wrong outcomes should not have different effects to the score; they are both wrong, hence no points should be added. This suggestion was not inccorect or misleading and was very helpful. I verified this result by checking the logic of update_score in app.py and noticed that the code does do this. I was also able to verify this by playing with the game and testing the different cases.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  To be honest, I didn't find any of the suggestions to be incorrect or misleading.
  
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided a bug was really fixed when I tried playing with the game and seeing that it worked like how it should have.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  One test that I ran was checking whether the hint that displays on the screen is correct. It showed me that my code can be easily fixed with minimal change in my code.
- Did AI help you design or understand any tests? How?
  AI did help me with understanding the tests through its comments. I was able to easily follow along what cases the tests were testing for.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit "reruns" my code everytime the user clicks on anything, so information isn't typically stored into memory here. Session state however, is like a dictionary that remembers the information that we do need to keep, such as the score and secret number in this case.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  One habit from this project that I want to reuse in future labs or projects is to continue to reconfirm whether the AI is correct before using the suggested code.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
  Something I would like to do differently next time is trying to fix the code myself and asking the AI how to correct my current code or ask how to proceed with what I have so far.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project helped me realize that AI generated code is very useful but sometimes may do something that you did not intend it to do, so it is very important to double check what the suggested code does before accepting it.