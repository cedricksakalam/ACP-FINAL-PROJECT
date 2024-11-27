import tkinter as tk
import random

# Dictionary for the periodic table elements
ELEMENTS = {
    "Hydrogen": {"symbol": "H", "atomic_number": 1},
    "Helium": {"symbol": "He", "atomic_number": 2},
    "Lithium": {"symbol": "Li", "atomic_number": 3},
    "Beryllium": {"symbol": "Be", "atomic_number": 4},
    "Boron": {"symbol": "B", "atomic_number": 5},
    "Carbon": {"symbol": "C", "atomic_number": 6},
    "Nitrogen": {"symbol": "N", "atomic_number": 7},
    "Oxygen": {"symbol": "O", "atomic_number": 8},
    "Fluorine": {"symbol": "F", "atomic_number": 9},
    "Neon": {"symbol": "Ne", "atomic_number": 10},
    "Sodium": {"symbol": "Na", "atomic_number": 11},
    "Magnesium": {"symbol": "Mg", "atomic_number": 12},
    "Aluminum": {"symbol": "Al", "atomic_number": 13},
    "Silicon": {"symbol": "Si", "atomic_number": 14},
    "Phosphorus": {"symbol": "P", "atomic_number": 15},
    "Sulfur": {"symbol": "S", "atomic_number": 16},
    "Chlorine": {"symbol": "Cl", "atomic_number": 17},
    "Argon": {"symbol": "Ar", "atomic_number": 18},
    "Potassium": {"symbol": "K", "atomic_number": 19},
    "Calcium": {"symbol": "Ca", "atomic_number": 20},
    "Scandium": {"symbol": "Sc", "atomic_number": 21},
    "Titanium": {"symbol": "Ti", "atomic_number": 22},
    "Vanadium": {"symbol": "V", "atomic_number": 23},
    "Chromium": {"symbol": "Cr", "atomic_number": 24},
    "Manganese": {"symbol": "Mn", "atomic_number": 25},
    "Iron": {"symbol": "Fe", "atomic_number": 26},
    "Cobalt": {"symbol": "Co", "atomic_number": 27},
    "Nickel": {"symbol": "Ni", "atomic_number": 28},
    "Copper": {"symbol": "Cu", "atomic_number": 29},
    "Zinc": {"symbol": "Zn", "atomic_number": 30},
    "Gallium": {"symbol": "Ga", "atomic_number": 31},
    "Germanium": {"symbol": "Ge", "atomic_number": 32},
    "Arsenic": {"symbol": "As", "atomic_number": 33},
    "Selenium": {"symbol": "Se", "atomic_number": 34},
    "Bromine": {"symbol": "Br", "atomic_number": 35},
    "Krypton": {"symbol": "Kr", "atomic_number": 36},
    "Rubidium": {"symbol": "Rb", "atomic_number": 37},
    "Strontium": {"symbol": "Sr", "atomic_number": 38},
    "Yttrium": {"symbol": "Y", "atomic_number": 39},
    "Zirconium": {"symbol": "Zr", "atomic_number": 40},
    "Niobium": {"symbol": "Nb", "atomic_number": 41},
    "Molybdenum": {"symbol": "Mo", "atomic_number": 42},
    "Technetium": {"symbol": "Tc", "atomic_number": 43},
    "Ruthenium": {"symbol": "Ru", "atomic_number": 44},
    "Rhodium": {"symbol": "Rh", "atomic_number": 45},
    "Palladium": {"symbol": "Pd", "atomic_number": 46},
    "Silver": {"symbol": "Ag", "atomic_number": 47},
    "Cadmium": {"symbol": "Cd", "atomic_number": 48},
    "Indium": {"symbol": "In", "atomic_number": 49},
    "Tin": {"symbol": "Sn", "atomic_number": 50},
    "Antimony": {"symbol": "Sb", "atomic_number": 51},
    "Tellurium": {"symbol": "Te", "atomic_number": 52},
    "Iodine": {"symbol": "I", "atomic_number": 53},
    "Xenon": {"symbol": "Xe", "atomic_number": 54},
    "Cesium": {"symbol": "Cs", "atomic_number": 55},
    "Barium": {"symbol": "Ba", "atomic_number": 56},
    "Lanthanum": {"symbol": "La", "atomic_number": 57},
    "Cerium": {"symbol": "Ce", "atomic_number": 58},
    "Praseodymium": {"symbol": "Pr", "atomic_number": 59},
    "Neodymium": {"symbol": "Nd", "atomic_number": 60},
    "Promethium": {"symbol": "Pm", "atomic_number": 61},
    "Samarium": {"symbol": "Sm", "atomic_number": 62},
    "Europium": {"symbol": "Eu", "atomic_number": 63},
    "Gadolinium": {"symbol": "Gd", "atomic_number": 64},
    "Terbium": {"symbol": "Tb", "atomic_number": 65},
    "Dysprosium": {"symbol": "Dy", "atomic_number": 66},
    "Holmium": {"symbol": "Ho", "atomic_number": 67},
    "Erbium": {"symbol": "Er", "atomic_number": 68},
    "Thulium": {"symbol": "Tm", "atomic_number": 69},
    "Ytterbium": {"symbol": "Yb", "atomic_number": 70},
    "Lutetium": {"symbol": "Lu", "atomic_number": 71},
    "Hafnium": {"symbol": "Hf", "atomic_number": 72},
    "Tantalum": {"symbol": "Ta", "atomic_number": 73},
    "Tungsten": {"symbol": "W", "atomic_number": 74},
    "Rhenium": {"symbol": "Re", "atomic_number": 75},
    "Osmium": {"symbol": "Os", "atomic_number": 76},
    "Iridium": {"symbol": "Ir", "atomic_number": 77},
    "Platinum": {"symbol": "Pt", "atomic_number": 78},
    "Gold": {"symbol": "Au", "atomic_number": 79},
    "Mercury": {"symbol": "Hg", "atomic_number": 80},
    "Thallium": {"symbol": "Tl", "atomic_number": 81},
    "Lead": {"symbol": "Pb", "atomic_number": 82},
    "Bismuth": {"symbol": "Bi", "atomic_number": 83},
    "Polonium": {"symbol": "Po", "atomic_number": 84},
    "Astatine": {"symbol": "At", "atomic_number": 85},
    "Radon": {"symbol": "Rn", "atomic_number": 86},
    "Francium": {"symbol": "Fr", "atomic_number": 87},
    "Radium": {"symbol": "Ra", "atomic_number": 88},
    "Actinium": {"symbol": "Ac", "atomic_number": 89},
    "Thorium": {"symbol": "Th", "atomic_number": 90},
    "Protactinium": {"symbol": "Pa", "atomic_number": 91},
    "Uranium": {"symbol": "U", "atomic_number": 92},
    "Neptunium": {"symbol": "Np", "atomic_number": 93},
    "Plutonium": {"symbol": "Pu", "atomic_number": 94},
    "Americium": {"symbol": "Am", "atomic_number": 95},
    "Curium": {"symbol": "Cm", "atomic_number": 96},
    "Berkelium": {"symbol": "Bk", "atomic_number": 97},
    "Californium": {"symbol": "Cf", "atomic_number": 98},
    "Einsteinium": {"symbol": "Es", "atomic_number": 99},
    "Fermium": {"symbol": "Fm", "atomic_number": 100},
    "Mendelevium": {"symbol": "Md", "atomic_number": 101},
    "Nobelium": {"symbol": "No", "atomic_number": 102},
    "Lawrencium": {"symbol": "Lr", "atomic_number": 103},
    "Rutherfordium": {"symbol": "Rf", "atomic_number": 104},
    "Dubnium": {"symbol": "Db", "atomic_number": 105},
    "Seaborgium": {"symbol": "Sg", "atomic_number": 106},
    "Bohrium": {"symbol": "Bh", "atomic_number": 107},
    "Hassium": {"symbol": "Hs", "atomic_number": 108},
    "Meitnerium": {"symbol": "Mt", "atomic_number": 109},
    "Darmstadtium": {"symbol": "Ds", "atomic_number": 110},
    "Roentgenium": {"symbol": "Rg", "atomic_number": 111},
    "Copernicium": {"symbol": "Cn", "atomic_number": 112},
    "Nihonium": {"symbol": "Nh", "atomic_number": 113},
    "Flerovium": {"symbol": "Fl", "atomic_number": 114},
    "Moscovium": {"symbol": "Mc", "atomic_number": 115},
    "Livermorium": {"symbol": "Lv", "atomic_number": 116},
    "Tennessine": {"symbol": "Ts", "atomic_number": 117},
    "Oganesson": {"symbol": "Og", "atomic_number": 118}
}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Elemental Explorer")
        self.geometry("400x250")  # Main window size
        self.iconbitmap('C:/Users/ced/ACP FINAL PROJ/PeriodicTableUI/src/Icon.ico')
        self.resizable(False, False)
        self.config(bg='#0C6478')

        self.total_questions = 25  # Default to 25 questions

        # Call the method to create widgets
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Elemental Explorer", bg='#0C6478', font=("Papyrus", 20, "bold"), fg=('white'))
        self.label.pack(pady=10)

        self.label = tk.Label(self, text="Enter the number of questions (max 100):", bg='#0C6478', font=("Papyrus", 12, "bold"), fg=('white'))
        self.label.pack(pady=10)

        self.questions_entry = tk.Entry(self, font=("Papyrus", 12))
        self.questions_entry.pack(pady=10)

        # Start and Help buttons
        button_frame = tk.Frame(self, bg='#0C6478')
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text="Start Game", bg='#15919B', font=("Georgia", 10), command=self.start_game)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.help_button = tk.Button(button_frame, text="How to play?", bg='#15919B', font=("Georgia", 10), command=self.help_button)
        self.help_button.pack(side=tk.LEFT)

    def start_game(self):
        try:
            self.total_questions = int(self.questions_entry.get())
            if self.total_questions < 1 or self.total_questions > 100:
                raise ValueError
            self.questions_entry.config(state="disabled")
            self.start_button.config(state="disabled")
            self.help_button.config(state="disabled")  # Disable the help button when the game starts

            # Hide the main window before opening the game window
            self.withdraw()

            self.create_game_window()  # Create and start the game window
        except ValueError:
            self.label.config(text="Please enter a number between 1 and 100.", fg="orange")


    def create_game_window(self):
        self.game_window = GameWindow(self.total_questions)  # Create the game window with the number of questions
        self.game_window.mainloop()  # Start the game window event loop
        self.destroy()  # Close the main window when the game window opens

    def help_button(self):
        self.destroy()  
        from PeriodicTableUI.src.helpGuide import Help
        help_window = Help()  
        help_window.flash_instructions()
        help_window.mainloop()

class GameWindow(tk.Toplevel):
    def __init__(self, total_questions):
        super().__init__()
        self.title("Elemental Explorer - Game")
        self.geometry("400x550")
        self.iconbitmap('C:/Users/ced/ACP FINAL PROJ/PeriodicTableUI/src/Icon.ico')
        self.resizable(False, False)
        self.config(bg='#0C6478')

        self.total_questions = total_questions
        self.question_count = 1
        self.score = 0

        # Call the method to create widgets
        self.create_game_widgets()

    def create_game_widgets(self):
        self.label = tk.Label(self, text="Elemental Explorer", bg='#0C6478', font=("Papyrus", 20, "bold"), fg=('white'))
        self.label.pack(pady=10)

        self.label = tk.Label(self, text="Periodic Table Game", bg='#0C6478', font=("Papyrus", 15, "bold"), fg=('white'))
        self.label.pack(pady=10)

        self.item_number_label = tk.Label(self, text=f"Question: {self.question_count}", bg='#0C6478', font=("Papyrus", 15 , "bold"), fg=('white'))
        self.item_number_label.pack(pady=15)

        self.question_label = tk.Label(self, text="", bg='#0C6478', font=("Papyrus", 12, "italic", "bold"), fg=('white'))
        self.question_label.pack(pady=0)

        self.entry = tk.Entry(self, font=("Papyrus", 12))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", font=("Georgia", 10), bg='#15919B', command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.new_question_button = tk.Button(self, text="Next Question", bg='#15919B', font=("Georgia", 10), command=self.next_question)
        self.new_question_button.pack(pady=10)

        self.feedback_label = tk.Label(self, text="", bg='#0C6478', font=("Georgia", 12), fg="green")
        self.feedback_label.pack(pady=10)

        self.retake_button = tk.Button(self, text="Retry", bg='#15919B', font=("Georgia", 10), command=self.retake_exam, state=tk.DISABLED)
        self.retake_button.pack(pady=10)

        self.study_button = tk.Button(self, text="Study Area", bg='#15919B', font=("Georgia", 10), command=self.study_area, state=tk.DISABLED)
        self.study_button.pack(pady=10)

        self.ask_question()

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

    def display_final_score(self):
        self.question_label.config(text="Test Complete!")
        self.submit_button.config(state="disabled")
        self.entry.config(state="disabled")
        self.new_question_button.config(state="disabled")
        self.feedback_label.config(
            text=f"Your final score is: {self.score} / {self.total_questions}", font=("Papyrus", 15, "bold"), fg="#46BDF1"
        )
        self.retake_button.config(state="normal")
        self.study_button.config(state="normal")

    def retake_exam(self):
        self.question_count = 1
        self.score = 0
        self.submit_button.config(state="normal")
        self.entry.config(state="normal")
        self.new_question_button.config(state="normal")
        self.feedback_label.config(text="")
        self.retake_button.config(state="disabled")
        self.ask_question()
        self.destroy()  # Close the current game window
        self.quit()  # Quit the current event loop
        app = App()  # Recreate the App window
        app.mainloop()  # Start a new main loop for the App window

    def study_area(self):
        self.destroy()
        from periodicTableGUI import main
        main()

    def next_question(self):
        if self.question_count < self.total_questions:
            self.question_count += 1
            self.ask_question()
        else:
            self.display_final_score()


if __name__ == "__main__":
    app = App()
    app.mainloop()
