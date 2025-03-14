# src/gui/token_visualization_frame.py
import tkinter as tk
from tkinter import ttk, scrolledtext

class TokenVisualizationFrame(ttk.Frame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.token_colors = [
            "#87CEEB", "#90EE90", "#FFB6C1", "#FFD700", "#C0C0C0",
            "#E6E6FA", "#F0F8FF", "#FAEBD7", "#F5FFFA", "#FFF0F5"
        ]
        self.create_widgets()


    def create_widgets(self):
        self.token_viz_text = scrolledtext.ScrolledText(
            self,
            wrap=tk.WORD,
            height=20,
            font=("Arial", 12),
            state=tk.DISABLED,
            bg="#f0f0f0"
        )
        self.token_viz_text.pack(fill="both", expand=True, padx=5, pady=5)

    def set_tokens(self, tokens, encoding_name, token_counter):
        """Visualize tokens with different colors."""
        self.token_viz_text.config(state=tk.NORMAL)
        self.token_viz_text.delete("1.0", tk.END)

        #Remove old tags
        for tag in self.token_viz_text.tag_names():
            self.token_viz_text.tag_delete(tag)

        self.token_viz_text.insert(tk.END, "Tokens (highlighted):\n\n", "header")
        self.token_viz_text.tag_configure("header", font=("Arial", 14, "bold"))

        used_colors = {}
        for i, token_id in enumerate(tokens):
            # Use the improved decode_token method
            token_text = token_counter.decode_token(token_id, encoding_name)

            if token_id in used_colors:
                color_index = used_colors[token_id]
            else:
                color_index = i % len(self.token_colors)
                used_colors[token_id] = color_index

            tag_name = f"token_{i}"
            self.token_viz_text.tag_configure(
                tag_name,
                background=self.token_colors[color_index],
                borderwidth=1,
                relief="solid",
                font=("Arial", 12),
                spacing1=2,
                spacing3=2,
            )

            self.token_viz_text.insert(tk.END, token_text, tag_name)
            if i < len(tokens) - 1:
                self.token_viz_text.insert(tk.END, " ")

        self.token_viz_text.see("1.0")
        self.token_viz_text.config(state=tk.DISABLED)

    def clear(self):
        self.token_viz_text.config(state=tk.NORMAL)
        self.token_viz_text.delete("1.0", tk.END)
        self.token_viz_text.config(state=tk.DISABLED)