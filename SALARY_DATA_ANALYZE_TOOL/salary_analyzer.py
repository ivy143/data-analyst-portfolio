import pandas as pd
from datetime import datetime


# ---------------------------
# Load Data
# ---------------------------
def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print("Error loading file:", e)
        return None


# ---------------------------
# Basic Salary Statistics
# ---------------------------
def calculate_statistics(df):
    stats = {
        "total_salary": df["salary"].sum(),
        "average_salary": df["salary"].mean(),
        "median_salary": df["salary"].median(),
        "std_deviation": df["salary"].std()
    }
    return stats


# ---------------------------
# Extreme Salary Detection
# ---------------------------
def find_extremes(df):
    highest = df.loc[df["salary"].idxmax()]
    lowest = df.loc[df["salary"].idxmin()]
    return highest, lowest


# ---------------------------
# Department Analysis
# ---------------------------
def department_analysis(df):
    dept_avg = df.groupby("department")["salary"].mean()
    dept_total = df.groupby("department")["salary"].sum()

    total_salary = df["salary"].sum()
    dept_percentage = (dept_total / total_salary) * 100

    return dept_avg, dept_percentage


# ---------------------------
# Save Analysis Report
# ---------------------------
def save_report(stats, highest, lowest, dept_avg, dept_percentage):
    with open("salary_analysis_report.txt", "w") as file:
        file.write("SALARY DATA ANALYSIS REPORT\n")
        file.write("=" * 50 + "\n")
        file.write(f"Generated On: {datetime.now()}\n\n")

        file.write("Overall Statistics:\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total Salary: {stats['total_salary']}\n")
        file.write(f"Average Salary: {stats['average_salary']:.2f}\n")
        file.write(f"Median Salary: {stats['median_salary']}\n")
        file.write(f"Standard Deviation: {stats['std_deviation']:.2f}\n\n")

        file.write("Highest Paid Employee:\n")
        file.write(f"{highest['name']} - {highest['salary']}\n\n")

        file.write("Lowest Paid Employee:\n")
        file.write(f"{lowest['name']} - {lowest['salary']}\n\n")

        file.write("Department Wise Average Salary:\n")
        file.write("-" * 30 + "\n")
        for dept, avg in dept_avg.items():
            file.write(f"{dept}: {avg:.2f}\n")

        file.write("\nDepartment Salary Contribution (%):\n")
        file.write("-" * 30 + "\n")
        for dept, percent in dept_percentage.items():
            file.write(f"{dept}: {percent:.2f}%\n")


# ---------------------------
# Main Function
# ---------------------------
def main():
    input_file = "cleaned_employee_data.csv"

    print("Starting Salary Data Analysis...\n")

    df = load_data(input_file)
    if df is None:
        return

    stats = calculate_statistics(df)
    highest, lowest = find_extremes(df)
    dept_avg, dept_percentage = department_analysis(df)

    save_report(stats, highest, lowest, dept_avg, dept_percentage)

    print("Analysis Completed Successfully!")
    print("Report saved as: salary_analysis_report.txt")


if __name__ == "__main__":
    main()