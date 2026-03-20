import pandas as pd
from datetime import datetime


# ---------------------------
# Load Cleaned Data
# ---------------------------
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


# ---------------------------
# Generate Report Metrics
# ---------------------------
def generate_metrics(df):
    total_salary = df["salary"].sum()
    average_salary = df["salary"].mean()
    max_salary = df["salary"].max()
    min_salary = df["salary"].min()

    dept_salary = df.groupby("department")["salary"].sum()

    metrics = {
        "total_salary": total_salary,
        "average_salary": average_salary,
        "highest_salary": max_salary,
        "lowest_salary": min_salary,
        "department_salary": dept_salary
    }

    return metrics


# ---------------------------
# Create Text Report
# ---------------------------
def create_report(metrics, output_file):
    with open(output_file, "w") as file:
        file.write("EMPLOYEE SALARY REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Report Generated On: {datetime.now()}\n\n")

        file.write(f"Total Salary Expense: {metrics['total_salary']}\n")
        file.write(f"Average Salary: {metrics['average_salary']:.2f}\n")
        file.write(f"Highest Salary: {metrics['highest_salary']}\n")
        file.write(f"Lowest Salary: {metrics['lowest_salary']}\n\n")

        file.write("Department Wise Salary Distribution:\n")
        file.write("-" * 40 + "\n")

        for dept, salary in metrics["department_salary"].items():
            file.write(f"{dept}: {salary}\n")


# ---------------------------
# Main Function
# ---------------------------
def main():
    input_file = "cleaned_employee_data.csv"
    output_file = "salary_report.txt"

    print("Generating Automated Salary Report...\n")

    df = load_data(input_file)
    metrics = generate_metrics(df)
    create_report(metrics, output_file)

    print("Report Generated Successfully!")
    print(f"Report saved as: {output_file}")


if __name__ == "__main__":
    main()