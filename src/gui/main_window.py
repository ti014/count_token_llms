# src/gui/main_window.py
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from gui.input_frame import InputFrame
from gui.results_frame import ResultsFrame
from gui.token_visualization_frame import TokenVisualizationFrame
from logic.token_counter_logic import AppController

class MainWindow(ThemedTk):
    def __init__(self):
        super().__init__(theme="arc")
        self.title("LLM Token Counter")
        self.geometry("850x650")
        self.minsize(850, 400)  # Reduced min height

        self.controller = AppController()

        self.input_frame = InputFrame(self,
                                      on_count_tokens=self.controller.count_tokens,
                                      on_import=self.controller.import_text,
                                      on_clear=self.controller.clear_input)
        self.results_frame = ResultsFrame(self)
        self.token_viz_frame = TokenVisualizationFrame(self)

        self.input_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))
        self.results_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        self.token_viz_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=(5, 10))

        self.rowconfigure(0, weight=0)  # Input frame *doesn't* expand vertically
        self.rowconfigure(1, weight=0)  # Result frame *doesn't* expand
        self.rowconfigure(2, weight=1)  # Visualization frame *does* expand vertically
        self.columnconfigure(0, weight=1)

        self.controller.set_ui_update_callback(self.update_ui)


    def update_ui(self, counts, tokens, encoding_name):
        self.results_frame.update_results(counts['tokens'], counts['characters'], counts['words'], counts['lines'])
        self.token_viz_frame.set_tokens(tokens, encoding_name, self.controller.token_counter)