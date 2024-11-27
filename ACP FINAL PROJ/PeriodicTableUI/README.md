#Elemental Explorer README

##I. *Project Overview*
  Elemental Explorer is an interactive and educational application designed to enhance knowledge about the periodic table and its elements.
    It includes two main features:

    Periodic Table Viewer: View and explore detailed information about chemical elements, their properties, and their positions in the periodic table.
    Periodic Table Game: A quiz-style game that challenges users to answer questions about element symbols and atomic numbers, promoting learning through play.

 II. *Python Concepts, Libraries, and Applications*
  This project leverages core Python programming concepts and libraries, such as:

    1. Tkinter: The GUI toolkit used to create an interactive and visually appealing user interface.
    2. Random: For generating random questions in the game module, ensuring diverse gameplay.
    3. Object-Oriented Programming (OOP): Encapsulation of application functionality into classes and methods for modularity and reusability.
    4. Custom Widgets: Integration of buttons, labels, and other GUI elements for seamless navigation.
    5. Canvas and Graphics: Displaying a periodic table background and interactive elements.

 III. *Chosen SDG and Its Integration*
   The project aligns with Sustainable Development Goal (SDG) 4: Quality Education by providing an engaging and innovative platform for science education. Through the game mode, learners can test their understanding of chemistry fundamentals, and the periodic table viewer enables users to explore detailed properties of elements in an interactive way.

 IV. Instructions for Running the Program
  Prerequisites
   1. Python 3.9 or later installed on your machine.
   2. The following dependencies must be installed:
     > tkinter (usually included in the standard Python library).
   3. Ensure the image files (Icon.ico and background1.png) are located in the specified directories.

  *Running the Application*
   1. Main Application - The Game
    - Launch the game by running the following command in your terminal or IDE:
      python MainGameGUI.py
      - Play the game by answering questions about the periodic table. Scores will be displayed at the end, with options to retake the quiz or view the periodic table.
   2. Periodic Table Viewer
    - Access the periodic table viewer by selecting "View Periodic Table" at the end of the quiz, or by running the following command directly:
      python PeriodicTableViewer.py
      - Click on any element in the table to learn about its atomic number, weight, state, and category.

 *Folder Structure*

  Project/
  │
  ├── src/
  │   ├── MainGameGUI.py          # Main game file (includes the quiz)
  │   ├── PeriodicTableViewer.py  # Periodic table viewer
  │   ├── Icon.ico                # Application icon
  │   ├── background1.png         # Background image for the game
  │
  └── README.md                   # This README file
  *Key Features*
    1. Periodic Table Game
    Gameplay:
      Users answer 25 multiple-choice questions about chemical elements.
      Questions focus on element symbols and atomic numbers, chosen randomly.
    Feedback:
      Correct answers earn points, and incorrect answers display the correct response.
    2. Periodic Table Viewer
    Interactive Table:
      Clickable elements provide detailed properties (e.g., atomic number, weight, category).
      Organized by groups and periods with color-coded categories.
    Educational Information:
      Covers comprehensive information about the elements, including their physical states (such as solid, gas, or synthetic) and classifications (e.g., alkali metals, transition metals).
    3. Retake and Explore Options
    At the end of the game, users can:
      Retake the quiz.
      Switch to the periodic table viewer.

 Enjoy exploring the elements and testing your knowledge with Elemental Explorer!
