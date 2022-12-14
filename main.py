from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for page in range(row["Pages"]):
        pdf.add_page()
        if page == 0:
            # Set the header
            pdf.set_font(family="Times", style="B", size=24)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
            pdf.ln(266)
        else:
            pdf.ln(278)

        # Set the footer
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # Create lines for lined paper
        for y in range(21, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")