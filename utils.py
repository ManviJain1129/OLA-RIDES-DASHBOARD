import pandas as pd

def load_excel_data(filepath, sheet_name):
    """
    Loads Excel data into a pandas DataFrame.
    """
    try:
        df = pd.read_excel(filepath, sheet_name=sheet_name)
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

def preprocess_booking_value(df, col_name='Booking_Value'):
    df[col_name] = pd.to_numeric(df[col_name], errors='coerce')  # This converts values to numeric
    return df

def convert_to_datetime(df, col_name='Date_backup'):
    """
    Converts the specified column to datetime format.
    """
    df[col_name] = pd.to_datetime(df[col_name], errors='coerce')
    return df

def calculate_total_revenue(df, col='Booking_Value'):
    """
    Calculate total revenue from a specified column.
    """
    return df[col].sum()
