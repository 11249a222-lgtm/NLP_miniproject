"""Tkinter graphical user interface for the College Enquiry Chatbot."""
import tkinter as tk
from tkinter import scrolledtext
from chatbot import CollegeChatbot
from knowledge_base import COLLEGE_FAQS

class CollegeChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("College Enquiry Chatbot")
        self.root.geometry("680x620")
        self.root.minsize(500, 450)
        self.root.configure(bg="#f1f5f9")

        self.bot = CollegeChatbot(COLLEGE_FAQS)

        title = tk.Label(
            root, text="COLLEGE ENQUIRY CHATBOT",
            font=("Arial", 18, "bold"), bg="#1e3a8a",
            fg="white", pady=15
        )
        title.pack(fill=tk.X)

        subtitle = tk.Label(
            root,
            text="Ask about admissions, courses, fees and college facilities",
            font=("Arial", 10), bg="#f1f5f9", fg="#334155", pady=8
        )
        subtitle.pack()

        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, font=("Arial", 11),
            bg="white", fg="#111827", state=tk.DISABLED,
            padx=10, pady=10
        )
        self.chat_area.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

        input_frame = tk.Frame(root, bg="#f1f5f9")
        input_frame.pack(fill=tk.X, padx=15, pady=12)

        self.entry = tk.Entry(input_frame, font=("Arial", 12))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
        self.entry.bind("<Return>", self.send_message)

        send_button = tk.Button(
            input_frame, text="Send", font=("Arial", 11, "bold"),
            bg="#2563eb", fg="white", command=self.send_message,
            padx=18, pady=7
        )
        send_button.pack(side=tk.LEFT, padx=(8, 0))

        clear_button = tk.Button(
            root, text="Clear Chat", command=self.clear_chat,
            font=("Arial", 10), bg="#e2e8f0", fg="#1e293b"
        )
        clear_button.pack(pady=(0, 10))

        self.add_message(
            "Bot",
            "Hello! Welcome to the College Enquiry Chatbot. Ask me about "
            "admissions, courses, fees, hostel, transport, library, exams or placements."
        )
        self.entry.focus_set()

    def add_message(self, sender, message):
        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_area.configure(state=tk.DISABLED)
        self.chat_area.see(tk.END)

    def send_message(self, event=None):
        user_message = self.entry.get().strip()
        if not user_message:
            return
        self.add_message("You", user_message)
        self.entry.delete(0, tk.END)
        self.add_message("Bot", self.bot.get_response(user_message))

    def clear_chat(self):
        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.configure(state=tk.DISABLED)
        self.add_message("Bot", "Chat cleared. How can I help you?")
