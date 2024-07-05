import pandas as df
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
csv = df.read_csv("topics.csv")


def line_creator(min, max):
    while min < max:
        pdf.line(10, min, 200, min)
        min = min + 10

for index, row in csv.iterrows():
    pdf.add_page()
    # Header
    pdf.set_font(family="helvetica", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=24, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.set_text_color(0, 0, 0)

    # Lines
    line_creator(42,270)
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        line_creator(30, 260)
        pdf.ln(240)
        pdf.set_font(family="helvetica",  size=12)
        pdf.cell(w=0, h=24, txt=row["Topic"], align="R", ln=1, border=0)



pdf.output("names.pdf")



