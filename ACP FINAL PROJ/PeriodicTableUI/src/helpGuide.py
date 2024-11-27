import tkinter as tk

class Help(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Elemental Explorer")
        self.geometry("500x660")  # Adjust window size
        self.iconbitmap('C:/Users/ced/ACP FINAL PROJ/PeriodicTableUI/src/Icon.ico')  # Replace with a valid path
        self.config(bg='#0C6478')
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Create a frame to hold all the widgets (without scrolling)
        self.frame = tk.Frame(self, bg='#0C6478')
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_labels()

        # Add the back button after the frame is created, using pack(side="bottom")
        self.back = tk.Button(self, text="Back to Game", bg='#15919B', font=("Georgia", 10), command=self.back_to_game)
        self.back.pack(side="bottom", padx=10, pady=10)

    def create_labels(self):
        # Title label
        self.label = tk.Label(self.frame, text="Elemental Explorer", bg='#0C6478', font=("Papyrus", 20, "bold"), fg='white')
        self.label.pack(pady=(10, 10))  # Adjust padding between title and next label

        # Subtitle label
        self.label = tk.Label(self.frame, text="Periodic Table Game", bg='#0C6478', font=("Papyrus", 12, "bold"), fg='white')
        self.label.pack(pady=(0, 10))  # Adjust padding

        # Instruction label for instructions
        self.instruction_label = tk.Label(self.frame, text="", bg='#0C6478', font=("Arial", 10, "italic", "bold"), fg='white', justify="left", wraplength=460, anchor="nw")
        self.instruction_label.pack(fill="both", expand=True, padx=0, pady=10)  # Allow it to expand and fill

    def flash_instructions(self):
        instructions_text = (
            "Instructions for Playing 'Elemental Explorer' Game\n\n"
            "1. Objective:\n"
            "   Test your knowledge of the Periodic Table by answering questions about element symbols or atomic numbers.\n"
            "2. Game Flow:\n"
            "   - Upon starting the game, you’ll see a prompt to enter the number of questions you’d like to answer.\n"
            "      - Enter a number between 1 and 100, and click ->Start Game<- to begin.\n"
            "   - You will be asked to identify either the symbol or atomic number of elements.\n"
            "   - Notice:\n"
            "     - Always type something as an answer! Leaving the answer blank will be treated as wrong and scored as zero.\n"
            "     - Double-check your answers before clicking ->Submit<-.\n"
            "   - After submitting your answer, click ->Next Question<- to proceed.\n"
            "3. Final Score:\n"
            "   - After all questions are completed, your final score will be displayed.\n"
            "4. Help:\n"
            "   - Click the ->Help<- button if you need guidance on how the game works.\n"
            "5. Periodic Table:\n"
            "   - You can view the Periodic Table by clicking the ->Study Area<- button, which is only available after completing the game.\n"
            "6. Retake the Exam:\n"
            "   - You can retake the game by clicking ->Retry<- button."
        )
        
        # Display the instructions in the instruction_label
        self.instruction_label.config(text=instructions_text, fg='white')

    def clear_instructions(self):
        # Clear the instructions after 5 seconds
        self.instruction_label.config(text="")

    def back_to_game(self):
        self.destroy()
        from gameGUI import App
        App()


# Run the Tkinter window
if __name__ == "__main__":
    app = Help()  # Create an instance of the Help class
    app.flash_instructions()  # Show instructions when the app starts
    app.mainloop()  # Run the Tkinter event loop to display the window


