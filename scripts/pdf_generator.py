# pdf_generator.py
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Automatic Report", ln=1)
pdf.output("report.pdf")
