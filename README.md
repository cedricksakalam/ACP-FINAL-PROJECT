# Elemental Explorer

---

## I. Project Overview

Elemental Explorer is an educational and interactive application designed to make learning the periodic table fun and engaging. It challenges players to test their knowledge of chemical elements through a gamified experience while offering additional features to encourage continuous learning and improvement.

In this program, users can participate in a trivia-style game where they answer questions about element symbols, atomic numbers, and other properties. Elemental Explorer incorporates a database to manage user data, such as tracking high scores on the leaderboard and collecting user feedback. This ensures a seamless experience by saving progress, maintaining rankings, and enabling data-driven improvements to the application. The app also includes a study area for deeper exploration of the periodic table, providing a well-rounded educational tool.

With an intuitive interface, smooth animations, and a focus on accessibility, Elemental Explorer is perfect for students, educators, or anyone interested in chemistry.

---

## Application of Python Concepts and Libraries

This section explains various Python programming techniques and external libraries were utilized to build and enhance the functionality of the project.
1. ### **Libraries**
   - Lists below are the libraries used to run the program.
   ```bash
   tkinter: Implements the graphical user interface, creating visually structured windows, buttons, labels, and other elements for the application.
   sqlite3: Provides a lightweight database for persisting user data such as scores and feedback.
   Pillow: Enhances the GUI by managing image rendering, including animated GIFs, ensuring a polished visual presentation.
   random: Generates randomized questions to keep the game dynamic and challenging.
   re: Validates user input, ensuring usernames conform to acceptable standards.
   ttk: Used for advanced widgets like Treeview to display leaderboard and feedback tables.

3. ### **Functions**:
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
     create_game_widgets() - Creates and arranges the widgets for the game window, where the user will interact with the questions.
     > Sets up labels, buttons, and entry fields for answering questions, displaying feedback, and controlling the game flow (e.g., next question, retry, study area, etc.).

     ask_question() - Asks a new question from the periodic table and displays it in the window.
     > Chooses a random element and randomly asks either for its symbol or atomic number.
     > Updates the question label and prepares for the user's input.

     check_answer() - Checks the user's answer and provides feedback.
     > Compares the user's answer to the correct one and provides a "Correct!" or "Wrong!" message accordingly.

     next_question() - Moves to the next question in the game.
     > Increases the question count and calls ask_question() to load the next question.

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
3. ### **Exception Handling**
Used extensively (e.g., in database interactions and feedback submission) to manage errors gracefully.
1. Input Validation: Catching invalid user inputs (e.g., non-numeric values) using try-except blocks.
2. Database Error Handling: Wrapping database-related operations (e.g., creating tables, executing queries) in try-except blocks to catch sqlite3.DatabaseError.
3. File Handling Errors: Managing errors when working with files, such as missing files or unsupported file types (e.g., images), using try-except.
4. General Exception Handling: Catching all unexpected errors with a general Exception block to prevent crashes.
     
3. ### **OOP-Concepts**:
   1. **Classes and Objects**
   Class - A blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from it will have.
   Object - An instance of a class, representing a specific entity with the structure defined by the class.
   In the code:
   > The App class is a template for the main application window. When the script runs, an instance of this class (app) is created, which represents the main application object.
   > The GameWindow class is used to define a window for the game. An object of this class is created when a game session starts.
   
   2. **Encapsulation**
   Encapsulation involves bundling data (attributes) and methods (functions) within a class and restricting access to some components. This ensures that data is not directly accessible, improving modularity and security.
   In the code:
   > Attributes like self.username, self.question_count, and self.score in GameWindow are encapsulated within the class. These attributes can only be modified using methods of the class.
   > The database interaction functions like add_score and get_leaderboard encapsulate the logic for interacting with the database, preventing direct access.
   
   3. **Inheritance**
   Inheritance allows a class (child) to inherit attributes and methods from another class (parent), enabling code reuse and extending functionality.
   In the code:
   > GameWindow inherits from tk.Toplevel, which is a class in the tkinter library for creating secondary windows. This inheritance allows GameWindow to use and extend the functionality of Toplevel.

   4. **Polymorphism**
   Polymorphism allows methods in different classes to have the same name but behave differently based on the object invoking them. It can be achieved through method overriding or overloading.
   In the code:
   > The load_gif method is defined in both App and GameWindow. While the method name is the same, its behavior depends on the context (i.e., whether it's being called in App or GameWindow).

   5. **Abstraction**
   Abstraction involves hiding complex implementation details and exposing only what is necessary. This helps reduce complexity for the user.
   In the code:
   > The database initialization logic (init_db) and other database interaction methods (add_score, get_leaderboard) abstract away the details of SQL queries. The main program doesn't need to know how data is stored or       retrieved.
   > The update_background method abstracts the logic for handling GIF frames, so the main logic doesn't deal with animation intricacies.

---

## III. Sustainable Development Goal (SDG) Integration

## SDG 4: Quality Education

The program "Elemental Explorer" aligns primarily with SDG 4: Quality Education, which is centered around ensuring inclusive, equitable, and quality education for all, and promoting lifelong learning opportunities.

Enhancing STEM Education SDG 4 specifically calls for the improvement of education in science, technology, engineering, and mathematics (STEM). By focusing on chemistry and the periodic table, "Elemental Explorer" contributes directly to this goal. It encourages students to explore fundamental scientific concepts in a gamified setting, which may inspire greater interest in STEM fields. In the long term, this can help cultivate a more scientifically literate population that is better equipped to engage with contemporary challenges, such as sustainability, innovation, and technological advancement.

---

## IV. Instructions for Running the Program

### Steps to Run:

1. **Step 1: Clone or Download the Project**:
   ```bash
   git clone https://github.com/your-username/periodic-table-game.git
OR

Download the project files as a ZIP and extract them to your preferred folder.

2. **Step 2: Install Required Libraries**:
Ensure Python is installed on your system. Then, open your terminal or command prompt and install the required libraries:
   ```bash
   pip install sqlite3
- This library is used to create tables, databases, and etc..
- 
4. **Step 3: Download required Extensions**:
   ```bash
   Extensions: sqlite viewer
- This extension helps to view the databases.

5. **Step 4: FollowFolder Structure**

- Follow the Folder Structure to fully utilize the program
  ```bash
    ACP/
    │
    ├── Project/
    │   ├── main.py                # Main game file
    │   ├── studyArea.py           # Displays the periodic table
    │   ├── help_guide.py          # Provides help and instructions
    │   ├── bg.gif                 
    |   ├── helpbg.gif
    |   ├── Icon.ico
    |      
    └── README.md                   # This README file

---

## ACKNOWLEDGEMENT

- In God, that I always trust.
- Ma'am Fatima
- Random Guy sa Reddit
- CoF na mas madaming ml kesa gawa
- kay B-jork





  
