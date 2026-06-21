# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game's purpose is to have the user successfully guess the secret number within a set number of tries. The user has the ability to change the level of difficulty as well as a chance to see a hint regarding their current guess (whether it is too high or low compared to the secret number) as well. 
- A few bugs that I have encountered were incorrect hints ("Go Higher" instead of "Go Lower" and vice versa), the secret number not being within the range of the difficulty chosen, etc..
- I fixed these bugs by changing the return statements depending on the case, adjusting the secret number to be within the range of the difficulty chosen, and more.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects a difficulty level of Easy
2. User enters a guess of 12
3. The game returns a hint "Too High"
4. User enters a guess of 5
5. The game returns a hint "Too Low"
6. Score updates correctly after each guess
7. Game ends after the correct guess
8. User clicks on "New Game" to restart
