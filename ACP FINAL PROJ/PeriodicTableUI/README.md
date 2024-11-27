# Elemental Explorer

---

## I. Project Overview

The Periodic Table Game is an interactive educational game designed to test users' knowledge of the periodic table. The game focuses on questions related to the symbols and atomic numbers of chemical elements, providing immediate feedback on the correctness of users' answers. Using Java’s Swing library for the graphical user interface (GUI), the game offers an easy-to-use, engaging interface for learning. It aims to reinforce chemistry concepts in a fun and interactive manner, suitable for students, teachers, and anyone interested in enhancing their knowledge of the periodic table.

---

## II. Object-Oriented Programming (OOP) Principles

This project demonstrates key Object-Oriented Programming principles:

1. **Encapsulation**:
   - The Element class encapsulates the properties of a chemical element, such as its symbol and atomic number. These properties are protected by private fields and accessed through public methods to ensure data integrity.
   - The PeriodicTableGame class manages the game state (e.g., current score, question number) privately, interacting with these states using public methods such as askQuestion() and checkAnswer().
2. **Inheritance**:
   - Although the current implementation doesn’t require inheritance, the design allows for future extensions. For example, additional subclasses could be created to handle different categories of questions or advanced game modes, inheriting core behaviors from the PeriodicTableGame class.

3. **Polymorphism**:
   - Polymorphism is demonstrated with method overriding. For example, the SubmitButtonListener and NextQuestionButtonListener classes implement the ActionListener interface, providing different behaviors when their respective buttons are clicked.

4. **Abstraction**:
   - The Element class serves as an abstract representation of a chemical element, exposing only essential properties like symbol and atomic number, while hiding implementation details.
   - The PeriodicTableGame class abstracts the game logic behind methods like askQuestion(), checkAnswer(), and displayFinalScore(), simplifying interaction for the user.

---

## III. Sustainable Development Goal (SDG) Integration

### SDG 4: Quality Education

The Elemental Explorer aligns with **SDG 4: Quality Education** by promoting accessible, interactive learning in chemistry. It contributes to the following:

1. **Enhancing Learning**:
   - Offers an engaging way to explore chemistry through games and interactive tools.
   - Helps users memorize element symbols, atomic numbers, and properties.

2. **Encouraging Curiosity**:
   - The game and viewer encourage curiosity and deeper exploration of science topics.

3. **Inclusive Design**:
   - Designed to be user-friendly for learners of all ages and educational levels.

---

## IV. Instructions for Running the Program

### Prerequisites:
- **PJava Development Kit (JDK) version 8** or higher.
- A compatible IDE or text editor such as IntelliJ IDEA, Eclipse, or Visual Studio Code.

### Steps to Run:

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-username/periodic-table-game.git
   cd periodic-table-game
2. **Compile the Java Files (if not using an IDE):**:
   ```bash
   javac PeriodicTableGame.java
3. **Run the Game:**:
   ```bash
   java PeriodicTableGame
- The game window will appear, where you can begin answering questions about chemical elements.

### Game Controls:
- **Submit**: Submit your answer to the current question.
- **Next Question**: Move to the next question after submitting your answer.
- **Retry**: Retake the game after viewing your final score.
- **Study Area**: View the periodic table for reference (opens in a new window).
- **Help**: View the game instructions and rules.

---

## V. Folder Structure
- Follow the Folder Structure to fully utilize the program
  ```bash
    Periodic-Table-Game/
    │
    ├── src/
    │   ├── PeriodicTableGame.java   # Main game file
    │   ├── Element.java             # Class representing elements
    │   ├── StudyArea.java          # Displays the periodic table
    │   ├── HelpGuide.java          # Provides help and instructions
    │
    └── README.md                   # This README file


---

## VI. Key Features

### Periodic Table Game:
Gameplay:
- Answer questions on the atomic number and symbol of chemical elements.
- Questions are randomly selected, providing diverse gameplay each time.

Feedback:
- Immediate feedback on the correctness of answers.
- Displays a final score after completing all questions.

### Periodic Table Viewer:
Interactive Table:
- View and explore detailed information about elements (atomic number, symbol, weight, and category).
Educational Information:
- Categorizes elements by groups and periods, highlighting their properties and states.
Study Area:
- Access the periodic table for reference during gameplay.
Help Guide:
- Offers detailed instructions for using the application.

---

## VII. Explanation of Key Functions
- ### Explain how the code works and what parts are responsible for running the program.
  
  ```bash
  __init__(self): Initializes the game, setting up the GUI window, layout, and appearance.
  create_widgets(self): Creates and places all interactive elements in the GUI window.
  start_game(self): Validates user input (number of questions) and starts the quiz.
  check_answer(self): Compares user input with the correct answer, updating the score and providing feedback.
  ask_question(self): Randomly selects a new question and updates the user interface.
  display_final_score(self): Shows the user’s final score after the quiz and provides options to retry or explore the periodic table.
  
---

### Thank You for Using Elemental Explorer!

We sincerely appreciate you choosing the Periodic Table Game as your learning tool. We hope it has helped you explore and enjoy the fascinating world of elements. Keep learning and feel free to return anytime for more fun with the periodic table!

### Happy learning!

  




  
