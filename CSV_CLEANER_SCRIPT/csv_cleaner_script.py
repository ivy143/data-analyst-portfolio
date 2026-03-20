import pandas as pd
import re
import logging

# ---------------------------
# Logging Configuration
# ---------------------------
logging.basicConfig(
    filename="cleaning_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------------------
# Email Validation
# ---------------------------
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, str(email)))


# ---------------------------
# Load Data
# ---------------------------
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info("File loaded successfully.")
        return df
    except Exception as e:
        logging.error(f"Error loading file: {e}")
        raise


# ---------------------------
# Clean Data
# ---------------------------
def clean_data(df):
    # Check for required columns
    required_columns = ["email", "age", "salary"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        logging.error(f"Missing required columns: {missing_columns}")
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    original_shape = df.shape

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()
    logging.info(f"Removed {duplicates} duplicate rows.")

    # Handle missing values
    missing_before = df.isnull().sum().sum()
    df = df.fillna({
        "age": 0,
        "salary": 0
    })
    logging.info(f"Handled {missing_before} missing values.")

    # Convert age and salary to numeric
    df["age"] = pd.to_numeric(df["age"], errors="coerce").fillna(0)
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce").fillna(0)

    # Validate emails
    invalid_emails = df[~df["email"].apply(validate_email)]
    logging.info(f"Found {len(invalid_emails)} invalid emails.")

    df.loc[~df["email"].apply(validate_email), "email"] = "invalid@email.com"

    final_shape = df.shape

    summary = {
        "original_rows": original_shape[0],
        "final_rows": final_shape[0],
        "duplicates_removed": duplicates,
        "invalid_emails_corrected": len(invalid_emails)
    }

    return df, summary


# ---------------------------
# Save Cleaned Data
# ---------------------------
def save_data(df, output_file):
    df.to_csv(output_file, index=False)
    logging.info("Cleaned file saved successfully.")


# ---------------------------
# Main Automation Function
# ---------------------------
def main():
    input_file = "raw_employee_data.csv"
    output_file = "cleaned_employee_data.csv"

    print("Starting Automated Data Cleaning Process...\n")

    df = load_data(input_file)
    cleaned_df, summary = clean_data(df)
    save_data(cleaned_df, output_file)

    print("Cleaning Completed Successfully!\n")
    print("Summary Report:")
    print("-" * 30)
    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
