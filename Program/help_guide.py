import tkinter as tk
from PIL import Image, ImageTk

# Instruction text moved to a constant for clarity
INSTRUCTIONS_TEXT = (
    "Instructions for Playing 'Elemental Explorer' Game\n\n"
    "1. Objective:\n"
    "   Test your knowledge of the Periodic Table by answering questions about element symbols or atomic numbers.\n\n"
    "2. Game Flow:\n"
    "   - Upon starting the game, you’ll see a prompt to enter your username.\n"
    "     - Type an alphanumeric username (no spaces or special characters) and click ->Start Game<- to begin.\n"
    "   - You will be asked to identify either the symbol or atomic number of elements.\n"
    "   - After answering a question, click ->Next Question<- to proceed.\n\n"
    "3. Answering Questions:\n"
    "   - If you answer correctly, you’ll receive positive feedback, and your score will increase.\n"
    "   - If the answer is wrong, the correct answer will be shown.\n\n"
    "4. Final Score:\n"
    "   - After all 50 questions are completed, your final score will be displayed.\n"
    "   - The score will be recorded in the leaderboard if it is your highest score.\n\n"
    "5. Leaderboard:\n"
    "   - Click ->View Leaderboard<- to see the top 10 highest scores.\n"
    "   - Leaderboards can be reset depends on the user.\n"
    "6. Study Area:\n"
    "   - You can access the ->Study Area<- button for more educational content after finishing the game.\n\n"
    "7. Retake the Game:\n"
    "   - You can retry the game by clicking ->Retry<- to try for a better score.\n\n"
    "8. Help:\n"
    "   - If you need help, click the ->Help<- button on the main screen for guidance.\n\n"
    "9. Notes:\n"
    "   - Always type something as an answer! Leaving the answer blank will be scored as zero.\n"
    "   - Double-check your answers before submitting.\n\n"
    "You can give feedback and view other players' feedback about the\t\tgame. This will help the game grow!"
)

class Help(tk.Tk):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.create_widgets()
        self.flash_instructions()

    def setup_window(self):
        self.title("Elemental Explorer")
        self.geometry("1920x1080")
        self.iconbitmap('C:/Users/ced/Elemental Explorer/Program/images/Icon.ico') 
        self.config(bg='#485540')

    def create_widgets(self):
        self.frame = tk.Frame(self, bg='#485540', padx=100) 
        self.frame.pack(fill="both", expand=True)

        self.create_labels()
        self.create_gif()
        self.create_back_button()

    def create_labels(self):
        self.title_label = tk.Label(
            self.frame, text="Elemental Explorer", bg='#485540',
            font=("Papyrus", 60, "bold"), fg='white'
        )
        self.title_label.pack(pady=20)

        self.subtitle_label = tk.Label(
            self.frame, text="Periodic Table Game", bg='#485540',
            font=("Papyrus", 45, "bold"), fg='white'
        )
        self.subtitle_label.pack(pady=10)

        self.canvas = tk.Canvas(self.frame, bg='#485540', highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True) 

        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = tk.Frame(self.canvas, bg='#485540')

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.instruction_label = tk.Label(
            self.scrollable_frame, text=INSTRUCTIONS_TEXT, bg='#485540', font=("Arial", 18, "italic", "bold"),
            fg='white', justify="left", wraplength=900  # Adjust wrap length for left alignment
        )
        self.instruction_label.pack(padx=50, pady=10)

        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def create_gif(self):
        self.gif_path = "C:/Users/ced/Elemental Explorer/Program/images/helpbg.gif"
        self.gif_image = Image.open(self.gif_path)

        self.frames = []
        for frame in range(self.gif_image.n_frames):
            self.gif_image.seek(frame)
            frame_image = ImageTk.PhotoImage(self.gif_image.convert("RGBA"))
            self.frames.append(frame_image)
            
        self.gif_label = tk.Label(self.frame, image=self.frames[0], bg='#485540')
        self.gif_label.place(relx=0.85, rely=0.65, anchor="e")
        self.animate_gif(0)


    def animate_gif(self, current_frame):
        self.gif_label.config(image=self.frames[current_frame])
        next_frame = (current_frame + 1) % len(self.frames) 
        self.after(110, self.animate_gif, next_frame) 

    def create_back_button(self):
        self.back = tk.Button(
            self, text="Back to Game", bg='#485540', fg='white', font=("Georgia", 20),
            command=self.back_to_game
        )
        self.back.pack(side="bottom", pady=50)

    def flash_instructions(self):
        self.instruction_label.config(text=INSTRUCTIONS_TEXT)

    def clear_instructions(self):
        self.instruction_label.config(text="")

    def back_to_game(self):

        self.destroy()
        from classes import App
        App()

if __name__ == "__main__":
    app = Help()
    app.mainloop()