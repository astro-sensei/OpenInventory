import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from models import Product
from gui.dialogs import ProductDialog


class ProductsTab(ttk.Frame):
    def __init__(self, parent, storage):
        super().__init__(parent)
        self.storage = storage

        toolbar = ttk.Frame(self)
        toolbar.pack(fill="x", padx=4, pady=4)

        ttk.Button(toolbar, text="➕ Ajouter", command=self._add).pack(side="left", padx=2)
        ttk.Button(toolbar, text="✏ Modifier", command=self._edit).pack(side="left", padx=2)
        ttk.Button(toolbar, text="🗑 Supprimer", command=self._delete).pack(side="left", padx=2)

        ttk.Separator(toolbar, orient="vertical").pack(side="left", fill="y", padx=6)

        ttk.Label(toolbar, text="Recherche :").pack(side="left")
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(toolbar, textvariable=self.search_var, width=20)
        search_entry.pack(side="left", padx=2)
        search_entry.bind("<KeyRelease>", lambda e: self._refresh())

        ttk.Separator(toolbar, orient="vertical").pack(side="left", fill="y", padx=6)

        ttk.Label(toolbar, text="Trier par :").pack(side="left")
        self.sort_var = tk.StringVar(value="category")
        ttk.Radiobutton(toolbar, text="Catégorie", variable=self.sort_var, value="category", command=self._refresh).pack(side="left")
        ttk.Radiobutton(toolbar, text="Quantité", variable=self.sort_var, value="quantity", command=self._refresh).pack(side="left")

        ttk.Separator(toolbar, orient="vertical").pack(side="left", fill="y", padx=6)
        ttk.Button(toolbar, text="📥 Import Excel", command=self._import_excel).pack(side="right", padx=2)
        ttk.Button(toolbar, text="📤 Export Excel", command=self._export_excel).pack(side="right", padx=2)
        ttk.Button(toolbar, text="📤 Export CSV", command=self._export_csv).pack(side="right", padx=2)
        ttk.Button(toolbar, text="📥 Import CSV", command=self._import_csv).pack(side="right", padx=2)

        cols = ("ref", "name", "category", "quantity", "price")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", selectmode="browse")
        for cid, text, w in [
            ("ref", "Référence", 100), ("name", "Nom", 200),
            ("category", "Catégorie", 130), ("quantity", "Quantité", 80), ("price", "Prix (€)", 90),
        ]:
            self.tree.heading(cid, text=text)
            self.tree.column(cid, width=w, anchor="center" if cid in ("quantity", "price") else "w")

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(fill="both", expand=True, padx=4, side="left")
        scrollbar.pack(fill="y", side="left")

        self._refresh()

    def _refresh(self):
        self.tree.delete(*self.tree.get_children())
        query = self.search_var.get().strip()
        products = self.storage.search_products(query) if query else self.storage.products_sorted(self.sort_var.get())
        for p in products:
            tag = "low" if p.quantity <= 5 else ""
            self.tree.insert("", "end", iid=p.reference, values=(p.reference, p.name, p.category, p.quantity, f"{p.price:.2f}"), tags=(tag,))
        self.tree.tag_configure("low", background="#ffcccc")

    def _selected_ref(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Sélectionnez un produit.")
            return None
        return sel[0]

    def _add(self):
        dlg = ProductDialog(self, "Ajouter un produit")
        self.wait_window(dlg)
        if not dlg.result:
            return
        try:
            r = dlg.result
            p = Product(name=r["name"], reference=r["reference"],
                        quantity=int(r["quantity"]), price=float(r["price"]),
                        category=r["category"])
            if not p.name or not p.reference:
                raise ValueError("Nom et référence obligatoires.")
            self.storage.add_product(p)
            self._refresh()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def _edit(self):
        ref = self._selected_ref()
        if not ref:
            return
        p = self.storage.find_product(ref)
        dlg = ProductDialog(self, "Modifier le produit", defaults=p.to_dict())
        self.wait_window(dlg)
        if not dlg.result:
            return
        try:
            r = dlg.result
            self.storage.update_product(ref, name=r["name"], quantity=int(r["quantity"]),
                                        price=float(r["price"]), category=r["category"])
            self._refresh()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    def _delete(self):
        ref = self._selected_ref()
        if not ref:
            return
        if messagebox.askyesno("Confirmation", f"Supprimer le produit {ref} ?"):
            self.storage.delete_product(ref)
            self._refresh()

    def _export_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if path:
            self.storage.export_products_csv(path)
            messagebox.showinfo("OK", "Export CSV terminé.")

    def _import_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if path:
            self.storage.import_products_csv(path)
            self._refresh()
            messagebox.showinfo("OK", "Import CSV terminé.")

    def _export_excel(self):
        path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")])
        if path:
            try:
                self.storage.export_products_excel(path)
                messagebox.showinfo("OK", "Export Excel terminé.")
            except ImportError:
                messagebox.showerror("Erreur", "Installez openpyxl : pip install openpyxl")

    def _import_excel(self):
        path = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx")])
        if path:
            try:
                self.storage.import_products_excel(path)
                self._refresh()
                messagebox.showinfo("OK", "Import Excel terminé.")
            except ImportError:
                messagebox.showerror("Erreur", "Installez openpyxl : pip install openpyxl")
