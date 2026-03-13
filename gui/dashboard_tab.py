import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from storage import LOW_STOCK_THRESHOLD

class DashboardTab:
    def __init__(self, parent, storage):
        self.frame = tk.Frame(parent)
        self.storage = storage

        btn_frame = tk.Frame(self.frame)
        btn_frame.pack(fill="x", padx=10, pady=5)
        tk.Button(btn_frame, text="Rafraîchir", command=self.refresh).pack(side="left")

        self.stats_frame = tk.Frame(self.frame)
        self.stats_frame.pack(fill="x", padx=10)

        self.canvas_frame = tk.Frame(self.frame)
        self.canvas_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.refresh()

    def refresh(self):
        for w in self.stats_frame.winfo_children():
            w.destroy()
        for w in self.canvas_frame.winfo_children():
            w.destroy()

        products = self.storage.products
        sales = self.storage.sales

        total_products = len(products)
        total_stock = sum(p.quantity for p in products)
        total_value = sum(p.price * p.quantity for p in products)
        alerts = sum(1 for p in products if p.quantity <= LOW_STOCK_THRESHOLD)
        total_sales = sum(s.total for s in sales)

        stats = [
            ("Produits", total_products),
            ("Stock total", total_stock),
            ("Valeur stock", f"{total_value:.2f} €"),
            ("Alertes", alerts),
            ("CA total", f"{total_sales:.2f} €"),
        ]
        for i, (label, val) in enumerate(stats):
            f = tk.Frame(self.stats_frame, bd=1, relief="groove", padx=15, pady=8)
            f.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
            tk.Label(f, text=label, font=("Helvetica", 9)).pack()
            tk.Label(f, text=str(val), font=("Helvetica", 14, "bold")).pack()
        self.stats_frame.columnconfigure(list(range(len(stats))), weight=1)

        fig = Figure(figsize=(12, 4), dpi=85)

        ax1 = fig.add_subplot(131)
        if products:
            names = [p.name[:15] for p in products[:15]]
            qtys = [p.quantity for p in products[:15]]
            colors = ["#e74c3c" if p.quantity <= LOW_STOCK_THRESHOLD else "#2ecc71" for p in products[:15]]
            ax1.barh(names, qtys, color=colors)
            ax1.set_title("Stock actuel")
            ax1.set_xlabel("Quantité")
        else:
            ax1.text(0.5, 0.5, "Aucun produit", ha="center", va="center")
            ax1.set_title("Stock actuel")

        ax2 = fig.add_subplot(132)
        daily = {}
        for s in sales:
            day = s.date[:10]
            daily[day] = daily.get(day, 0) + s.total
        if daily:
            sorted_days = sorted(daily.keys())[-7:]
            ax2.bar([d[5:] for d in sorted_days], [daily[d] for d in sorted_days], color="#3498db")
            ax2.set_title("Ventes (7 derniers jours)")
            ax2.set_ylabel("€")
            ax2.tick_params(axis='x', rotation=45)
        else:
            ax2.text(0.5, 0.5, "Aucune vente", ha="center", va="center")
            ax2.set_title("Ventes récentes")

        ax3 = fig.add_subplot(133)
        product_sales = {}
        for s in sales:
            product_sales[s.product_name] = product_sales.get(s.product_name, 0) + s.quantity
        if product_sales:
            top = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:5]
            ax3.pie([v for _, v in top], labels=[n[:12] for n, _ in top], autopct="%1.0f%%", startangle=90)
            ax3.set_title("Top 5 ventes")
        else:
            ax3.text(0.5, 0.5, "Aucune vente", ha="center", va="center")
            ax3.set_title("Top 5 ventes")

        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
