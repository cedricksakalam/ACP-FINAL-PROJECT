# Elemental Explorer

---

## I. Project Overview

Elemental Explorer is an educational and interactive application designed to make learning the periodic table fun and engaging. It challenges players to test their knowledge of chemical elements through a gamified experience while offering additional features to encourage continuous learning and improvement.

In this program, users can participate in a trivia-style game where they answer questions about element symbols, atomic numbers, and other properties. Elemental Explorer incorporates a database to manage user data, such as tracking high scores on the leaderboard and collecting user feedback. This ensures a seamless experience by saving progress, maintaining rankings, and enabling data-driven improvements to the application. The app also includes a study area for deeper exploration of the periodic table, providing a well-rounded educational tool.

With an intuitive interface, smooth animations, and a focus on accessibility, Elemental Explorer is perfect for students, educators, or anyone interested in chemistry.

---

## Application of Python Concepts and Libraries

This section explains various Python programming techniques and external libraries were utilized to build and enhance the functionality of the project.

1. **Functions**:
   - Lists below are functions used to run the program.
     ```bash
     init_db() - Initializes the SQLite database and creates the necessary tables (leaderboard and feedback).
     > It establishes a connection to the SQLite database (leaderboard.db).
     > Executes SQL queries to create the tables, ensuring they exist.
     > The leaderboard table stores username and score, while the feedback table stores username, feedback, and a timestamp.

     add_score(username, score) - Adds a score to the leaderboard for a given user, or updates the score if the user already has a higher score.
     > Checks if the username already exists in the leaderboard table.
     > If the username exists, it updates the score if the new score is higher than the existing one.
     > If the username does not exist, it inserts a new record into the leaderboard table with the provided score.

     get_leaderboard() - Retrieves the top 10 scores from the leaderboard table.
     > Selects the username and score columns from the leaderboard table.
     > Orders the results by score in descending order, limiting the results to the top 10.

     reset_leaderboard_db() -  Resets the leaderboard by deleting all entries in the leaderboard table.
     > Executes a DELETE statement to remove all records from the leaderboard table.

     add_feedback(username, feedback) - Adds feedback from the user to the feedback table.
     > Validates that the username and feedback are not empty.
     > Inserts the feedback into the feedback table, with the username and the text of the feedback.
     > Handles any exceptions that may occur during the insertion.

     get_feedback() - Retrieves all feedback from the feedback table.
     > Selects username, feedback, and timestamp columns from the feedback table.
     > Orders the results by the timestamp in descending order.

     UNDER CLASS APP
     create_widgets() - Creates and arranges the widgets for the main application window.
     > Sets up labels, entry fields, and buttons for the user interface, allowing users to input their name and start the game.
     > Also includes the "Help" button that leads to a help window.

     start_game() - Starts the game by validating the username and transitioning to the game window.
     > Ensures the username entered is valid (contains only alphanumeric characters).
     > Disables the name entry field and start button after the game begins.
     > Calls the create_game_window() function to initialize the game.

     help() - Opens the help window by importing and displaying the help guide.
     > Calls a method from an external help_guide module (assumed to be a different file) to show instructions to the user.

     create_game_window() - Creates and opens the game window where the user will answer questions.
     > Initializes a new GameWindow instance and starts the game logic there.
     > Closes the main app window after transitioning to the game window.

     UNDER CLASS GameWindow
     __init__(self, username) - Initializes the game window where the user will answer elemental questions.
     > "Sets up the window's title, geometry, background, and a GIF for the background."
     > Sets the initial question count and score, and calls create_game_widgets() to generate the game interface.

     create_game_widgets() - Creates and arranges the widgets for the game window, where the user will interact with the questions.
     > Sets up labels, buttons, and entry fields for answering questions, displaying feedback, and controlling the game flow (e.g., next question, retry, study area, etc.).

     ask_question() - Asks a new question from the periodic table and displays it in the window.
     > Chooses a random element and randomly asks either for its symbol or atomic number.
     > Updates the question label and prepares for the user's input.

     check_answer() - Checks the user's answer and provides feedback.
     > Compares the user's answer to the correct one and provides a "Correct!" or "Wrong!" message accordingly.

     next_question() - Moves to the next question in the game.
     > "Increases the question count and calls ask_question() to load the next question."

     display_final_score() - Displays the final score after all questions are answered.
     > Shows the user’s final score and disables further interactions with the game.
     > Calls add_score() to save the user’s score in the leaderboard.
     > Enables the "Retry", "Study Area", "View Leaderboards" buttons.

     retry_game() - Allows the user to retry the game.
     > Saves the current score in the leaderboard.
     > Closes the current game window and reopens the main app window to start fresh.

     study_area() - Opens the study area for the user to learn more about the periodic table.
     > Calls a method from the studyArea module to display additional learning resources.

     open_feedback_window() - Opens a window where the user can submit feedback.
     > Displays a text entry field for the user to enter feedback.
     > Submits the feedback to the database using the add_feedback() function.

     view_feedback() - Opens a window to display all user feedback.
     > Displays feedback stored in the database in a Treeview widget with columns for username, feedback, and timestamp.

     show_leaderboard() - Displays the leaderboard showing top scores.
     > Retrieves the top scores from the database and displays them in a Treeview widget.
     > Includes a "Reset Leaderboard" button to clear the leaderboard data from the database.
          reset_leaderboard(self) - Resets the leaderboard by deleting all entries from the database.
          > Prompts the user for confirmation and then calls reset_leaderboard_db() to clear the leaderboard. 
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
    │   ├── gameGUI.py              # Main game file
    │   ├── periodicTableGUI        # Displays the periodic table
    │   ├── helpGuide.java          # Provides help and instructions
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

  




  
