import tkinter as tk
from tkinter import messagebox

# Function to obtain all ultras
def get_all_ultras():
    # Assuming there's a global game object with a method to get ultras
    if hasattr(game, 'obtain_ultra') and callable(game.obtain_ultra):
        ultras = ['ultra1', 'ultra2', 'ultra3']  # List all ultras here
        for ultra in ultras:
            game.obtain_ultra(ultra)
        messagebox.showinfo("Success", "All ultras have been obtained!")
    else:
        print("Game object or obtain_ultra method not found.")

# Adding a button to the game interface for obtaining all ultras
def add_button():
    btn = tk.Button(root, text="Get All Ultras", command=get_all_ultras)
    btn.place(x=root.winfo_width() - 100, y=10)

# Wait for the game to load
def on_window_load():
    add_button()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Game Window")
    root.geometry("800x600")

    # Simulating a game object
    class Game:
        def obtain_ultra(self, ultra):
            print(f"Obtained {ultra}")

    game = Game()

    root.after(100, on_window_load)  # Wait for window to load
    root.mainloop()


