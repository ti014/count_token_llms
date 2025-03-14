# Usage

1.  **Run the application:**

    ```bash
    python ./src/main.py
    ```

2.  **GUI Interface:**

    *   **Encoding Model:** Select the desired encoding model from the dropdown menu.  The menu provides descriptive names (e.g., "cl100k_base (GPT-3.5, GPT-4)") to help you choose.
    *   **Input Text:** Enter the text you want to analyze in the "Input Text" area.  You can type directly, paste text, or import from a `.txt` file.
    *   **Import Text File:** Click this button to load text from a `.txt` file.
    *   **Count Tokens:** Click this button to perform the tokenization and update the results.  (Note: Token counting also happens automatically with a short delay after you stop typing, thanks to debouncing.)
    *   **Clear:** Click this button to clear the input text and results.
    *   **Results:** The "Tokens", "Characters", "Words", and "Lines" counts will be displayed.
    *   **Tokens (highlighted):** The tokenized text will be shown in the visualization area, with each token highlighted in a different color. Spaces, newlines, and tabs are represented by visible characters (`·`, `↵`, `→`). Any undecodable byte sequences are shown with the Unicode replacement character ().
