# src/gui/results_frame.py

import tkinter as tk
from tkinter import ttk

class ResultsFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.token_var = tk.StringVar(value="Tokens: 0")
        self.char_var = tk.StringVar(value="Characters: 0")
        self.word_var = tk.StringVar(value="Words: 0")
        self.line_var = tk.StringVar(value="Lines: 0")
        self.create_widgets()

    def create_widgets(self):
        # Use grid layout within the frame
        token_label = ttk.Label(self, textvariable=self.token_var, font=("Arial", 18, "bold"), foreground="#007bff")  # Larger, bolder, blue
        token_label.grid(row=0, column=0, padx=(10, 20), pady=5, sticky="w") # More horizontal space

        char_label = ttk.Label(self, textvariable=self.char_var, font=("Arial", 14), foreground="#28a745")  # Larger, green
        char_label.grid(row=0, column=1, padx=20, pady=5, sticky="w") # More space

        word_label = ttk.Label(self, textvariable=self.word_var, font=("Arial", 14), foreground="#dc3545")  # Larger, red
        word_label.grid(row=0, column=2, padx=20, pady=5, sticky="w")# More space

        line_label = ttk.Label(self, textvariable=self.line_var, font=("Arial", 14), foreground="#17a2b8")  # Larger, teal
        line_label.grid(row=0, column=3, padx=(20, 10), pady=5, sticky="w")# More space


    def update_results(self, tokens, characters, words, lines):
        self.token_var.set(f"Tokens: {tokens}")
        self.char_var.set(f"Characters: {characters}")
        self.word_var.set(f"Words: {words}")
        self.line_var.set(f"Lines: {lines}")