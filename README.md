# Python Refresher
This repository contains files I created to refresh and reinforce my understanding of Python. Although I’ve worked extensively with Python across internships, research projects, and professional roles, I wanted to revisit the fundamentals to ensure a solid foundation. Since I don’t come from a formal computer science background, this was a way to clear any lingering gaps and avoid carrying forward false assumptions in future projects and roles.

---

### Week 1: Control Flow & Functions

In Week 1, I focused on strengthening my understanding of control flow (`if/else`, loops) and function calls, including working with modules. I created two main Python files along with a helper module (`pig_latin.py`).

1. **Estimate Pi**:
   This script estimates the value of π using the Gregory-Leibniz series. It takes the number of desired iterations as input and outputs the estimated value along with the error compared to π's actual value.

2. **Text Conversion**:
   This script takes a user-input phrase or sentence, cleans it (removing punctuation and extra spaces), and converts it into a jumbled version using a function from the `pig_latin.py` module. It demonstrates basic string manipulation and module usage.

---

### Week 2: Lists and Dictionaries

In Week 2, I explored the use of lists and dictionaries to store and manipulate data. I created two main Python files: one for data processing using a dictionary to track frequency, and another for a game that uses a nested list (list of lists) to represent a game board.

1. **Count words**:
This script is a word frequency counter. It prompts the user to enter a phrase or sentence, then processes the input by splitting it into a list of words. It utilizes the build_dictionary function to create a dictionary where each unique word is a key and its count (frequency) is the corresponding value. Finally, it prints the word-frequency pairs, ensuring they are displayed in alphabetical order by iterating through the sorted keys of the dictionary.

2. **Connect4 Game**
This script implements the classic game Connect Four. It uses a nested list (a list of 6 lists, each with 7 elements) to represent the 6 x 7 game board. Key functions demonstrate list manipulation and conditional logic:
   'resetBoard' initializes the 2D list to a fresh board.
   'printBoard' handles displaying the board visually.
   'validateEntry' and 'availablePosition' manage move legality by checking the state of the list.
   'checkWin' implements the complex logic for checking horizontal, vertical, and diagonal wins by iterating and slicing through the nested list structure.
   The main game loop alternates turns until a win or a tie (full board) is detected.
