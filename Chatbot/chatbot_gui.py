import tkinter as tk
from tkinter import ttk
from chatbot_logic import get_random_agent_name, generate_response
from datetime import datetime

# Add rounded rectangle method to Canvas
tk.Canvas.create_rounded_rectangle = lambda self, x1, y1, x2, y2, radius=25, **kwargs: \
    self.create_polygon(
        x1+radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1,
        smooth=True,
        **kwargs
    )

class RoundedFrame(tk.Canvas):
    def __init__(self, parent, width, height, corner_radius, color, **kwargs):
        tk.Canvas.__init__(self, parent, width=width, height=height, bg=parent.cget('bg'), highlightthickness=0, **kwargs)
        self.corner_radius = corner_radius
        self.color = color
        self.width = width
        self.height = height
        self.draw_rounded_rect()
        
    def draw_rounded_rect(self):
        self.create_rounded_rectangle(
            2, 2, self.width-2, self.height-2,
            radius=self.corner_radius,
            fill=self.color,
            outline=self.color
        )

class RoundedEntryFrame(tk.Frame):
    def __init__(self, parent, width, height, corner_radius, color, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(bg=parent.cget('bg'))  # Match parent background
        
        self.canvas = tk.Canvas(
            self,
            width=width,
            height=height,
            bg=parent.cget('bg'),  # Match parent background
            highlightthickness=0  # Remove canvas border
        )
        self.canvas.pack(fill='both', expand=True)
        
        self.canvas.create_rounded_rectangle(
            2, 2, width-2, height-2,
            radius=corner_radius,
            fill=color,
            outline=color  # Remove outline by matching fill color
        )
        
        self.entry = tk.Entry(
            self,
            font=("Helvetica", 12),
            bg=color,  # Match the rounded rectangle color
            fg="#FFFFFF",  # Text color
            insertbackground="#FFFFFF",  # Cursor color
            relief='flat',  # Remove 3D border
            bd=0  # No border width
        )
        self.canvas.create_window(
            width//2,
            height//2,
            window=self.entry,
            width=width-20,  # Adjust width for padding
            height=height-10  # Adjust height for padding
        )

    def get(self):
        return self.entry.get()

    def delete(self, first, last):
        return self.entry.delete(first, last)

    def bind(self, sequence, func):
        return self.entry.bind(sequence, func)

    def focus(self):
        return self.entry.focus()


class ScrolledFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.canvas = tk.Canvas(self, borderwidth=0, background="#000000")
        self.viewPort = tk.Frame(self.canvas, background="#000000")
        
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.viewPort, anchor="nw", tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

class ModernChatbotGUI:
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 800
    PRIMARY_COLOR = "#424242"
    SECONDARY_COLOR = "#BDBDBD"
    BACKGROUND_COLOR = "#000000"
    USER_MSG_COLOR = "#616161"
    BOT_MSG_COLOR = "#9E9E9E"
    TEXT_COLOR = "#FFFFFF"
    INPUT_HEIGHT = 40

    EXIT_PHRASES = {
        "bye", "quit", "exit", "shutdown", "good bye", "goodbye",
        "you can go", "sleep", "close", "ok bye", "okay bye"
    }

    def __init__(self):
        self.window = tk.Tk()
        self.setup_window()
        self.create_styles()
        self.create_widgets()
        self.name = None
        self.chatbot_name = None

    def setup_window(self):
        self.window.title("Modern Chat Assistant")
        self.window.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.window.configure(bg=self.BACKGROUND_COLOR)
        
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - self.WINDOW_WIDTH) // 2
        y = (screen_height - self.WINDOW_HEIGHT) // 2
        self.window.geometry(f"+{x}+{y}")

    def create_styles(self):
        style = ttk.Style()
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
        style.configure(
            'Modern.TFrame',
            background=self.BACKGROUND_COLOR
        )

    def create_message_bubble(self, message, is_user=True):
        bubble_color = self.USER_MSG_COLOR if is_user else self.BOT_MSG_COLOR
        bubble_frame = RoundedFrame(
            self.chat_log.viewPort,
            width=self.WINDOW_WIDTH - 40,
            height=60,
            corner_radius=20,
            color=bubble_color
        )
        
        time_label = tk.Label(
            bubble_frame,
            text=datetime.now().strftime("%H:%M"),
            font=("Helvetica", 8),
            fg="#757575",
            bg=bubble_color
        )
        time_label.pack(anchor="e", padx=5, pady=(2, 0))
        
        msg_label = tk.Label(
            bubble_frame,
            text=message,
            wraplength=self.WINDOW_WIDTH - 80,
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
        self.main_frame = ttk.Frame(self.window, style='Modern.TFrame')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.chat_container = tk.Frame(self.main_frame, bg=self.BACKGROUND_COLOR)
        self.chat_container.pack(fill=tk.BOTH, expand=True)

        self.chat_log = ScrolledFrame(self.chat_container)
        self.chat_log.pack(fill=tk.BOTH, expand=True)

        self.welcome_frame = tk.Frame(self.main_frame, bg=self.BACKGROUND_COLOR)
        self.welcome_frame.pack(fill=tk.X, pady=20)

        tk.Label(
            self.welcome_frame,
            text="Welcome to Modern Chat Assistant",
            font=("Helvetica", 24, "bold"),
            fg=self.SECONDARY_COLOR,
            bg=self.BACKGROUND_COLOR
        ).pack(pady=(0, 20))

        self.name_frame = tk.Frame(self.welcome_frame, bg=self.BACKGROUND_COLOR)
        self.name_frame.pack(fill=tk.X, pady=10)

        tk.Label(
            self.name_frame,
            text="What's your name?",
            font=("Helvetica", 12),
            bg=self.BACKGROUND_COLOR,
            fg=self.TEXT_COLOR
        ).pack(pady=5)

        self.name_entry = RoundedEntryFrame(
            self.name_frame,
            width=self.WINDOW_WIDTH - 200,
            height=self.INPUT_HEIGHT,
            corner_radius=20,
            color=self.PRIMARY_COLOR
        )
        self.name_entry.pack(pady=5)

        tk.Label(
            self.name_frame,
            text="Give your assistant a name (optional)",
            font=("Helvetica", 12),
            bg=self.BACKGROUND_COLOR,
            fg=self.TEXT_COLOR
        ).pack(pady=5)

        self.chatbot_name_entry = RoundedEntryFrame(
            self.name_frame,
            width=self.WINDOW_WIDTH - 200,
            height=self.INPUT_HEIGHT,
            corner_radius=20,
            color=self.PRIMARY_COLOR
        )
        self.chatbot_name_entry.pack(pady=5)

        self.start_button = ttk.Button(
            self.name_frame,
            text="Start Chatting",
            style='Modern.TButton',
            command=self.handle_name_submission
        )
        self.start_button.pack(pady=20)

        self.input_frame = tk.Frame(self.main_frame, bg=self.BACKGROUND_COLOR)
        self.entry = RoundedEntryFrame(
            self.input_frame,
            width=self.WINDOW_WIDTH - 120,
            height=self.INPUT_HEIGHT,
            corner_radius=20,
            color=self.PRIMARY_COLOR
        )

        self.submit_button = ttk.Button(
            self.input_frame,
            text="Send",
            style='Modern.TButton',
            command=self.handle_user_input
        )

        self.name_entry.bind("<Return>", self.handle_name_submission)
        self.chatbot_name_entry.bind("<Return>", self.handle_name_submission)
        self.entry.bind("<Return>", self.handle_user_input)

    def handle_name_submission(self, event=None):
        self.name = self.name_entry.get() or "Friend"
        self.chatbot_name = self.chatbot_name_entry.get() or get_random_agent_name()

        self.welcome_frame.pack_forget()
        
        self.input_frame.pack(fill=tk.X, pady=10)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.submit_button.pack(side=tk.RIGHT)
        
        welcome_msg = f"Welcome {self.name}! I'm {self.chatbot_name}, your personal assistant. How can I help you today?"
        self.add_message(welcome_msg, is_user=False)
        
        self.entry.focus()

    def add_message(self, message, is_user=True):
        bubble = self.create_message_bubble(message, is_user)
        bubble.pack(anchor="e", padx=10, pady=5, fill="x")
        self.chat_log.update_idletasks()
        self.chat_log.canvas.yview_moveto(1.0)

    def handle_user_input(self, event=None):
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
        return any(phrase in user_input.lower() for phrase in self.EXIT_PHRASES)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    chat_app = ModernChatbotGUI()
    chat_app.run()