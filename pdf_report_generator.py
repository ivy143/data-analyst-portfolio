import pandas as pd
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet


# ---------------------------
# Load Data
# ---------------------------
def load_data(file_path):
    return pd.read_csv(file_path)


# ---------------------------
# Generate Metrics
# ---------------------------
def generate_metrics(df):
    return {
        "total_salary": df["salary"].sum(),
        "average_salary": df["salary"].mean(),
        "highest_salary": df["salary"].max(),
        "lowest_salary": df["salary"].min(),
        "department_salary": df.groupby("department")["salary"].sum()
    }


# ---------------------------
# Create PDF Report
# ---------------------------
def create_pdf_report(metrics, output_file):
    doc = SimpleDocTemplate(output_file)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    normal_style = styles["Normal"]

    elements.append(Paragraph("EMPLOYEE SALARY REPORT", title_style))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"Report Generated On: {datetime.now()}", normal_style))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"Total Salary Expense: {metrics['total_salary']}", normal_style))
    elements.append(Paragraph(f"Average Salary: {metrics['average_salary']:.2f}", normal_style))
    elements.append(Paragraph(f"Highest Salary: {metrics['highest_salary']}", normal_style))
    elements.append(Paragraph(f"Lowest Salary: {metrics['lowest_salary']}", normal_style))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("Department Wise Salary Distribution:", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    for dept, salary in metrics["department_salary"].items():
        elements.append(Paragraph(f"{dept}: {salary}", normal_style))

    doc.build(elements)


# ---------------------------
# Main
# ---------------------------
def main():
    input_file = "cleaned_employee_data.csv"
    output_file = "salary_report.pdf"

    print("Generating Professional PDF Report...\n")

    df = load_data(input_file)
    metrics = generate_metrics(df)
    create_pdf_report(metrics, output_file)

    print("PDF Report Generated Successfully!")
    print(f"Saved as: {output_file}")


if __name__ == "__main__":
    main()