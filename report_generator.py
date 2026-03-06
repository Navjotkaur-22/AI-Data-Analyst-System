from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_report(insights, filename="analysis_report.pdf"):

    c = canvas.Canvas(filename, pagesize=letter)

    y = 750
    c.setFont("Helvetica", 12)

    c.drawString(50, 800, "AI Data Analysis Report")

    for insight in insights:
        c.drawString(50, y, f"- {insight}")
        y -= 20

    c.save()

    return filename