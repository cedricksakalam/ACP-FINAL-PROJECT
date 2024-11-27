# Elemental Explorer

---

## I. Project Overview

The provided code is a Python application built using the Tkinter library for creating graphical user interfaces (GUIs). It serves as the foundation for the Elemental Explorer, a quiz-based periodic table learning tool. The code implements a structured, interactive framework that manages different aspects of the user experience, from data handling to interface interactions. It includes two main features:

1. **Periodic Table Viewer**: View and explore detailed information about chemical elements, their properties, and their positions in the periodic table.
2. **Periodic Table Game**: A quiz-style game that challenges users to answer questions about element symbols and atomic numbers, promoting learning through play.

Elemental Explorer aims to make learning chemistry fun and accessible, catering to students, educators, and enthusiasts alike.

---

## II. Python Concepts, Libraries, and Features

This project demonstrates the following Python concepts and libraries:

1. **Tkinter GUI**:
   - A user-friendly graphical interface with buttons, labels, and entry fields for intuitive navigation.
   - Icons and custom styles to enhance user experience.
   - Canvas graphics for displaying the periodic table.

2. **Random Library**:
   - Generates random questions for diverse gameplay.

3. **Object-Oriented Programming (OOP)**:
   - Encapsulation of application functionality into classes and methods for modularity and reusability.

4. **Error Handling and Input Validation**:
   - Ensures users provide valid inputs before proceeding:
     - Displays prompts for incomplete fields, such as missing number of questions.
     - Prevents invalid entries like numbers outside the range of 1–100.

5. **Dynamic Feedback**:
   - Provides real-time feedback for quiz answers, such as correct/incorrect responses and the final score.

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
- **Python 3.9** or later installed on your machine.
- The following dependencies must be installed (pre-installed with Python):
  - `tkinter`
  - `random`
- Ensure the image file `Icon.ico` is placed in the `src/` directory.

### Steps to Run:

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-repository-name/Elemental-Explorer.git
   cd Elemental-Explorer
2. **Run the Game**:
- Launch the game by running the following command:
   ```bash
   python src/gameGUI.py
- Play the game by answering questions about the periodic table. The score is displayed at the end, with options to retake the quiz or explore the periodic table.
3. **Access the Periodic Table Viewer**:
- Run the following command:
  ```bash
  python src/periodicTableGUI.py
4. **Use the Help Guide**:
- Learn how to navigate the program by running:
  ```bash
  python src/helpGuide.py

---

## V. Folder Structure
- Follow the Folder Structure to fully utilize the program
  ```bash
  Project/
   │
   ├── src/
   │   ├── gameGUI.py             # Main game file
   │   ├── periodicTableGUI.py    # Periodic table viewer
   │   ├── Icon.ico               # Application icon
   │   ├── helpGuide.py           # Help guide for users
   │
   └── README.md                  # This README file

---

## VI. Key Features

### Periodic Table Game:
Gameplay:
- Answer up to 100 multiple-choice questions about chemical elements.
- Questions focus on element symbols and atomic numbers, chosen randomly.
Feedback:
- Displays correct answers for wrong responses and tracks scores.

### Periodic Table Viewer:
Interactive Table:
- Clickable elements provide detailed properties (e.g., atomic number, weight, and category).
Educational Information:
- Categorizes elements by groups and periods, highlighting their properties and states.
Retry and Explore Options:
- Replay the game or switch to the Study Area after completing the game.
Help Guide:
- Offers detailed instructions for using the application.

---

## VII. Explanation of Key Functions
- ### Explain how the code works and what parts are responsible for running the program.
  
  ```bash
  1. __init__(self)
- 1. Initializes the main application, setting up the GUI, window size, and appearance.
  ```bash
  2. create_widgets(self)
- 2. Creates and places all interactive elements in the main application window, including buttons and labels.
  




  
