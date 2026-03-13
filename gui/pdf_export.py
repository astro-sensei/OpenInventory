from fpdf import FPDF
from datetime import datetime
import os

class PDFExporter:
    @staticmethod
    def export_inventory(products, filepath="exports/inventaire.pdf"):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, "Rapport d'inventaire", ln=True, align="C")
        pdf.set_font("Helvetica", "", 9)
        pdf.cell(0, 8, f"Genere le {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True, align="C")
        pdf.ln(5)

        pdf.set_font("Helvetica", "B", 9)
        headers = ["ID", "Nom", "Categorie", "Prix", "Qte", "Fournisseur", "Seuil"]
        widths = [15, 40, 30, 20, 15, 40, 15]
        for h, w in zip(headers, widths):
            pdf.cell(w, 8, h, border=1, align="C")
        pdf.ln()

        pdf.set_font("Helvetica", "", 8)
        for p in products:
            vals = [str(p.id), p.name[:20], p.category[:15],
                    f"{p.price:.2f}", str(p.quantity),
                    p.supplier[:20], str(p.alert_threshold)]
            for v, w in zip(vals, widths):
                pdf.cell(w, 7, v, border=1, align="C")
            pdf.ln()

        pdf.output(filepath)
        return filepath

    @staticmethod
    def export_sales(sales, filepath="exports/ventes.pdf"):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, "Rapport des ventes", ln=True, align="C")
        pdf.set_font("Helvetica", "", 9)
        pdf.cell(0, 8, f"Genere le {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True, align="C")
        pdf.ln(5)

        pdf.set_font("Helvetica", "B", 9)
        headers = ["Date", "Produit", "Qte", "PU", "Total"]
        widths = [40, 45, 20, 25, 25]
        for h, w in zip(headers, widths):
            pdf.cell(w, 8, h, border=1, align="C")
        pdf.ln()

        pdf.set_font("Helvetica", "", 8)
        grand_total = 0
        for s in sales:
            vals = [s.date[:16], s.product_name[:22], str(s.quantity),
                    f"{s.unit_price:.2f}", f"{s.total:.2f}"]
            for v, w in zip(vals, widths):
                pdf.cell(w, 7, v, border=1, align="C")
            pdf.ln()
            grand_total += s.total

        pdf.set_font("Helvetica", "B", 9)
        pdf.cell(sum(widths[:4]), 8, "TOTAL", border=1, align="R")
        pdf.cell(widths[4], 8, f"{grand_total:.2f}", border=1, align="C")

        pdf.output(filepath)
        return filepath
