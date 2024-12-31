# Samaaye Interactive Bot

## Description

Samaaye Interactive Bot is a simple chatbot application built using Python's `tkinter` library. This chatbot is designed to provide responses to questions related to a fictional university's services, such as library hours, coffee bar timings, admission information, and available courses. The bot randomly generates an agent name and responds to user queries accordingly.

The application provides a GUI where users can ask questions, and the chatbot will respond based on predefined keywords. If no matching keyword is found, the chatbot will provide a generic response. The chatbot continues to interact with the user until the user types "bye", "quit", or "exit" to end the conversation.

## Features

- Modern and clean GUI design
- User and chatbot message bubbles with timestamps
- Basic natural language processing for greetings, feelings, and common campus-related queries
- Configurable chatbot and user names
- Easy to extend and customize
- Responses based on specific keywords such as `coffee`, `library`, `admission`, and `courses`
- Default random responses for unrecognized queries
- User can end the conversation by typing "bye", "quit", or "exit"

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/samaaye-interactive-bot.git
    cd samaaye-interactive-bot
    ```

2. **Install the required dependencies:**

    This project requires Python 3.x. Install the dependencies using pip:

    ```sh
    pip install -r requirements.txt
    ```

    Note: If you don't have a `requirements.txt` file, you can create one with the following content:

    ```txt
    tkinter
    ```

## Usage

1. **Run the Chatbot GUI:**

    ```sh
    python gui.py
    ```

2. **Interact with the Chatbot:**

    - Enter your name and optionally give your chatbot a name.
    - Type your messages in the input field and press Enter or click the Send button to interact with the chatbot.
    - The chatbot can respond to greetings, feelings, and common campus-related queries.

## Project Structure

- `gui.py`: Contains the `ModernChatbotGUI` class that defines the GUI and handles user interactions.
- `logic.py`: Contains the functions `get_random_agent_name` and `generate_response` which provide random chatbot names and generate responses based on user input.

## Customization

### Adding New Responses

To add new responses or patterns for the chatbot to recognize, update the dictionaries in `logic.py`:

- **Greetings**: Add new greeting patterns and responses in the `greetings` dictionary.
- **How are you**: Add new patterns and responses in the `how_are_you` dictionary.
- **Feelings**: Add new patterns and responses in the `feelings` dictionary.
- **Location queries**: Add new location keywords and responses in the `location_queries` dictionary.

### Changing Styles

To change the look and feel of the GUI, update the style configurations in the `create_styles` method in `gui.py`:

```python
style.configure(
    'Modern.TEntry',
    fieldbackground='white',
    borderwidth=0,
    relief='flat'
)

style.configure(
    'Modern.TButton',
    background=self.PRIMARY_COLOR,
    foreground='white',
    borderwidth=0,
    focuscolor=self.PRIMARY_COLOR,
    lightcolor=self.PRIMARY_COLOR,
    darkcolor=self.PRIMARY_COLOR,
    relief='flat',
    padding=(20, 10)
)


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The project uses Python's `tkinter` library for GUI development.
- Thanks to the contributors and the open-source community for their support.

---

Feel free to customize this README file further based on your specific requirements and project details.
```

This `README.md` file incorporates all the details from the previous `README.md` and includes the updated information.
