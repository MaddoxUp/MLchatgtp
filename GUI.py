# main.py

import tkinter as tk
from tkinter import messagebox
import openai
# Assume the other scripts you mentioned are imported here...

class ChatWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.create_widgets()
        # Initialize other attributes here...

    def create_widgets(self):
        self.create_chatbox()
        self.create_entrybox()
        self.create_send_button()
        self.create_setting_button()

    def create_chatbox(self):
        self.chatbox = tk.Text(self.root)
        self.chatbox.pack()

    def create_entrybox(self):
        self.entrybox = tk.Text(self.root)
        self.entrybox.pack()

    def create_send_button(self):
        self.send_button = tk.Button(self.root, text="Send", command=self.send)
        self.send_button.pack()

    def create_setting_button(self):
        self.setting_button = tk.Button(self.root, text="Setting", command=self.open_setting)
        self.setting_button.pack()

    def send(self):
        user_input = self.entrybox.get("1.0", 'end-1c')
        self.entrybox.delete('1.0', tk.END)
        # Process the user input here...

    def open_setting(self):
        # Open the setting window here...
        pass

    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    window = ChatWindow()
    window.mainloop()
