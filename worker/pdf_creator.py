from fpdf import FPDF


def create_pdf_from_quote(quote_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for key, value in quote_data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)
    pdf_output = f'quote_{quote_data["id"]}.pdf'
    pdf.output(pdf_output)
    return pdf_output
