from fpdf import FPDF

name = input('Name: ')
pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(text="CS50 Shirtificate")
pdf.image("shirtificate.png", h=pdf.eph, w=pdf.epw)
pdf.set_font("Times", size=36)
pdf.cell(text=f"{name} took CS50")
pdf.output("shirtificate.pdf")
