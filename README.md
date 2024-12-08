# Elemental Explorer

---

## I. Project Overview

Elemental Explorer is an educational and interactive application designed to make learning the periodic table fun and engaging. It challenges players to test their knowledge of chemical elements through a gamified experience while offering additional features to encourage continuous learning and improvement.

In this program, users can participate in a trivia-style game where they answer questions about element symbols, atomic numbers, and other properties. Elemental Explorer incorporates a database to manage user data, such as tracking high scores on the leaderboard and collecting user feedback. This ensures a seamless experience by saving progress, maintaining rankings, and enabling data-driven improvements to the application. The app also includes a study area for deeper exploration of the periodic table, providing a well-rounded educational tool.

With an intuitive interface, smooth animations, and a focus on accessibility, Elemental Explorer is perfect for students, educators, or anyone interested in chemistry.

---

## II. Application of Python Concepts and Libraries

This section explains various Python programming techniques and external libraries were utilized to build and enhance the functionality of the project.

### 1. Libraries
   - Lists below are the libraries used to run the program.
      - tkinter: Implements the graphical user interface, creating visually structured windows, buttons, labels, and other elements for the application.
      - sqlite3: Provides a lightweight database for persisting user data such as scores and feedback.
      - Pillow: Enhances the GUI by managing image rendering, including animated GIFs, ensuring a polished visual presentation.
      - random: Generates randomized questions to keep the game dynamic and challenging.
      - re: Validates user input, ensuring usernames conform to acceptable standards.
      - ttk: Used for advanced widgets like Treeview to display leaderboard and feedback tables.
      
### 2. Python Concepts
**Tkinter (GUI Programming)**
   - **Tkinter Basics**: Builds a GUI using Tkinter, the standard library for GUI development in Python. It includes windows, labels, buttons, input fields, and frames.
   - **Event Handling**: Buttons and input fields trigger actions, such as starting the game, submitting answers, or showing feedback, using the `command` attribute to link actions to Python functions.
   - **Layouts**: Utilizes layout management techniques (`pack()`, `place()`, `grid()`) to organize widgets within the window.

**Database (SQLite)**
   - **SQLite Database**: Uses the `sqlite3` module to store user scores, feedback, and user details (e.g., username, age) in a lightweight database.
   - **CRUD Operations**: Implements basic CRUD (Create, Read, Update, Delete) operations:
     - **Create**: Defines table structures for leaderboard, feedback, and users using `CREATE TABLE` statements.
     - **Read**: Retrieves data using `SELECT` queries (e.g., `get_users()`, `get_leaderboard()`, `get_feedback()`).
     - **Update**: Updates user scores in the leaderboard if a new score is higher.
     - **Delete**: Clears the leaderboard using the `DELETE` statement.

**Random Module**
   - Uses the `random` module to select elements randomly (e.g., generating random questions) during gameplay with functions like `random.choice()`.

**Regular Expressions (Regex)**
   - Implements input validation using `re.match()` to ensure that usernames contain only alphanumeric characters, preventing invalid symbols or spaces.

**Object-Oriented Programming (OOP)**
   - **Classes and Inheritance**: Defines classes (`App`, `GameWindow`) representing different game windows, inheriting from Tkinter classes (`tk.Tk`, `tk.Toplevel`).
   - **Methods and Attributes**: Methods like `create_widgets()`, `ask_question()`, and `check_answer()` define behaviors, while attributes like `username`, `score`, and `question_count` store game state.
   - **Encapsulation**: Keeps internal states (e.g., `self.username`, `self.age`) private within classes, manipulated through methods.

**File I/O**
   - **Image Handling**: Uses Pillow (PIL) to load and display GIFs for background animation. The `Image.open()` and `ImageTk.PhotoImage()` methods enable displaying images in Tkinter windows.
   - **File Paths**: Uses absolute file paths for resources like icons and backgrounds (e.g., `C:/Users/ced/Elemental Explorer/Program/Icon.ico`), though it's advisable to handle paths dynamically for deployment.

**Error Handling**
   - Implements `try-except` blocks for database operations and other critical functions to handle potential errors (e.g., connection issues) gracefully. Displays error messages using `messagebox.showerror()`.

**List and Dictionary Manipulation**
   - **Dictionaries**: Uses dictionaries (e.g., `ELEMENTS`) to store properties of elements like names, symbols, and atomic numbers, allowing easy access during the game.
   - **Lists**: Manages background animation frames using lists, updating them periodically with `self.after()` to create an animated effect.

**Multithreading (Background Updating)**
   - Uses `after()` for asynchronous updates to the background, allowing continuous changes to frames and creating the illusion of an animated GIF background.

**Window Management**
   - **Main Window (App)**: Manages user input (name, age) and launches the game.
   - **Game Window (GameWindow)**: Displays questions and tracks user interactions.
   - **Feedback and Leaderboard Windows**: Dynamically created using `Toplevel` windows to show additional content without closing the main window.

**Advanced Widgets and Customization**
   - **Treeview**: Uses the `Treeview` widget to display leaderboard scores and feedback in a tabular format, with scrollbars for easy navigation.
   - **Combobox**: Implements a `Combobox` widget for selecting user age, with a limited range of values (1-100).

**Dynamic State Updates**
   - Dynamically updates the state of buttons and input fields based on the game flow. For example, the "Start Game" button is disabled after the game begins, and the "Retry" button is enabled at the end.

**Game Logic**
   - **Score Keeping**: Tracks and updates the user’s score by comparing their answers to the correct ones. The score is displayed at the end of the game.
   
   - **Question Flow**: The game proceeds by asking questions, checking if the answers are correct, and moving to the next question. The game continues until all questions are answered or the game ends.

---

## III. Sustainable Development Goal (SDG) Integration

## SDG 4: Quality Education

The program "Elemental Explorer" aligns primarily with SDG 4: Quality Education, which is centered around ensuring inclusive, equitable, and quality education for all, and promoting lifelong learning opportunities.

Enhancing STEM Education SDG 4 specifically calls for the improvement of education in science, technology, engineering, and mathematics (STEM). By focusing on chemistry and the periodic table, "Elemental Explorer" contributes directly to this goal. It encourages students to explore fundamental scientific concepts in a gamified setting, which may inspire greater interest in STEM fields. In the long term, this can help cultivate a more scientifically literate population that is better equipped to engage with contemporary challenges, such as sustainability, innovation, and technological advancement.

---

## IV. Instructions for Running the Program

### Steps to Run:

1. **Download the project files as a ZIP and extract them to your preferred folder.**

2. **Step 2: Install Required Libraries**:
Ensure Python is installed on your system. Then, open your terminal or command prompt and install the required libraries:
   ```bash
   pip install sqlite3
   pip install Pillow
- This library is used to create tables, databases, and etc..

4. **Step 3: Download required Extensions**:
   ```bash
   Extensions: sqlite viewer, PIL
- This extension helps to view the databases, and utilize images.

5. **Step 4: FollowFolder Structure**

- Follow the Folder Structure to fully utilize the program
  ```bash
    ACP - Final Project
   ├── Project/
   │   ├── main.py                # Main game file
   │   ├── studyArea.py           # Displays the periodic table
   │   ├── help_guide.py          # Provides help and instructions
   │   ├── classes.py             # Handles core class definitions
   │   ├── elements.py            # Manages element-related functionalities
   │   ├── db.py                  # Handles database interactions
   │   ├── images/
   │   │   ├── bg.gif             # Background image for the game
   │   │   └── Icon.ico           # Application icon
   │
   └── README.md                  # Project documentation


---

For more visual presentation just click this link!! https://drive.google.com/file/d/1mB5Ba0ZUOOzuXylhpXbm-Y68csisAegX/view?usp=sharing





  
