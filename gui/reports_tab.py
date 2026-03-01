import tkinter as tk
from tkinter import ttk


class ReportsTab(ttk.Frame):
    def __init__(self, parent, storage):
        super().__init__(parent)
        self.storage = storage

        btn_bar = ttk.Frame(self)
        btn_bar.pack(fill="x", padx=6, pady=6)

        ttk.Button(btn_bar, text="Stock min/max", command=self._stock_extremes).pack(side="left", padx=3)
        ttk.Button(btn_bar, text="Produits les + vendus", command=self._top_sold).pack(side="left", padx=3)
        ttk.Button(btn_bar, text="CA par catégorie", command=self._revenue_cat).pack(side="left", padx=3)
        ttk.Button(btn_bar, text="CA total", command=self._total_revenue).pack(side="left", padx=3)
        ttk.Button(btn_bar, text="Produits stock faible", command=self._low_stock).pack(side="left", padx=3)

        ttk.Separator(btn_bar, orient="vertical").pack(side="left", fill="y", padx=8)
        ttk.Label(btn_bar, text="Du :").pack(side="left")
        self.start_var = tk.StringVar()
        ttk.Entry(btn_bar, textvariable=self.start_var, width=12).pack(side="left", padx=2)
        ttk.Label(btn_bar, text="Au :").pack(side="left")
        self.end_var = tk.StringVar()
        ttk.Entry(btn_bar, textvariable=self.end_var, width=12).pack(side="left", padx=2)

        self.text = tk.Text(self, wrap="word", font=("Consolas", 11))
        self.text.pack(fill="both", expand=True, padx=6, pady=4)

    def _write(self, content):
        self.text.delete("1.0", "end")
        self.text.insert("1.0", content)

    def _period(self):
        s = self.start_var.get().strip() or None
        e = self.end_var.get().strip() or None
        return s, e

    def _stock_extremes(self):
        mn, mx = self.storage.stock_extremes()
        if not mn:
            self._write("Aucun produit en stock.")
            return
        self._write(
            f"📉 Stock le plus bas :\n   {mn.name} (réf: {mn.reference}) — {mn.quantity} unités\n\n"
            f"📈 Stock le plus haut :\n   {mx.name} (réf: {mx.reference}) — {mx.quantity} unités"
        )

    def _top_sold(self):
        s, e = self._period()
        top = self.storage.top_sold(s, e)
        if not top:
            self._write("Aucune vente enregistrée pour cette période.")
            return
        lines = ["🏆 Produits les plus vendus :\n"]
        for i, (name, qty) in enumerate(top, 1):
            lines.append(f"   {i}. {name} — {qty} unité(s)")
        self._write("\n".join(lines))

    def _revenue_cat(self):
        s, e = self._period()
        rev = self.storage.revenue_by_category(s, e)
        if not rev:
            self._write("Aucune donnée.")
            return
        lines = ["💰 Chiffre d'affaires par catégorie :\n"]
        for cat, total in sorted(rev.items(), key=lambda x: -x[1]):
            lines.append(f"   {cat or 'N/A'} : {total:.2f} €")
        lines.append(f"\n   TOTAL : {sum(rev.values()):.2f} €")
        self._write("\n".join(lines))

    def _total_revenue(self):
        total = self.storage.total_revenue()
        self._write(f"💵 Chiffre d'affaires total : {total:.2f} €")

    def _low_stock(self):
        low = self.storage.low_stock()
        if not low:
            self._write("✅ Tous les produits ont un stock suffisant.")
            return
        lines = ["⚠ Produits avec stock faible (≤ 5) :\n"]
        for p in low:
            lines.append(f"   • {p.name} (réf: {p.reference}) — {p.quantity} unité(s)")
        self._write("\n".join(lines))
