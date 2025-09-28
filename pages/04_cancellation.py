import streamlit as st
import pandas as pd

# Load Excel dataset
excel_file_path = r"C:\Users\pc\Desktop\MANVI LABMENTIX\OLA RIDES DATASET USED.xlsx"
df = pd.read_excel(excel_file_path, sheet_name='OLA RIDES DATASET USED')

st.title("Cancellation Analysis")

# Count cancellations by customer reasons
st.header("Cancelled Rides Reasons (Customer)")
cancel_cust = df['Canceled_Rides_by_Customer'].value_counts()
st.bar_chart(cancel_cust)

# Count cancellations by driver reasons
st.header("Cancelled Rides Reasons (Driver)")
cancel_driver = df['Canceled_Rides_by_Driver'].value_counts()
st.bar_chart(cancel_driver)

# Show raw data option
if st.checkbox("Show Raw Data"):
    st.write(df[['Canceled_Rides_by_Customer', 'Canceled_Rides_by_Driver']].head(50))
