from fpdf import FPDF
from .schemas import Quote

def generate_pdf(quote: Quote) -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Quote ID: {quote.id}", ln=True)
    pdf.cell(200, 10, txt=f"Description: {quote.description}", ln=True)
    pdf.cell(200, 10, txt=f"Price: {quote.price}", ln=True)
    pdf.cell(200, 10, txt=f"Created at: {quote.created_at}", ln=True)
    pdf_output = f'quote_{quote.id}.pdf'
    pdf.output(pdf_output)
    return pdf_output
