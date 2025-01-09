import tkinter as tk
from tkinter import ttk
from chatbot_logic import get_random_agent_name, generate_response
from datetime import datetime

class RoundedFrame(tk.Canvas):
    """A custom frame with rounded corners."""
    def __init__(self, parent, width, height, corner_radius, color, **kwargs):
        tk.Canvas.__init__(self, parent, width=width, height=height, bg=color, **kwargs)
        self.corner_radius = corner_radius
        self.color = color
        self.width = width
        self.height = height
        self.draw_rounded_rect()
        
    def draw_rounded_rect(self):
        """Draw a rectangle with rounded corners."""
        self.create_arc((0, 0, 2*self.corner_radius, 2*self.corner_radius), start=90, extent=90, fill=self.color, outline=self.color)
        self.create_arc((self.width-2*self.corner_radius, 0, self.width, 2*self.corner_radius), start=0, extent=90, fill=self.color, outline=self.color)
        self.create_arc((0, self.height-2*self.corner_radius, 2*self.corner_radius, self.height), start=180, extent=90, fill=self.color, outline=self.color)
        self.create_arc((self.width-2*self.corner_radius, self.height-2*self.corner_radius, self.width, self.height), start=270, extent=90, fill=self.color, outline=self.color)
        self.create_rectangle((self.corner_radius, 0, self.width-self.corner_radius, self.height), fill=self.color, outline=self.color)
        self.create_rectangle((0, self.corner_radius, self.width, self.height-self.corner_radius), fill=self.color, outline=self.color)

class ScrolledFrame(tk.Frame):
    """A frame that allows vertical scrolling of its content."""
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.canvas = tk.Canvas(self, borderwidth=0, background="#000000")
        self.viewPort = tk.Frame(self.canvas, background="#000000")
        
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.viewPort, anchor="nw", 
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class ModernChatbotGUI:
    """A modern, aesthetically pleasing chatbot GUI implementation."""

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 800
    PRIMARY_COLOR = "#424242"  # Dark Gray
    SECONDARY_COLOR = "#BDBDBD"  # Light Gray
    BACKGROUND_COLOR = "#000000"  # Black
    USER_MSG_COLOR = "#616161"  # Medium Gray
    BOT_MSG_COLOR = "#9E9E9E"  # Light Gray
    TEXT_COLOR = "#FFFFFF"  # White

    EXIT_PHRASES = {
        "bye", "quit", "exit", "shutdown", "good bye", "goodbye",
        "you can go", "sleep", "close", "ok bye", "okay bye"
    }

    def __init__(self):
        """Initialize the modernized chatbot GUI."""
        self.window = tk.Tk()
        self.setup_window()
        self.create_styles()
        self.create_widgets()
        self.name = None
        self.chatbot_name = None

    def setup_window(self):
        """Configure the main window with modern styling."""
        self.window.title("Modern Chat Assistant")
        self.window.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.window.configure(bg=self.BACKGROUND_COLOR)
        
        # Center window
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - self.WINDOW_WIDTH) // 2
        y = (screen_height - self.WINDOW_HEIGHT) // 2
        self.window.geometry(f"+{x}+{y}")

    def create_styles(self):
        """Define modern custom styles for widgets."""
        style = ttk.Style()
        
        # Entry style
        style.configure(
            'Modern.TEntry',
            fieldbackground=self.PRIMARY_COLOR,
            foreground=self.TEXT_COLOR,
            borderwidth=0,
            relief='flat'
        )
        
        # Button style
        style.configure(
            'Modern.TButton',
            background=self.PRIMARY_COLOR,
            foreground=self.TEXT_COLOR,
            borderwidth=0,
            focuscolor=self.PRIMARY_COLOR,
            lightcolor=self.PRIMARY_COLOR,
            darkcolor=self.PRIMARY_COLOR,
            relief='flat',
            padding=(20, 10)
        )
        
        # Frame style
        style.configure(
            'Modern.TFrame',
            background=self.BACKGROUND_COLOR
        )

    def create_message_bubble(self, message, is_user=True):
        """Create a stylized message bubble frame."""
        bubble_color = self.USER_MSG_COLOR if is_user else self.BOT_MSG_COLOR
        bubble_frame = RoundedFrame(
            self.chat_log.viewPort,
            width=self.WINDOW_WIDTH - 40,  # Adjust width to fit the window
            height=60,  # Adjust height as needed
            corner_radius=20,
            color=bubble_color
        )
        
        # Time stamp
        time_label = tk.Label(
            bubble_frame,
            text=datetime.now().strftime("%H:%M"),
            font=("Helvetica", 8),
            fg="#757575",
            bg=bubble_color
        )
        time_label.pack(anchor="e", padx=5, pady=(2, 0))
        
        # Message content
        msg_label = tk.Label(
            bubble_frame,
            text=message,
            wraplength=self.WINDOW_WIDTH - 80,  # Adjust wrap length to fit the window
            justify="left",
            font=("Helvetica", 11),
            bg=bubble_color,
            fg=self.TEXT_COLOR,
            padx=10,
            pady=5
        )
        msg_label.pack(anchor="w" if is_user else "e", padx=5, pady=(0, 5))
        
        return bubble_frame

    def create_widgets(self):
        """Create and configure all GUI widgets with modern styling."""
        # Main container
        self.main_frame = ttk.Frame(self.window, style='Modern.TFrame')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Chat container
        self.chat_container = tk.Frame(self.main_frame, bg=self.BACKGROUND_COLOR)
        self.chat_container.pack(fill=tk.BOTH, expand=True)

        # Chat log with scrolling
        self.chat_log = ScrolledFrame(self.chat_container)
        self.chat_log.pack(fill=tk.BOTH, expand=True)

        # Welcome Frame
        self.welcome_frame = tk.Frame(self.main_frame, bg=self.BACKGROUND_COLOR)
        self.welcome_frame.pack(fill=tk.X, pady=20)

        # Welcome header
        tk.Label(
            self.welcome_frame,
            text="Welcome to Modern Chat Assistant",
            font=("Helvetica", 24, "bold"),
            fg=self.SECONDARY_COLOR,
            bg=self.BACKGROUND_COLOR
        ).pack(pady=(0, 20))

        # Name entry section
        self.name_frame = tk.Frame(self.welcome_frame, bg=self.BACKGROUND_COLOR)
        self.name_frame.pack(fill=tk.X, pady=10)

        tk.Label(
            self.name_frame,
            text="What's your name?",
            font=("Helvetica", 12),
            bg=self.BACKGROUND_COLOR,
            fg=self.TEXT_COLOR
        ).pack(pady=5)

        self.name_entry = ttk.Entry(
            self.name_frame,
            style='Modern.TEntry',
            font=("Helvetica", 12)
        )
        self.name_entry.pack(fill=tk.X, pady=5, padx=100)
        tk.Label(
            self.name_frame,
            text="Give your assistant a name (optional)",
            font=("Helvetica", 12),
            bg=self.BACKGROUND_COLOR,
            fg=self.TEXT_COLOR
        ).pack(pady=5)

        self.chatbot_name_entry = ttk.Entry(
            self.name_frame,
            style='Modern.TEntry',
            font=("Helvetica", 12)
        )
        self.chatbot_name_entry.pack(fill=tk.X, pady=5, padx=100)

        # Start button
        self.start_button = ttk.Button(
            self.name_frame,
            text="Start Chatting",
            style='Modern.TButton',
            command=self.handle_name_submission
        )
        self.start_button.pack(pady=20)

        # Input area
        self.input_frame = tk.Frame(self.main_frame, bg=self.BACKGROUND_COLOR)
        self.entry = ttk.Entry(
            self.input_frame,
            style='Modern.TEntry',
            font=("Helvetica", 12)
        )
        self.entry.bind("<Return>", self.handle_user_input)

        self.submit_button = ttk.Button(
            self.input_frame,
            text="Send",
            style='Modern.TButton',
            command=self.handle_user_input
        )

        # Bind enter key
        self.name_entry.bind("<Return>", self.handle_name_submission)
        self.chatbot_name_entry.bind("<Return>", self.handle_name_submission)

    def handle_name_submission(self, event=None):
        """Process the user's and chatbot's name submissions with animated transition."""
        self.name = self.name_entry.get() or "Friend"
        self.chatbot_name = self.chatbot_name_entry.get() or get_random_agent_name()

        # Fade out welcome frame
        self.welcome_frame.pack_forget()
        
        # Show input frame
        self.input_frame.pack(fill=tk.X, pady=10)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.submit_button.pack(side=tk.RIGHT)
        
        # Add welcome message
        welcome_msg = f"Welcome {self.name}! I'm {self.chatbot_name}, your personal assistant. How can I help you today?"
        self.add_message(welcome_msg, is_user=False)
        
        self.entry.focus()

    def add_message(self, message, is_user=True):
        """Add a new message bubble to the chat log."""
        bubble = self.create_message_bubble(message, is_user)
        bubble.pack(anchor="e", padx=10, pady=5, fill="x")  # Align to the right and fill width
        
        self.chat_log.update_idletasks()
        self.chat_log.canvas.yview_moveto(1.0)  # Auto-scroll to the bottom

    def handle_user_input(self, event=None):
        """Process user input and generate responses with modern styling."""
        user_input = self.entry.get().strip()
        if not user_input:
            return

        if self.is_exit_command(user_input):
            self.add_message(user_input, is_user=True)
            self.add_message(f"Goodbye {self.name}! Have a great day!", is_user=False)
            self.window.after(1500, self.window.quit)
            return

        self.add_message(user_input, is_user=True)
        response = generate_response(user_input)
        self.add_message(response, is_user=False)
        self.entry.delete(0, tk.END)

    def is_exit_command(self, user_input: str) -> bool:
        """Check if the user input is an exit command."""
        return any(phrase in user_input.lower() for phrase in self.EXIT_PHRASES)

    def run(self):
        """Start the chatbot application."""
        self.window.mainloop()

if __name__ == "__main__":
    chat_app = ModernChatbotGUI()
    chat_app.run()