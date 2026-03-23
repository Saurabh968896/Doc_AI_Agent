from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

file_path = "data/test_doc.pdf"

c = canvas.Canvas(file_path, pagesize=letter)

text = c.beginText(50, 700)

lines = [
    "Artificial Intelligence is transforming industries.",
    "Machine learning is a subset of AI.",
    "Python is widely used in data science.",
    "Deep learning is a powerful technique used in AI.",
]

for line in lines:
    text.textLine(line)

c.drawText(text)
c.save()

print("PDF created at:", file_path)