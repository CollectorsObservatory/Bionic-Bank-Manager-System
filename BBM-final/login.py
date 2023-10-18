import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bionic Bank Manager")
        self.geometry("400x200")
        
        self.label = tk.Label(self, text="Enter password to access Bionic Bank Manager", font=("Arial", 14))
        self.label.pack(pady=20)

        self.password_entry = tk.Entry(self, show='*', font=("Arial", 12))
        self.password_entry.pack(pady=5)
        
        self.button = tk.Button(self, text="Authenticate", command=self.authenticate, font=("Arial", 12))
        self.button.pack()

    def authenticate(self):
        password = self.password_entry.get()
        if password == "admin123":
            self.label.config(text="Yeah buddy! You've accessed Bionic Bank Manager.")
            self.password_entry.pack_forget()  # Hide the password entry field
            self.button.pack_forget()  # Hide the Authenticate button
        else:
            messagebox.showwarning("Authentication Failed", "Incorrect password.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
