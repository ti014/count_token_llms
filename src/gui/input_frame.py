# src/gui/input_frame.py
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog

class InputFrame(ttk.Frame):
    def __init__(self, master, on_count_tokens, on_import, on_clear):
        super().__init__(master)
        self.on_count_tokens = on_count_tokens
        self.on_import = on_import
        self.on_clear = on_clear
        # Use a descriptive name as the default, and store the mapping
        self.encoding_var = tk.StringVar(value="cl100k_base (GPT-3.5, GPT-4)")
        self.debounce_timer = None

        # --- ENCODING MAPPING ---
        self.encoding_map = {
            "cl100k_base (GPT-3.5, GPT-4)": "cl100k_base",
            "p50k_base (GPT-3, Davinci)": "p50k_base",
            "r50k_base (GPT-2, Ada)": "r50k_base",
             "p50k_edit": "p50k_edit",
             "gpt2": "gpt2"
        }
        self.create_widgets()

    def create_widgets(self):
        # --- Encoding Selection ---
        encoding_frame = ttk.LabelFrame(self, text="Encoding Model")
        encoding_frame.pack(fill="x", padx=10, pady=5)

        self.encoding_dropdown = ttk.Combobox(
            encoding_frame,
            textvariable=self.encoding_var,
            values=list(self.encoding_map.keys()),  # Use descriptive names
            state="readonly",
            font=("Arial", 11)
        )
        self.encoding_dropdown.pack(fill="x", padx=5, pady=(5, 10))

        # --- Text Input ---
        input_frame = ttk.LabelFrame(self, text="Input Text")
        input_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.text_input = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, font=("Arial", 11), height=10)
        self.text_input.pack(fill="both", expand=True, padx=5, pady=5)
        self.text_input.bind("<KeyRelease>", self.on_text_change)
        self.text_input.bind("<BackSpace>", self.on_text_change)
        self.text_input.bind("<Delete>", self.on_text_change)
        self.text_input.bind("<Control-x>", self.on_text_change)
        self.text_input.bind("<Control-v>", self.on_text_change)
        self.text_input.bind("<Control-a>", self.on_text_change)

        # --- Buttons ---
        buttons_frame = ttk.Frame(self)
        buttons_frame.pack(fill="x", padx=10, pady=(5, 10))

        self.count_button = ttk.Button(buttons_frame, text="Count Tokens", command=self._on_count_clicked, style="Accent.TButton")
        self.count_button.grid(row=0, column=0, padx=5)

        self.import_button = ttk.Button(buttons_frame, text="Import Text File", command=self._on_import_clicked)
        self.import_button.grid(row=0, column=1, padx=5)

        self.clear_button = ttk.Button(buttons_frame, text="Clear", command=self._on_clear_clicked)
        self.clear_button.grid(row=0, column=2, padx=5)

    def on_text_change(self, event=None):
        if self.debounce_timer:
            self.after_cancel(self.debounce_timer)
        self.debounce_timer = self.after(10, self._on_count_clicked)

    def _on_count_clicked(self):
        text = self.get_text()
        encoding = self.get_encoding()  # Get the *short* encoding name
        if text and self.on_count_tokens:
            self.on_count_tokens(text, encoding)

    def _on_import_clicked(self):
        file_path = filedialog.askopenfilename(
            title="Select a text file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path and self.on_import:
            self.on_import(file_path)

    def _on_clear_clicked(self):
        if self.on_clear:
            self.clear_text()
            self.on_clear()

    def get_encoding(self):
        """Returns the *short* encoding name (for tiktoken)."""
        selected_display_name = self.encoding_var.get()
        return self.encoding_map.get(selected_display_name, "cl100k_base") # Default, and handle errors

    def get_text(self):
        return self.text_input.get("1.0", tk.END).strip()

    def set_text(self, text):
        self.text_input.delete("1.0", tk.END)
        self.text_input.insert("1.0", text)

    def clear_text(self):
        self.text_input.delete("1.0", tk.END)