import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class SalesTab(ttk.Frame):
    def __init__(self, parent, storage, products_tab):
        super().__init__(parent)
        self.storage = storage
        self.products_tab = products_tab

        form = ttk.LabelFrame(self, text="Enregistrer une vente")
        form.pack(fill="x", padx=8, pady=6)

        ttk.Label(form, text="Réf. produit :").grid(row=0, column=0, padx=4, pady=3, sticky="e")
        self.ref_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.ref_var, width=20).grid(row=0, column=1, padx=4)

        ttk.Label(form, text="Quantité :").grid(row=0, column=2, padx=4, sticky="e")
        self.qty_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.qty_var, width=10).grid(row=0, column=3, padx=4)

        ttk.Label(form, text="Date (AAAA-MM-JJ) :").grid(row=0, column=4, padx=4, sticky="e")
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        ttk.Entry(form, textvariable=self.date_var, width=14).grid(row=0, column=5, padx=4)

        ttk.Button(form, text="✅ Enregistrer", command=self._record).grid(row=0, column=6, padx=8)

        cols = ("date", "ref", "product", "qty", "unit_price", "total")
        self.tree = ttk.Treeview(self, columns=cols, show="headings")
        for cid, text, w in [
            ("date", "Date", 100), ("ref", "Réf.", 90), ("product", "Produit", 180),
            ("qty", "Qté", 60), ("unit_price", "Prix unit.", 90), ("total", "Total (€)", 100),
        ]:
            self.tree.heading(cid, text=text)
            self.tree.column(cid, width=w, anchor="center")

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(fill="both", expand=True, padx=8, pady=4, side="left")
        scrollbar.pack(fill="y", side="left")

        self._refresh()

    def _refresh(self):
        self.tree.delete(*self.tree.get_children())
        for s in reversed(self.storage.sales):
            self.tree.insert("", "end", values=(s.date, s.reference, s.product_name,
                                                  s.quantity, f"{s.unit_price:.2f}", f"{s.total:.2f}"))

    def _record(self):
        ref = self.ref_var.get().strip()
        date_str = self.date_var.get().strip()
        try:
            qty = int(self.qty_var.get().strip())
            if qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erreur", "Quantité invalide.")
            return
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Erreur", "Format de date invalide (AAAA-MM-JJ).")
            return
        try:
            sale = self.storage.record_sale(ref, qty, date_str)
            self._refresh()
            self.products_tab._refresh()
            messagebox.showinfo("Vente enregistrée",
                                f"{sale.product_name} × {qty} = {sale.total:.2f} €")
            if self.storage.find_product(ref) and self.storage.find_product(ref).quantity <= 5:
                messagebox.showwarning("⚠ Stock faible",
                                       f"Le stock de '{sale.product_name}' est maintenant à {self.storage.find_product(ref).quantity}.")
        except (KeyError, ValueError) as e:
            messagebox.showerror("Erreur", str(e))
