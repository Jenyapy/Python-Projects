import tkinter as tk
from random import randint
from PIL import Image, ImageTk
import time

# Create the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Creating a list of play options
t = ["Rock", "Paper", "Scissors"]


# Function to show "thinking" animation
def show_thinking_animation():
    for _ in range(3):
        result_label.config(text="Thinking...", font=("Helvetica", 16, "italic"), fg="#007BFF")
        root.update()
        time.sleep(0.5)
        result_label.config(text="", font=("Helvetica", 16, "italic"), fg="#007BFF")
        root.update()
        time.sleep(0.5)


# Function to determine the winner
def determine_winner(player_choice):
    show_thinking_animation()

    computer_choice = t[randint(0, 2)]
    result = ""
    if player_choice == computer_choice:
        result = "Tie!"
    elif player_choice == "Rock":
        if computer_choice == "Paper":
            result = f"You lose! {computer_choice} covers {player_choice}"
        else:
            result = f"You win! {player_choice} smashes {computer_choice}"
    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            result = f"You lose! {computer_choice} cuts {player_choice}"
        else:
            result = f"You win! {player_choice} covers {computer_choice}"
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            result = f"You lose! {computer_choice} smashes {player_choice}"
        else:
            result = f"You win! {player_choice} cuts {computer_choice}"
    else:
        result = "That's not a valid play. Check your spelling!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}", font=("Helvetica", 14, "bold"),
                        fg="#28a745")


# Load images
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((80, 80)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((80, 80)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((80, 80)))

# Creating GUI components
instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 16, "bold"),
                             bg="#f0f0f0")
instruction_label.pack(pady=20)

# Creating buttons with images for each choice
rock_button = tk.Button(root, image=rock_img, command=lambda: determine_winner("Rock"), bd=0, bg="#f0f0f0")
rock_button.pack(side=tk.LEFT, padx=20)

paper_button = tk.Button(root, image=paper_img, command=lambda: determine_winner("Paper"), bd=0, bg="#f0f0f0")
paper_button.pack(side=tk.LEFT, padx=20)

scissors_button = tk.Button(root, image=scissors_img, command=lambda: determine_winner("Scissors"), bd=0, bg="#f0f0f0")
scissors_button.pack(side=tk.LEFT, padx=20)

# Creating a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0")
result_label.pack(pady=20)

# Running the main event loop
root.mainloop()
