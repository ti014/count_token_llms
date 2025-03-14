# src/main.py (CORRECTED)
import tkinter as tk
from gui.main_window import MainWindow

def main():
    # root = tk.Tk()  <-- NO LONGER NEEDED
    app = MainWindow()  # Create the MainWindow instance directly (no arguments)
    app.mainloop()  # Call mainloop on the MainWindow instance

if __name__ == "__main__":
    main()