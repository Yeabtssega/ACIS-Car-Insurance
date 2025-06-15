from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()

# Use default font to avoid font issues
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "ACIS Car Insurance A/B Test Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", "", 12)

summary = (
    "Groups compared:\n"
    "- Group A: Comprehensive - Taxi (N=504,847)\n"
    "- Group B: Third Party Only (N=63)\n\n"
    "Summary Statistics for Total Premium:\n"
    "- Group A mean: 64.67, std: 171.35\n"
    "- Group B mean: 107.51, std: 24.90\n\n"
    "T-test Results:\n"
    "- t-statistic = -13.6175\n"
    "- p-value = 0.0000\n\n"
    "Interpretation:\n"
    "Statistically significant difference between the groups (reject null hypothesis)."
)

pdf.multi_cell(0, 10, summary)
pdf.ln(10)

# Insert images if available
images = ["boxplot_total_premium.png", "histogram_total_premium.png"]
for img in images:
    if os.path.exists(img):
        pdf.image(img, w=180)
        pdf.ln(10)
    else:
        pdf.cell(0, 10, f"[Missing image: {img}]", ln=True)

pdf.output("ACIS_AB_Test_Report_Simple.pdf")
print("Simple report generated: ACIS_AB_Test_Report_Simple.pdf")
