# World of Games

Welcome to the **World of Games**, where your wits, memory, and intuition are put to the ultimate test! Whether you're a seasoned gamer or a curious novice, our collection of engaging challenges will keep you on the edge of your seat. Dive into a realm where guessing the right number, predicting currency values, and recalling sequences are all part of the thrilling journey. Ready to embark on an adventure filled with fun and excitement? Let's get started and see if you have what it takes to conquer the World of Games!

### Guess Game

**Objective:**  
Guess a randomly generated number within a range of 0 to the difficulty level.

**Gameplay:**

1. A number is generated within the range.
2. The player guesses the number.
3. The game checks if the guess matches the generated number.
4. The player wins if the guess is correct; otherwise, loses.

---

### Currency Roulette Game

**Objective:**  
Guess the value of a random USD amount (1 to 100) converted to ILS.

**Gameplay:**

1. The game retrieves the current USD to ILS exchange rate.
2. The player guesses the ILS value of a random USD amount.
3. The acceptable range for the guess is determined by subtracting the difficulty level from 10 NIS.
4. The player wins if their guess falls within the acceptable range; otherwise, loses.

---

### Memory Game

**Objective:**  
Recall and input a sequence of displayed random numbers.

**Gameplay:**

1. A sequence of random numbers is displayed briefly.
2. The player recalls and inputs the sequence.
3. The game checks if the input matches the original sequence.
4. The player wins if the input is correct; otherwise, loses.

---

---

**Installation Guide**
To start playing you need:

- python installed (tested on v3.12)

- install dependencies `pip install -r requirements.txt`

- run main `py main.py`

- run main score server `py main_score.py`
  and then to view the current score go to http://localhost:3001

- Good Mood!

**Testing**
For testing the current score page, use this command:
`py tests/e2e.py 3001`

### Enjoy!
