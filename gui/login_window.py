import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, root, user_manager, on_success):
        self.root = root
        self.um = user_manager
        self.on_success = on_success
        self.root.title("OpenInventory — Connexion")
        self.root.geometry("350x220")
        self.root.resizable(False, False)

        frame = tk.Frame(root, padx=30, pady=20)
        frame.pack(expand=True)

        tk.Label(frame, text="OpenInventory", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

        tk.Label(frame, text="Utilisateur").grid(row=1, column=0, sticky="e", padx=5, pady=3)
        self.entry_user = tk.Entry(frame, width=20)
        self.entry_user.grid(row=1, column=1, pady=3)
        self.entry_user.insert(0, "admin")

        tk.Label(frame, text="Mot de passe").grid(row=2, column=0, sticky="e", padx=5, pady=3)
        self.entry_pass = tk.Entry(frame, width=20, show="*")
        self.entry_pass.grid(row=2, column=1, pady=3)

        tk.Button(frame, text="Connexion", command=self.login, width=15).grid(row=3, column=0, columnspan=2, pady=12)
        self.entry_pass.bind("<Return>", lambda e: self.login())
        self.entry_user.focus_set()

    def login(self):
        if self.um.authenticate(self.entry_user.get().strip(), self.entry_pass.get()):
            self.on_success()
        else:
            messagebox.showerror("Erreur", "Identifiants incorrects")
