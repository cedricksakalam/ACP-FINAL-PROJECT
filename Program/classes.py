import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import random
import re  
from elements import ELEMENTS
from db import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Elemental Explorer")
        self.geometry("1920x1080")
        self.iconbitmap('C:/Users/ced/Elemental Explorer/Program/images/Icon.ico')
        self.config(bg='#485540')

        # Initialize database
        init_db()

        self.frames = self.load_gif('C:/Users/ced/Elemental Explorer/Program/images/bg.gif')
        self.current_frame_index = 0
        self.bottom_canvas = tk.Canvas(self, bg='#485540', highlightthickness=0)
        self.bottom_canvas.pack(side="bottom", fill="x")
        self.background_label = tk.Label(self.bottom_canvas, bg='#485540')
        self.background_label.pack()
        self.update_background()

        #Username and age placeholder
        self.username = None
        self.age = None

        self.create_widgets()

    def load_gif(self, filepath):
        gif = Image.open(filepath)
        frames = []
        bg_color = (72, 85, 64)

        try:
            while True:
                frame = gif.convert("RGBA")
                background = Image.new("RGBA", frame.size, bg_color)
                composite = Image.alpha_composite(background, frame)
                frames.append(ImageTk.PhotoImage(composite))
                gif.seek(len(frames))
        except EOFError:
            pass
        return frames

    def update_background(self):
        frame = self.frames[self.current_frame_index]
        self.background_label.config(image=frame)
        self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
        self.after(100, self.update_background)
        
    def create_widgets(self):
        self.label = tk.Label(self, text="Elemental Explorer", bg='#485540', font=("Arial", 80, "bold"), fg='#80986a')
        self.label.pack(pady=100)

        self.label = tk.Label(self, text="Put your knowledge to the test in Elemental Guesser.\nHow well can you name the elements of the periodic table before your mind runs out of clues?", bg='#485540', font=("Papyrus", 20, "bold"), fg='#80986a')
        self.label.pack(pady=0)

        self.label = tk.Label(self, text="Enter your name and age to play:", bg='#485540', font=("Arial", 25, "bold"), fg='#80986a')
        self.label.pack(pady=20)

        self.name_entry = tk.Entry(self, font=("Arial", 15, "bold"), bg='#b9cea4', fg='#395f25')
        self.name_entry.pack(pady=10)

        self.age_label = tk.Label(self, text="Select your age:", bg='#485540', font=("Arial", 20, "bold"), fg='#80986a')
        self.age_label.pack(pady=10)

        self.age_combobox = ttk.Combobox(self, values=list(range(1, 101)), font=("Arial", 15, "bold"), state="readonly", width=5)
        self.age_combobox.set(18)
        self.age_combobox.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Game", bg='#485540', fg='#80986a', font=("Georgia", 20), command=self.start_game)
        self.start_button.pack(pady=10)

        self.help_button = tk.Button(self, text="Help", bg='#b9cea4', font=("Georgia", 20), command=self.help)
        self.help_button.place(relx=0.95, rely=0.95, anchor="se")

    def start_game(self):
        username = self.name_entry.get().strip()
        age_str = self.age_combobox.get().strip()

        # Validate the username with regex
        if not re.match(r'^[a-zA-Z0-9]+$', username):
            messagebox.showwarning("Invalid Name", "Username must consist of only letters and numbers (no spaces or special characters).")
            return

        if not username:
            messagebox.showwarning("Invalid Name", "Please enter a valid name.")
            return

        # Validate the age
        if not age_str.isdigit() or int(age_str) <= 0:
            messagebox.showwarning("Invalid Age", "Please select a valid age (positive integer).")
            return
        
        age = int(age_str)

        self.username = username  # Set the username
        self.age = age  # Set the age
        self.name_entry.config(state="disabled")
        self.age_combobox.config(state="disabled")
        self.start_button.config(state="disabled")
        self.withdraw()

        self.create_game_window()
    
    def help(self):
        self.destroy()  
        from help_guide import Help
        help_window = Help()  
        help_window.flash_instructions()
        help_window.mainloop()

    def create_game_window(self):
        self.game_window = GameWindow(self.username, self.age)
        self.game_window.mainloop()
        self.destroy()

class GameWindow(tk.Toplevel):
    def __init__(self, username, age):
        super().__init__()
        self.title("Elemental Explorer - Game")
        self.geometry("1920x1080")
        self.iconbitmap('C:/Users/ced/Elemental Explorer/Program/images/Icon.ico')
        self.config(bg='#485540')

        self.username = username
        self.age = age
        self.question_count = 1
        self.score = 0
        self.total_questions = 5.

        self.frames = self.load_gif('C:/Users/ced/Elemental Explorer/Program/images/bg.gif')
        self.current_frame_index = 0
        self.bottom_canvas = tk.Canvas(self, bg='#485540', highlightthickness=0)
        self.bottom_canvas.pack(side="bottom", fill="x")
        self.background_label = tk.Label(self.bottom_canvas, bg='#485540')
        self.background_label.pack()
        self.update_background()

        self.create_game_widgets()

    def load_gif(self, filepath):
        gif = Image.open(filepath)
        frames = []
        bg_color = (72, 85, 64) 
        try:
            while True:
                frame = gif.convert("RGBA")
                background = Image.new("RGBA", frame.size, bg_color)
                composite = Image.alpha_composite(background, frame)
                frames.append(ImageTk.PhotoImage(composite))
                gif.seek(len(frames))
        except EOFError:
            pass
        return frames

    def update_background(self):
        frame = self.frames[self.current_frame_index]
        self.background_label.config(image=frame)
        self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
        self.after(100, self.update_background) 

    #Create widgets 
    def create_game_widgets(self):
        self.label = tk.Label(self, text="Elemental Explorer", bg='#485540', font=("Arial", 80, "bold"), fg='#80986a')
        self.label.pack(pady=20)

        self.item_number_label = tk.Label(self, text=f"Question: {self.question_count}", bg='#485540', font=("Arial", 30, "bold"), fg='#80986a')
        self.item_number_label.pack(pady=20)

        self.question_label = tk.Label(self, text="", bg='#485540', font=("Arial", 35, "italic", "bold"), fg='#80986a')
        self.question_label.pack(pady=0)

        self.entry = tk.Entry(self, bg='#b9cea4', fg='#395f25', font=("Arial", 20))
        self.entry.pack(pady=20)

        button_frame = tk.Frame(self, bg='#485540')
        button_frame.pack(pady=20)

        self.submit_button = tk.Button(button_frame, text="Submit", font=("Georgia", 18), bg='#80986a', command=self.check_answer)
        self.submit_button.pack(side="left", padx=10)

        self.next_question_button = tk.Button(button_frame, text="Next Question", bg='#80986a', font=("Georgia", 18), command=self.next_question)
        self.next_question_button.pack(side="left", padx=10)

        self.feedback_label = tk.Label(self, text="", bg='#485540', font=("Georgia", 20), fg="green")
        self.feedback_label.pack(pady=20)

        self.retake_button = tk.Button(self, text="Retry", bg='#80986a', font=("Georgia", 18), command=self.retry_game, state=tk.DISABLED)
        self.retake_button.pack(pady=15)

        self.study_area_button = tk.Button(self, text="Study Area", bg='#80986a', font=("Georgia", 18), command=self.study_area, state=tk.DISABLED)
        self.study_area_button.pack(pady=10)
        
        self.view_leaderboards_button = tk.Button(self, text="View Leaderboards", bg='#80986a', font=("Georgia", 18), command=self.show_leaderboard, state=tk.DISABLED)
        self.view_leaderboards_button.pack(pady=10)

        self.feedback_button = tk.Button(self, text="Give Feedback", bg='#b9cea4', font=("Georgia", 18), command=self.open_feedback_window)
        self.feedback_button.place(relx=0.10, rely=0.95, anchor="sw")
        
        self.view_feedback_button = tk.Button(self, text="View Feedback", bg='#b9cea4', font=("Georgia", 18), command=self.view_feedback)
        self.view_feedback_button.place(relx=0.90, rely=0.95, anchor="se")

        self.ask_question()

    #Generates Questions from "Element", by random
    def ask_question(self):
        if self.question_count > self.total_questions:
            self.display_final_score()
            return

        self.current_element = random.choice(list(ELEMENTS.keys()))
        question_type = random.choice(["symbol", "atomic_number"])

        if question_type == "symbol":
            self.question_label.config(
                text=f"What is the symbol for {self.current_element}?"
            )
            self.correct_answer = ELEMENTS[self.current_element]["symbol"]
        else:
            self.question_label.config(
                text=f"What is the atomic number of {self.current_element}?"
            )
            self.correct_answer = str(ELEMENTS[self.current_element]["atomic_number"])

        self.item_number_label.config(text=f"Question: {self.question_count}")
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    #Checks the answer, Incrementing to the score if correct
    def check_answer(self):
        user_answer = self.entry.get().strip().lower()
        correct_answer = self.correct_answer.lower()

        if user_answer != "":
            if user_answer == correct_answer:
                self.feedback_label.config(text="Correct!", fg="#46BDF1")
                self.score += 1
            else:
                self.feedback_label.config(
                    text=f"Wrong! The correct answer was {self.correct_answer}.", fg="orange"
                )
        else:
            self.feedback_label.config(text="Please enter an answer.", fg="black")

    #Increments the question
    def next_question(self):
        self.question_count += 1
        self.ask_question()

    #Displays Final Score
    def display_final_score(self):
        self.question_label.config(text="Test Complete!")
        self.submit_button.config(state="disabled")
        self.next_question_button.config(state="disabled")
        self.entry.config(state="disabled")
        self.feedback_label.config(
            text=f"Your final score is: {self.score} / {self.total_questions}", font=("Papyrus", 25, "bold"), fg="#46BDF1"
        )

        #Call add_score() to insert/update the user's score in the leaderboard
        add_score(self.username, self.score)

        #Enable Retry button and Study Area button
        self.retake_button.config(state=tk.NORMAL)
        self.study_area_button.config(state=tk.NORMAL)
        self.view_leaderboards_button.config(state=tk.NORMAL)

    def retry_game(self):
        #Save the current score and username to the leaderboard if it's not already saved
        add_score(self.username, self.score)

        self.destroy()
        self.master.deiconify() #Show the main window again (where the username is asked)

        #Re-enable the start button and the name entry field
        self.master.name_entry.config(state="normal")
        self.master.start_button.config(state="normal")
        
        #Clear the name entry field for a fresh start
        self.master.name_entry.delete(0, tk.END)
        
        self.master.age_combobox.config(state="readonly")
        self.master.age_combobox.set(18)

        #Reset the main window's username variable
        self.master.username = None
        #Disable the Study Area button
        self.study_area_button.config(state=tk.DISABLED)

    #Calls Study Area
    def study_area(self):
        from studyArea import main
        main()
    
    #Feedback window    
    def open_feedback_window(self):
        feedback_window = tk.Toplevel(self)
        feedback_window.title("Feedback")
        feedback_window.geometry("400x300")
        feedback_window.resizable(False, False)

        feedback_label = tk.Label(feedback_window, text="Enter your feedback:", font=("Arial", 14))
        feedback_label.pack(pady=10)

        feedback_entry = tk.Entry(feedback_window, font=("Arial", 12), width=40)
        feedback_entry.pack(pady=10)

        def submit_feedback():
            feedback = feedback_entry.get().strip()
            if feedback:
                try:
                    # Pass username, age, and feedback to add_feedback
                    add_feedback(self.username, self.age, feedback)
                    messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
                    feedback_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")  # Handle errors if they occur
            else:
                messagebox.showwarning("Invalid Feedback", "Please enter some feedback.")

        submit_button = tk.Button(feedback_window, text="Submit", font=("Arial", 14), command=submit_feedback)
        submit_button.pack(pady=10)

    def view_feedback(self):
        # This function will display the feedback in a Treeview
        self.feedback_window = tk.Toplevel(self)
        self.feedback_window.title("Feedback")

        # Frame to hold Treeview and Scrollbar
        frame = ttk.Frame(self.feedback_window)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Treeview widget
        treeview = ttk.Treeview(frame, columns=("Username", "Age", "Feedback", "Timestamp"), show="headings")
        treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        treeview.heading("Username", text="Username")
        treeview.heading("Age", text="Age")
        treeview.heading("Feedback", text="Feedback")
        treeview.heading("Timestamp", text="Timestamp")

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview)
        treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill="y")

        # Fetch the feedback and display it in the Treeview
        conn = sqlite3.connect("PeriodicGame.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username, age, feedback, timestamp FROM feedback ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        conn.close()

        print(rows)  # Debugging output to check data retrieval

        for row in rows:
            treeview.insert("", tk.END, values=row)

        # Frame for the Back button
        button_frame = ttk.Frame(self.feedback_window)
        button_frame.pack(fill=tk.X, pady=10)

        # Back button to close the feedback window
        back_button = tk.Button(
            button_frame,
            text="Back",
            font=("Arial", 14),
            bg="#80986a",
            fg="white",
            command=self.feedback_window.destroy,
        )
        back_button.pack(pady=5)

    def show_leaderboard(self):
        #Get the leaderboard data
        leaderboard = get_leaderboard()

        leaderboard_window = tk.Toplevel(self)
        leaderboard_window.title("Leaderboard")
        leaderboard_window.geometry("700x700")
        leaderboard_window.resizable(False, False)

        title_label = tk.Label(leaderboard_window, text="Leaderboard", font=("Arial", 24, "bold"), fg="#485540")
        title_label.pack(pady=10)

        #Treeview widget to display the leaderboard in table format
        leaderboard_tree = ttk.Treeview(
            leaderboard_window,
            columns=("Place", "Username", "Score"),
            show="headings",
            height=20
        )
        leaderboard_tree.heading("Place", text="Place")
        leaderboard_tree.heading("Username", text="Username")
        leaderboard_tree.heading("Score", text="Score")
        
        leaderboard_tree.column("Place", width=100, anchor="center")
        leaderboard_tree.column("Username", width=300, anchor="w")
        leaderboard_tree.column("Score", width=150, anchor="center")
        leaderboard_tree.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        #Insert leaderboard data into the table
        for i, row in enumerate(leaderboard):
            leaderboard_tree.insert("", "end", values=(i + 1, row[0], row[1]))

        def reset_leaderboard(self):
            result = messagebox.askyesno(
                "Reset Leaderboard", 
                "Are you sure you want to reset the leaderboard? This action cannot be undone."
            )
            if result:
                try:
                    reset_leaderboard_db()  # Call the reset function

                    # Clear the Treeview (clear the leaderboard display)
                    leaderboard_tree.delete(*leaderboard_tree.get_children())

                    # Optionally, reset the leaderboard list if you want to clear the leaderboard variable too
                    leaderboard.clear()

                    messagebox.showinfo("Reset Successful", "The leaderboard has been reset.")
                except Exception as e:
                    print(f"Error during leaderboard reset: {e}") #for error handling
                    messagebox.showerror("Error", f"An error occurred while resetting the leaderboard: {e}")
                    
        reset_button = tk.Button(
            leaderboard_window,
            text="Reset Leaderboard",
            font=("Arial", 14),
            bg="#80986a",
            command=lambda: reset_leaderboard(self)  # Use lambda to pass self
        )

        reset_button.pack(pady=10)
        
        close_button = tk.Button(
            leaderboard_window,
            text="Close",
            command=leaderboard_window.destroy,
            font=("Arial", 14),
            bg="#80986a"
        )
        close_button.pack(pady=10)