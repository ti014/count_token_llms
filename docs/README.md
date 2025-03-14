
# LLM Token Counter

This project provides a simple yet powerful graphical user interface (GUI) for counting and visualizing tokens in text using various encoding models from the `tiktoken` library. It's designed to help you understand how different Large Language Models (LLMs) process text at the token level.

![Token Counter GUI](/src/resources/images/1.jpg)


## Features

*   **Multiple Encoding Models:** Supports several `tiktoken` encodings, including:
    *   `cl100k_base` (used by GPT-3.5 and GPT-4)
    *   `p50k_base` (used by GPT-3)
    *   `r50k_base` (used by GPT-2)
    *   `p50k_edit`
    *   `gpt2`
*   **Token Counting:** Accurately counts the number of tokens in a given text string or text file, according to the selected encoding.
*   **Detailed Statistics:** Displays the number of characters, words, and lines in the input text.
*   **Token Visualization:**  Visually highlights the individual tokens in a separate text area, using different colors for each token.  This helps you see *exactly* how the text is being broken down.
*   **Unicode Support:** Robustly handles Unicode text (including Vietnamese and other languages with multi-byte characters).  Uses the `errors='replace'` decoding strategy and visual representations for whitespace/control characters to prevent errors and improve clarity.
*   **File Import:** Allows you to import text directly from `.txt` files.
*   **Debouncing:**  Implements debouncing on text input to prevent excessive updates and maintain responsiveness, even with large texts.
*   **Threading:** Uses a separate thread for token counting to keep the GUI responsive, even during long tokenization operations.
*   **Error Handling:**  Gracefully handles invalid encoding names and file I/O errors, displaying informative error messages.
* **User-friendly encoding selection:** Show the name of encoding, the name of model that related to them.


## Understanding Tokenization and Encodings

*   **Tokenization:** Tokenization is the process of breaking down text into smaller units (tokens) that an LLM can understand.  It's *not* simply splitting on spaces.  Tokenizers use sophisticated algorithms like Byte Pair Encoding (BPE).
*   **Encodings:** Different LLMs use different "encodings," which define the vocabulary of tokens and how text is converted to and from those tokens.
*   **`tiktoken`:**  This project uses the `tiktoken` library, which provides access to the encodings used by several OpenAI models.
*   **Vocabulary Differences:** The key difference between the encodings is their vocabulary.  `cl100k_base` has a large, diverse vocabulary and was trained on a massive dataset, making it better at handling a wide range of languages (including Vietnamese).  The other encodings have smaller vocabularies and may break down non-English words into smaller, less intuitive subword units (or even individual bytes).
*   **Unicode and Byte-Level Processing:** `tiktoken` works at the byte level.  This is why you might see partial characters or replacement characters () in the visualization, especially with encodings other than `cl100k_base` and with non-English text.  The code includes robust error handling to ensure that these situations are handled gracefully and don't cause crashes.

## Project Structure

```
count_token_llms/
├── src/
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── input_frame.py        # Input text area, encoding selection, buttons
│   │   ├── main_window.py       # Main application window
│   │   ├── results_frame.py      # Displays token, character, word, and line counts
│   │   └── token_visualization_frame.py  # Displays the highlighted tokenized text
│   ├── logic/
│   │   ├── __init__.py
│   │   └── token_counter_logic.py  # Handles communication between GUI and token counting
│   └── utils/
│       ├── __init__.py
│       └── token_counter.py     # Core token counting logic using tiktoken
├── main.py          # File run  
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```
## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request.
## License
This project is licensed under the MIT License - see the LICENSE file for details. (You should add a LICENSE file to your repository.)

