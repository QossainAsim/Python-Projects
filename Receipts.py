from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import csv


def load_file(file_name):
    if file_name.endswith(".csv"):
        with open(file_name, newline="") as f:
            reader = csv.reader(f)
            data = [row for row in reader]
        return data
    else:
        data = []
        with open(file_name) as f:
            for line in f:
                data.append(line.strip().split(","))
        return data


def receipt_table_style():
    return TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ]
    )


custom_size = (80*mm, 200*mm)
pdf = SimpleDocTemplate("receipts.pdf", pagesize= A4)

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
title_style.alignment = 1

title = Paragraph("One Stop Auto Care Zone", title_style)

style = receipt_table_style()

# load data from file
data = load_file(r"C:\Users\qossa\OneDrive\Desktop\data.txt")  # or "data.txt"
table = Table(data, style=style)

# build pdf
pdf.build([title, table])
