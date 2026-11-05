"""Entry point for the College Enquiry Chatbot."""
from gui import CollegeChatbotGUI
import tkinter as tk

def main():
    root = tk.Tk()
    CollegeChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
