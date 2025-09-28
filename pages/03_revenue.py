import streamlit as st
import pandas as pd

# Load Excel dataset
excel_file_path = r"C:\Users\pc\Desktop\MANVI LABMENTIX\OLA RIDES DATASET USED.xlsx"
df = pd.read_excel(excel_file_path, sheet_name='OLA RIDES DATASET USED')

st.title("Revenue Insights")

# Convert Booking_Value to numeric
df['Booking_Value'] = pd.to_numeric(df['Booking_Value'], errors='coerce')

# Revenue by Payment Method
st.header("Revenue by Payment Method")
payment_revenue = df.groupby('Payment_Method')['Booking_Value'].sum().sort_values(ascending=False)
st.bar_chart(payment_revenue)

# Top 5 Customers by Total Booking Value
st.header("Top 5 Customers by Total Booking Value")
customer_revenue = df.groupby('Customer_ID')['Booking_Value'].sum().sort_values(ascending=False).head(5)
st.bar_chart(customer_revenue)

# Optionally show raw data for bookings
if st.checkbox("Show Raw Data"):
    st.write(df[['Customer_ID', 'Payment_Method', 'Booking_Value']].head(50))
