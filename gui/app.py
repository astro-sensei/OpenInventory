import tkinter as tk
from tkinter import ttk, messagebox
import traceback
from storage import Storage
from user_manager import UserManager
from gui.login_window import LoginWindow
from gui.products_tab import ProductsTab
from gui.sales_tab import SalesTab
from gui.reports_tab import ReportsTab
from gui.suppliers_tab import SuppliersTab
from gui.dashboard_tab import DashboardTab
from gui.users_tab import UsersTab
from gui.theme import ThemeManager
from gui.pdf_export import PDFExporter

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.storage = Storage()
        self.um = UserManager()
        self.tm = ThemeManager()
        self.show_login()

    def show_login(self):
        for w in self.winfo_children():
            w.destroy()
        self.config(menu=tk.Menu(self))
        self.geometry("350x220")
        self.resizable(False, False)
        self.title("OpenInventory — Connexion")
        LoginWindow(self, self.um, self.on_login_success)

    def on_login_success(self):
        try:
            for w in self.winfo_children():
                w.destroy()
            self.geometry("1100x650")
            self.resizable(True, True)
            self.title(f"OpenInventory v1.1.0 — {self.um.current_user['username']} ({self.um.current_user['role']})")
            self.build_ui()
        except Exception as e:
            messagebox.showerror("Erreur build_ui", traceback.format_exc())

    def build_ui(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        menu_file = tk.Menu(menubar, tearoff=0)
        menu_file.add_command(label="Export PDF Inventaire", command=lambda: self._export_pdf_inv())
        menu_file.add_command(label="Export PDF Ventes", command=lambda: self._export_pdf_sales())
        menu_file.add_separator()
        menu_file.add_command(label="Déconnexion", command=self.show_login)
        menu_file.add_command(label="Quitter", command=self.quit)
        menubar.add_cascade(label="Fichier", menu=menu_file)

        # menu_view = tk.Menu(menubar, tearoff=0)
        # menu_view.add_command(label="Thème clair/sombre", command=lambda: self.toggle_theme())
        # menubar.add_cascade(label="Affichage", menu=menu_view)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        self.dashboard = DashboardTab(self.notebook, self.storage)
        self.notebook.add(self.dashboard.frame, text="Tableau de bord")

        self.products_tab = ProductsTab(self.notebook, self.storage)
        self.notebook.add(self.products_tab, text="Produits")

        self.sales_tab = SalesTab(self.notebook, self.storage, self.products_tab)
        self.notebook.add(self.sales_tab, text="Ventes")

        self.reports_tab = ReportsTab(self.notebook, self.storage)
        self.notebook.add(self.reports_tab, text="Rapports")

        self.suppliers_tab = SuppliersTab(self.notebook, self.storage)
        self.notebook.add(self.suppliers_tab, text="Fournisseurs")

        if self.um.is_admin():
            self.users_tab = UsersTab(self.notebook, self.um)
            self.notebook.add(self.users_tab.frame, text="Utilisateurs")

        if not self.um.is_admin():
            self._apply_readonly()

    def _apply_readonly(self):
        for tab in [self.products_tab, self.sales_tab]:
            self._disable_buttons(tab)

    def _disable_buttons(self, widget):
        if isinstance(widget, tk.Button):
            try:
                widget.configure(state="disabled")
            except:
                pass
        for child in widget.winfo_children():
            self._disable_buttons(child)

    def toggle_theme(self):
        t = self.tm.toggle()
        self.configure(bg=t["bg"])
        style = ttk.Style()
        style.configure("Treeview",
                        background=t["tree_bg"],
                        foreground=t["tree_fg"],
                        fieldbackground=t["tree_bg"])
        style.map("Treeview", background=[("selected", t["tree_select"])])
        style.configure("TNotebook", background=t["bg"])
        style.configure("TNotebook.Tab", background=t["button_bg"], foreground=t["button_fg"])
        self.tm.apply(self)

    def _export_pdf_inv(self):
        try:
            path = PDFExporter.export_inventory(self.storage.get_products())
            messagebox.showinfo("Export PDF", f"Inventaire exporté :\n{path}")
        except Exception as e:
            messagebox.showerror("Erreur", traceback.format_exc())

    def _export_pdf_sales(self):
        try:
            path = PDFExporter.export_sales(self.storage.get_sales())
            messagebox.showinfo("Export PDF", f"Ventes exportées :\n{path}")
        except Exception as e:
            messagebox.showerror("Erreur", traceback.format_exc())
