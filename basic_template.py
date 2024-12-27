import tkinter as tk
import random

# Function to get a random agent name from a predefined list
def get_agent_name():
    agent_names = ["Alex", "Charlie", "Jordon", "Taylor", "Casey"]
    return random.choice(agent_names)

# Function to handle user input from the entry field
def handle_user_input():
    user_input = entry.get()  # Get the text entered by the user
    # Check if the user wants to quit the application
    if user_input.lower() in ["bye", "quit", "exit"]:
        window.quit()  # Close the application
    else:
        response = generate_response(user_input)  # Generate a response based on user input
        chat_log.config(state=tk.NORMAL)  # Enable chat log to insert new text
        chat_log.insert(tk.END, f":User  {user_input}\nAgent: {response}\n\n")  # Display user input and agent response
        chat_log.config(state=tk.DISABLED)  # Disable chat log to prevent user editing

        entry.delete(0, tk.END)  # Clear the entry field for new input

# Function to generate a response based on user input
def generate_response(user_input):
    # Predefined responses based on specific keywords
    responses = {
        "coffee": "The campus coffee bar opens from 8:00 AM to 5:00 PM",
        "library": "The library is open from 9:00 AM to 6:00 PM",
        "admission": "For Admission inquiries, please visit our admission page",
        "courses": "You can check the available courses in the student portal"
    }

    # Check if any keyword from the responses is in the user input
    for keyword, response in responses.items():
        if keyword.lower() in user_input.lower():
            return response  # Return the corresponding response if a keyword is found

    # If no keywords match, return a random generic response
    random_responses = [
        "I didn't quite get that. Can you please rephrase it?",
        "Tell me more",
        "That's quite interesting, tell me more",
        "I'm here to help, what else would you like to know?"
    ]
    return random.choice(random_responses)  # Return a random response

# Create the main application window
window = tk.Tk()
window.title("Samaaye Interactive Bot")  # Set the title of the window

# Prompt the user to enter their name
name = input("Enter your name:")  
agent_name = get_agent_name()  # Get a random agent name

# Create a text area for displaying the chat log
chat_log = tk.Text(window, state=tk.DISABLED, height=20, width=50)
chat_log.pack()

# Enable chat log to insert the welcome message
chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, f"Hello {name}! I'm {agent_name}, your virtual assistant. How can I help you today?\n\n")
chat_log.config(state=tk.DISABLED)  # Disable chat log to prevent user editing

# Create an entry field for user input
entry = tk.Entry(window, width=50)
entry.pack()

# Create a button that triggers the handle_user_input function when clicked
submit_button = tk.Button(window, text="Ask", command=handle_user_input)
submit_button.pack()

# Start the main event loop of the application
window.mainloop()