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
