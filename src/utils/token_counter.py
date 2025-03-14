import tiktoken
import os

class TokenCounter:
    """Class to handle token counting logic for LLMs."""

    @staticmethod
    def get_available_models():
        """Return a list of available encoding models."""
        return ["cl100k_base", "p50k_base", "r50k_base", "p50k_edit", "gpt2"]

    @staticmethod
    def count_tokens(text: str, encoding_name: str) -> dict:
        """Counts tokens, characters, words, and lines."""
        try:
            encoding = tiktoken.get_encoding(encoding_name)
        except KeyError:
            raise ValueError(f"Invalid encoding name: {encoding_name}")

        if not text.strip():
            return {
                "tokens": 0,
                "characters": 0,
                "words": 0,
                "lines": 0
            }

        tokens = encoding.encode(text)
        return {
            "tokens": len(tokens),
            "characters": len(text),
            "words": len(text.split()),
            "lines": text.count('\n') + 1
        }

    @staticmethod
    def read_text_file(file_path: str) -> str:
        """Reads and returns the content of a text file."""
        if not os.path.exists(file_path):
            raise IOError(f"File not found: {file_path}")
        if not file_path.lower().endswith(".txt"):
            raise IOError(f"Not a text file: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            raise IOError(f"Error reading file: {e}")

    def get_tokens(self, text: str, encoding_name: str = "cl100k_base") -> list:
        """Encodes the text and returns the list of integer token IDs."""
        try:
            encoding = tiktoken.get_encoding(encoding_name)
            return encoding.encode(text)
        except KeyError:
            raise ValueError(f"Invalid encoding name: {encoding_name}")
        except Exception as e:
            print(f"Error in get_tokens: {e}")
            return []


    def decode_token(self, token_id: int, encoding_name: str = "cl100k_base") -> str:
        """Decodes a single token ID, handling potential errors robustly."""
        try:
            encoding = tiktoken.get_encoding(encoding_name)
            # Get the raw bytes for the token
            token_bytes = encoding.decode_single_token_bytes(token_id)

            # Decode with 'utf-8', replacing errors
            decoded_string = token_bytes.decode('utf-8', errors='replace')

            # Replace whitespace and control characters with visible representations
            decoded_string = decoded_string.replace('\n', '↵\n')  # Newline
            decoded_string = decoded_string.replace('\t', '→\t')  # Tab
            decoded_string = decoded_string.replace(' ', '·')    # Space

            return decoded_string

        except KeyError:
            raise ValueError(f"Invalid encoding name: {encoding_name}")
        except Exception as e:
            print(f"Error in decode_token: {e}")
            return f"[Error decoding token: {token_id}]" # Return placeholder
        
    