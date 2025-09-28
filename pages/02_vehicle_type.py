import streamlit as st
import pandas as pd

# Load Excel dataset
excel_file_path = r"C:\Users\pc\Desktop\MANVI LABMENTIX\OLA RIDES DATASET USED.xlsx"
df = pd.read_excel(excel_file_path, sheet_name='OLA RIDES DATASET USED')

st.title("Vehicle Type Insights")

# Top 5 Vehicle Types by Total Ride Distance
st.header("Top 5 Vehicle Types by Total Ride Distance")
vehicle_distance = df.groupby('Vehicle_Type')['Ride_Distance'].sum().sort_values(ascending=False).head(5)
st.bar_chart(vehicle_distance)

# Average Customer Rating per Vehicle Type
st.header("Average Customer Rating per Vehicle Type")
# Convert Customer_Rating to numeric, handle errors
df['Customer_Rating'] = pd.to_numeric(df['Customer_Rating'], errors='coerce')
vehicle_ratings = df.groupby('Vehicle_Type')['Customer_Rating'].mean().sort_values(ascending=False)
st.bar_chart(vehicle_ratings)

# Optionally show raw data
if st.checkbox("Show Raw Data"):
    st.write(df[['Vehicle_Type', 'Ride_Distance', 'Customer_Rating']].head(50))
