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

1. **Count Words**:
This script is a word frequency counter. It prompts the user to enter a phrase or sentence, then processes the input by splitting it into a list of words. It utilizes the build_dictionary function to create a dictionary where each unique word is a key and its count (frequency) is the corresponding value. Finally, it prints the word-frequency pairs, ensuring they are displayed in alphabetical order by iterating through the sorted keys of the dictionary.

2. **Connect4 Game**
This script implements the classic game `Connect Four`. It uses a nested list (a list of 6 lists, each with 7 elements) to represent the 6 x 7 game board. Key functions demonstrate list manipulation and conditional logic:
   * `resetBoard` initializes the 2D list to a fresh board.
   * `printBoard` handles displaying the board visually.
   * `validateEntry` and `availablePosition` manage move legality by checking the state of the list.
   * `checkWin` implements the complex logic for checking horizontal, vertical, and diagonal wins by iterating and slicing through the nested list structure.
   * The main game loop alternates turns until a win or a tie (full board) is detected.
   
---

### Week 3: Introduction to DataFrames with Pandas 🐼

This week, I explored the basics of the **pandas** library, a fundamental tool for data manipulation and analysis in Python. The focus was on understanding how to create, inspect, and analyze data stored in DataFrames. I completed two scripts to practice these skills.

1. **BMI Calculator & Storing in DataFrame**: This script is an interactive Body Mass Index (BMI) calculator. It showcases the dynamic creation of a pandas DataFrame from scratch.
    * It prompts the user to enter their age, weight (in lbs), and height (in cm) within a loop.
    * For each entry, it calculates the BMI, assigns a weight category (e.g., healthy, overweight), and appends the results to Python lists.
    * After each calculation, it converts a dictionary of these lists into a **pandas DataFrame**, printing the updated table to the console. This demonstrates how to build a DataFrame row-by-row from user input.

2. **Ramen Ratings Analysis**: This project involved performing exploratory data analysis on "The Ramen Rater" dataset from Kaggle. This notebook demonstrates a more practical, analysis-focused workflow. Key pandas operations practiced include:
    * **Loading Data**: Reading a `.csv` file directly into a DataFrame.
    * **Data Inspection**: Using `.head()`, `.tail()`, and `.describe()` to get a quick overview and statistical summary of the data.
    * **Filtering & Sorting**: Selecting specific columns, querying rows based on conditions (like finding all ramen from "Vietnam"), and sorting the data by review scores (`.sort_values()`).
    * **Data Cleaning**: Replacing values in a column, such as changing "USA" to "United States" using `.replace()`.
    * **Aggregation**: Using `.groupby()` combined with `.mean()` and `.nunique()` to answer analytical questions, such as finding the countries with the highest average ratings and the most unique brands.
   
---

### Week 4: Handling Files and Starting OOP 📁

This week marked a significant step in my Python journey as I explored two key areas: **file I/O** (Input/Output) for persistent data storage and the principles of **Object-Oriented Programming (OOP)** through the creation of classes.

1. **MPG Calculation with Files**: This project extended a basic miles-per-gallon calculator to read from and write to an external text file (`trips.txt`).
    * **File I/O**: The script uses a tab-delimited file to store trip data. The `read_trips` function demonstrates opening a file in read mode (`"r"`), skipping the header line, reading line-by-line, and parsing the data into a list of lists. The `write_trips` function handles opening the file in write mode (`"w"`) and overwriting it with the updated list of trips, including the header.
    * **Data Persistence**: By writing new trips to the file, the program maintains a persistent record of all entries, allowing the data to be loaded and updated across multiple runs.
    * **List Manipulation**: New calculated trips are temporarily appended to a list of lists before being written back to the file.

2. **Battle Simulation (OOP)**: This project introduces the core concepts of Object-Oriented Programming by simulating a fantasy battle between heroes and a monster (Needless to say I am a huge LOTR fan ✨).
    * **Classes & Inheritance**: It defines a base class, **`Character`**, which includes fundamental attributes (name, HP, attack, defense) and methods (like `attack` and `show_status`).
    * **Subclasses**: It then creates two specialized subclasses, **`Hero`** and **`Monster`**, which inherit all properties and methods from `Character`.
    * **Polymorphism & Special Moves**: Each subclass implements its own unique `special_move` method, demonstrating polymorphism. For instance, the **Healer Hero** restores HP, the **Warrior Hero** deals triple damage, and the **Boss Monster** reduces a target's attack power.
    * **Encapsulation**: Attributes like HP and ATK are bundled within the character objects, and their state is managed through class methods, providing a clean object structure. The `main` function then instantiates these classes to create a battle scenario.
  
---
