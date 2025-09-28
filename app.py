import streamlit as st
import pandas as pd
import dashboard_summary
from utils import load_excel_data, preprocess_booking_value, convert_to_datetime, calculate_total_revenue
import config

def main():
    # Load and preprocess data
    df = load_excel_data("data/OLA RIDES DATASET USED.xlsx", "OLA RIDES DATASET USED")
    if df is None:
        st.error("Failed to load data!")
        st.stop()

    # Convert 'Booking_Value' to numeric, coerces errors to NaN
    df['Booking_Value'] = pd.to_numeric(df['Booking_Value'], errors='coerce')

    # Drop rows where 'Booking_Value' is NaN after conversion
    df = df.dropna(subset=['Booking_Value'])

    # Further preprocessing
    df = preprocess_booking_value(df)
    df = convert_to_datetime(df)

    # Debug print to verify data types
    st.write(df['Booking_Value'].apply(type).value_counts())

    total_revenue = calculate_total_revenue(df)

    st.title("Ola Rides Dashboard")
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.selectbox("Choose a page", ["Dashboard Summary"])

    st.write("""
        Welcome to the Ola Rides data analytics dashboard!  
        Use the sidebar to navigate through different sections:
        - Dashboard Summary
    """)

    st.image("images/images.png")
    st.markdown("---")
    st.write("Project by: Manvi Jain")

    if selected_page == "Dashboard Summary":
        dashboard_summary.dashboard_summary(df)

if __name__ == "__main__":
    main()

