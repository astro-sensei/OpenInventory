import tkinter as tk
from tkinter import ttk


class ProductDialog(tk.Toplevel):
    def __init__(self, parent, title="Produit", defaults=None):
        super().__init__(parent)
        self.title(title)
        self.resizable(False, False)
        self.grab_set()
        self.result = None

        labels = ["Nom", "Référence", "Quantité", "Prix unitaire", "Catégorie"]
        keys = ["name", "reference", "quantity", "price", "category"]
        self.entries = {}
        defaults = defaults or {}

        for i, (lbl, key) in enumerate(zip(labels, keys)):
            ttk.Label(self, text=lbl + " :").grid(row=i, column=0, padx=8, pady=4, sticky="e")
            e = ttk.Entry(self, width=30)
            e.grid(row=i, column=1, padx=8, pady=4)
            if key in defaults:
                e.insert(0, str(defaults[key]))
            self.entries[key] = e

        btn_frame = ttk.Frame(self)
        btn_frame.grid(row=len(labels), column=0, columnspan=2, pady=10)
        ttk.Button(btn_frame, text="Valider", command=self._on_ok).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Annuler", command=self.destroy).pack(side="left", padx=5)

        self.entries[keys[0]].focus_set()
        self.bind("<Return>", lambda e: self._on_ok())

    def _on_ok(self):
        self.result = {k: e.get().strip() for k, e in self.entries.items()}
        self.destroy()


class SupplierDialog(tk.Toplevel):
    def __init__(self, parent, title="Fournisseur", defaults=None):
        super().__init__(parent)
        self.title(title)
        self.resizable(False, False)
        self.grab_set()
        self.result = None

        labels = ["Nom", "Contact", "Produits fournis (séparés par ,)"]
        keys = ["name", "contact", "products"]
        self.entries = {}
        defaults = defaults or {}

        for i, (lbl, key) in enumerate(zip(labels, keys)):
            ttk.Label(self, text=lbl + " :").grid(row=i, column=0, padx=8, pady=4, sticky="e")
            e = ttk.Entry(self, width=40)
            e.grid(row=i, column=1, padx=8, pady=4)
            val = defaults.get(key, "")
            if isinstance(val, list):
                val = ", ".join(val)
            e.insert(0, str(val))
            self.entries[key] = e

        btn_frame = ttk.Frame(self)
        btn_frame.grid(row=len(labels), column=0, columnspan=2, pady=10)
        ttk.Button(btn_frame, text="Valider", command=self._on_ok).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Annuler", command=self.destroy).pack(side="left", padx=5)

        self.bind("<Return>", lambda e: self._on_ok())

    def _on_ok(self):
        self.result = {k: e.get().strip() for k, e in self.entries.items()}
        self.destroy()
