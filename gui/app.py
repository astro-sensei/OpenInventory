import tkinter as tk
from tkinter import ttk, messagebox
from storage import Storage
from gui.products_tab import ProductsTab
from gui.sales_tab import SalesTab
from gui.reports_tab import ReportsTab
from gui.suppliers_tab import SuppliersTab


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OpenInventory — Gestion des Stocks")
        self.geometry("1050x620")
        self.minsize(900, 500)

        self.storage = Storage()

        style = ttk.Style(self)
        style.theme_use("clam")

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=6, pady=6)

        self.products_tab = ProductsTab(notebook, self.storage)
        self.sales_tab = SalesTab(notebook, self.storage, self.products_tab)
        self.reports_tab = ReportsTab(notebook, self.storage)
        self.suppliers_tab = SuppliersTab(notebook, self.storage)

        notebook.add(self.products_tab, text="  Produits  ")
        notebook.add(self.sales_tab, text="  Ventes  ")
        notebook.add(self.reports_tab, text="  Rapports  ")
        notebook.add(self.suppliers_tab, text="  Fournisseurs  ")

        self._check_low_stock()

    def _check_low_stock(self):
        low = self.storage.low_stock()
        if low:
            names = "\n".join(f"  • {p.name} (réf: {p.reference}) — qté: {p.quantity}" for p in low)
            messagebox.showwarning("⚠ Stock faible", f"Les produits suivants ont un stock faible :\n\n{names}")
