import tkinter as tk
from tkinter import ttk, messagebox

class UsersTab:
    def __init__(self, parent, user_manager):
        self.frame = tk.Frame(parent)
        self.um = user_manager

        form = tk.Frame(self.frame)
        form.pack(fill="x", padx=10, pady=5)

        tk.Label(form, text="Utilisateur").grid(row=0, column=0, padx=5)
        self.entry_user = tk.Entry(form, width=15)
        self.entry_user.grid(row=0, column=1, padx=5)

        tk.Label(form, text="Mot de passe").grid(row=0, column=2, padx=5)
        self.entry_pass = tk.Entry(form, width=15, show="*")
        self.entry_pass.grid(row=0, column=3, padx=5)

        tk.Label(form, text="Rôle").grid(row=0, column=4, padx=5)
        self.combo_role = ttk.Combobox(form, values=["admin", "readonly"], state="readonly", width=10)
        self.combo_role.set("readonly")
        self.combo_role.grid(row=0, column=5, padx=5)

        tk.Button(form, text="Ajouter", command=self.add_user).grid(row=0, column=6, padx=5)
        tk.Button(form, text="Supprimer", command=self.delete_user).grid(row=0, column=7, padx=5)

        self.tree = ttk.Treeview(self.frame, columns=("user", "role"), show="headings", height=12)
        self.tree.heading("user", text="Utilisateur")
        self.tree.heading("role", text="Rôle")
        self.tree.column("user", width=200)
        self.tree.column("role", width=120)
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        self.refresh()

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        for u in self.um.list_users():
            self.tree.insert("", "end", values=(u["username"], u["role"]))

    def add_user(self):
        user = self.entry_user.get().strip()
        pwd = self.entry_pass.get().strip()
        role = self.combo_role.get()
        if not user or not pwd:
            messagebox.showwarning("Attention", "Remplissez tous les champs")
            return
        if self.um.add_user(user, pwd, role):
            self.refresh()
            self.entry_user.delete(0, "end")
            self.entry_pass.delete(0, "end")
        else:
            messagebox.showerror("Erreur", "Utilisateur déjà existant")

    def delete_user(self):
        sel = self.tree.selection()
        if not sel:
            return
        user = self.tree.item(sel[0])["values"][0]
        if messagebox.askyesno("Confirmer", f"Supprimer l'utilisateur '{user}' ?"):
            if self.um.delete_user(user):
                self.refresh()
            else:
                messagebox.showerror("Erreur", "Impossible de supprimer cet utilisateur")
