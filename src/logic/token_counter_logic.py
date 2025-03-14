# src/logic/token_counter_logic.py
# Changes needed

import tkinter as tk
from tkinter import messagebox
from utils.token_counter import TokenCounter
import threading


class AppController:
    def __init__(self):
        self.token_counter = TokenCounter()
        self.ui_update_callback = None

    def set_ui_update_callback(self, callback):
        self.ui_update_callback = callback

    def _count_tokens_thread(self, text, encoding_name):
        """Counts tokens in a separate thread."""
        try:
            counts = self.token_counter.count_tokens(text, encoding_name)
            tokens = self.token_counter.get_tokens(text, encoding_name)
            if self.ui_update_callback:
                self.ui_update_callback(counts, tokens, encoding_name)
        except ValueError as e:
            if self.ui_update_callback:
              self.ui_update_callback({"tokens": 0, "characters": 0, "words": 0, "lines": 0}, [], "")
            messagebox.showerror("Error", str(e))


    def count_tokens(self, text, encoding_name):
        """Starts a new thread to count tokens."""
        thread = threading.Thread(target=self._count_tokens_thread, args=(text, encoding_name))
        thread.start()

    def import_text(self, file_path):
        """Imports text from a file (runs in the main thread)."""
        try:
            content = self.token_counter.read_text_file(file_path)
            if self.ui_update_callback:
                self.ui_update_callback({"tokens": 0, "characters": 0, "words": 0, "lines": 0}, [], "")
                self.count_tokens(content, "cl100k_base") # Auto count

        except IOError as e:
            messagebox.showerror("Error", str(e))
    def clear_input(self):
        if self.ui_update_callback:
            self.ui_update_callback({"tokens": 0, "characters": 0, "words": 0, "lines": 0}, [], "")