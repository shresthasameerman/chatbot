# Modern Chat Assistant

## Overview

The Modern Chat Assistant is a graphical user interface (GUI) chatbot application built using Python's Tkinter library. It allows users to interact with a virtual assistant that can respond to various queries, including greetings, feelings, and information about facilities.

## Features

- **User -Friendly Interface**: A modern and clean design with rounded frames and entry fields.
- **Dynamic Responses**: The chatbot can respond to greetings, inquiries about feelings, and specific questions about facilities.
- **Scrolling Chat Log**: Users can scroll through the chat history.
- **Customizable Assistant Name**: Users can provide a name for the assistant or let the system choose a random name.
- **Exit Commands**: The chatbot recognizes exit phrases to gracefully close the application.

## Installation

To run the chatbot, ensure you have Python installed on your machine. You will also need the Tkinter library, which is included with most Python installations.

1. Clone the repository or download the code files.
2. Run the `chatbot.py` file.

## Code Structure

### Main Application (`chatbot.py`)

The main application is structured as follows:

- **Imports**: The necessary libraries are imported, including `tkinter`, `ttk`, and custom logic for the chatbot.
- **Custom Widgets**: 
  - `RoundedFrame`: A custom frame with rounded corners.
  - `RoundedEntryFrame`: A custom entry field with rounded corners.
  - `ScrolledFrame`: A frame that allows for scrolling content.
- **ModernChatbotGUI Class**: The main class that initializes the GUI, handles user input, and generates responses.

### Chatbot Logic (`chatbot_logic.py`)

The chatbot logic is defined in a separate module, which includes:

- **get_random_agent_name**: Returns a random name for the assistant.
- **generate_response**: Generates a response based on user input, using regular expressions to match patterns for greetings, feelings, and facility information.

## Usage

1. Launch the application.
2. Enter your name and optionally provide a name for your assistant.
3. Start chatting with the assistant by typing your messages in the input field.
4. Use exit phrases like "bye" or "quit" to close the application.

## Example Queries

- "Where is the library?"
- "When does the coffee shop open?"
- "Hello!"
- "I'm feeling great!"

## Code Snippet

License

This project is licensed under the MIT License. Feel free to modify and distribute it as you wish.
Acknowledgments

    Tkinter for the GUI framework.
    Python for the programming language.
    Various online resources for inspiration and guidance in chatbot development.


You can save this content in a file named `README.md` in your project directory. This file provides a comprehensive overview of the chatbot application, its features, and how to use it.

Here is a snippet of the main application code:

```python
class ModernChatbotGUI:
    # Initialization and setup methods
    def __init__(self):
        self.window = tk.Tk()
        self.setup_window()
        self.create_styles()
        self.create_widgets()
        self.name = None
        self.chatbot_name = None

    def handle_user_input(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return
        self.add_message(user_input, is_user=True)
        response = generate_response(user_input)
        self.add_message(response, is_user=False)
        self.entry.delete(0, tk.END)
