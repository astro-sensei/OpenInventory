import tkinter as tk
from tkinter import ttk, messagebox
from models import Supplier
from gui.dialogs import SupplierDialog


class SuppliersTab(ttk.Frame):
    def __init__(self, parent, storage):
        super().__init__(parent)
        self.storage = storage

        toolbar = ttk.Frame(self)
        toolbar.pack(fill="x", padx=4, pady=4)
        ttk.Button(toolbar, text="➕ Ajouter", command=self._add).pack(side="left", padx=2)
        ttk.Button(toolbar, text="✏ Modifier", command=self._edit).pack(side="left", padx=2)
        ttk.Button(toolbar, text="🗑 Supprimer", command=self._delete).pack(side="left", padx=2)

        cols = ("name", "contact", "products")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", selectmode="browse")
        self.tree.heading("name", text="Nom")
        self.tree.heading("contact", text="Contact")
        self.tree.heading("products", text="Produits fournis")
        self.tree.column("name", width=180)
        self.tree.column("contact", width=200)
        self.tree.column("products", width=350)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(fill="both", expand=True, padx=4, side="left")
        scrollbar.pack(fill="y", side="left")

        self._refresh()

    def _refresh(self):
        self.tree.delete(*self.tree.get_children())
        for s in self.storage.suppliers:
            self.tree.insert("", "end", iid=s.name,
                             values=(s.name, s.contact, ", ".join(s.products)))

    def _selected_name(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Sélectionnez un fournisseur.")
            return None
        return sel[0]

    def _add(self):
        dlg = SupplierDialog(self, "Ajouter un fournisseur")
        self.wait_window(dlg)
        if not dlg.result:
            return
        r = dlg.result
        prods = [p.strip() for p in r["products"].split(",") if p.strip()]
        self.storage.add_supplier(Supplier(name=r["name"], contact=r["contact"], products=prods))
        self._refresh()

    def _edit(self):
        name = self._selected_name()
        if not name:
            return
        sup = next((s for s in self.storage.suppliers if s.name == name), None)
        if not sup:
            return
        dlg = SupplierDialog(self, "Modifier le fournisseur", defaults=sup.to_dict())
        self.wait_window(dlg)
        if not dlg.result:
            return
        r = dlg.result
        prods = [p.strip() for p in r["products"].split(",") if p.strip()]
        try:
            self.storage.update_supplier(name, name=r["name"], contact=r["contact"], products=prods)
            self._refresh()
        except KeyError as e:
            messagebox.showerror("Erreur", str(e))

    def _delete(self):
        name = self._selected_name()
        if not name:
            return
        if messagebox.askyesno("Confirmation", f"Supprimer le fournisseur '{name}' ?"):
            self.storage.delete_supplier(name)
            self._refresh()
