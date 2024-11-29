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
    "   - Click ->View Leaderboard<- to see the top 10 highest scores.\n\n"
    "6. Study Area:\n"
    "   - You can access the ->Study Area<- button for more educational content after finishing the game.\n\n"
    "7. Retake the Game:\n"
    "   - You can retry the game by clicking ->Retry<- to try for a better score.\n\n"
    "8. Help:\n"
    "   - If you need help, click the ->Help<- button on the main screen for guidance.\n\n"
    "9. Username Requirements:\n"
    "   - Your username should consist of letters and numbers only. No spaces or special characters are allowed.\n\n"
    "10. Notes:\n"
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
        """Configure the main window."""
        self.title("Elemental Explorer")
        self.geometry("1920x1080")  # Adjust window size
        self.iconbitmap('C:/Users/ced/ACP FINAL PROJ/PeriodicTableUI/src/Icon.ico')  # Replace with a valid path
        self.config(bg='#485540')
        self.resizable(False, False)

    def create_widgets(self):
        """Create and place widgets in the window."""
        # Create a frame to hold all the widgets
        self.frame = tk.Frame(self, bg='#485540', padx=100)  # Added padx=100 for space on the left
        self.frame.pack(fill="both", expand=True)

        self.create_labels()
        self.create_gif()  # Add the GIF
        self.create_back_button()

    def create_labels(self):
        """Create the labels for the title, subtitle, and instructions."""
        # Title label
        self.title_label = tk.Label(
            self.frame, text="Elemental Explorer", bg='#485540',
            font=("Papyrus", 60, "bold"), fg='white'
        )
        self.title_label.pack(pady=20)

        # Subtitle label
        self.subtitle_label = tk.Label(
            self.frame, text="Periodic Table Game", bg='#485540',
            font=("Papyrus", 45, "bold"), fg='white'
        )
        self.subtitle_label.pack(pady=10)

        # Create a canvas for scrolling
        self.canvas = tk.Canvas(self.frame, bg='#485540', highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)  # Keep the canvas filling space

        # Create a scrollbar for the canvas
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame to hold the content within the canvas
        self.scrollable_frame = tk.Frame(self.canvas, bg='#485540')

        # Add the scrollable frame to the canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Instruction label inside the scrollable frame
        self.instruction_label = tk.Label(
            self.scrollable_frame, text=INSTRUCTIONS_TEXT, bg='#485540', font=("Arial", 20, "italic", "bold"),
            fg='white', justify="left", wraplength=900  # Adjust wrap length for left alignment
        )
        self.instruction_label.pack(padx=100, pady=10)

        # Update the scrollable region after packing widgets
        self.scrollable_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def create_gif(self):
        """Create a label to display the animated GIF."""
        # Load the GIF using Pillow
        self.gif_path = "C:/Users/ced/ACP-DBMS/Program/helpbg.gif"  # Adjust the path to your GIF
        self.gif_image = Image.open(self.gif_path)

        # Create a list to store frames
        self.frames = []
        for frame in range(self.gif_image.n_frames):
            self.gif_image.seek(frame)
            frame_image = ImageTk.PhotoImage(self.gif_image.copy())
            self.frames.append(frame_image)

        # Create a label to display the GIF
        self.gif_label = tk.Label(self.frame, image=self.frames[0], bg='#485540')
        self.gif_label.place(relx=0.90, rely=0.50, anchor="e")

        # Start the animation
        self.animate_gif(0)

    def animate_gif(self, current_frame):
        """Animate the GIF by updating the image every 100ms."""
        self.gif_label.config(image=self.frames[current_frame])
        next_frame = (current_frame + 1) % len(self.frames)  # Loop back to the first frame
        self.after(100, self.animate_gif, next_frame)  # Schedule the next frame update

    def create_back_button(self):
        """Create the back button at the bottom of the window."""
        self.back = tk.Button(
            self, text="Back to Game", bg='#485540', fg='white', font=("Georgia", 20),
            command=self.back_to_game
        )
        self.back.pack(side="bottom", pady=50)

    def flash_instructions(self):
        """Display the instructions in the instruction_label."""
        self.instruction_label.config(text=INSTRUCTIONS_TEXT)

    def clear_instructions(self):
        """Clear the instructions from the instruction_label."""
        self.instruction_label.config(text="")

    def back_to_game(self):
        """Handle the back button functionality."""
        self.destroy()
        from main import App
        App()


# Run the Tkinter window
if __name__ == "__main__":
    app = Help()
    app.mainloop()