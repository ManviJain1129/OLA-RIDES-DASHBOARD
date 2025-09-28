import streamlit as st
import pandas as pd

# Load Excel dataset
excel_file_path = "data/OLA RIDES DATASET USED.xlsx"
df = pd.read_excel(excel_file_path, sheet_name='OLA RIDES DATASET USED')

st.title("Overall Ola Ride Insights")

# Convert date columns to datetime (using 'Date_backup' based on your data)
df['Date_backup'] = pd.to_datetime(df['Date_backup'], errors='coerce')

# Ride Volume Over Time
st.header("Ride Volume Over Time")
# Count rides per day based on Date_backup
ride_volume = df.groupby('Date_backup').size().reset_index(name='Ride_Count')
st.line_chart(ride_volume.rename(columns={'Date_backup': 'index'}).set_index('index'))

# Booking Status Breakdown
st.header("Booking Status Breakdown")
booking_status_counts = df['Booking_Status'].value_counts()
st.bar_chart(booking_status_counts)

# Show sample data option
if st.checkbox("Show Raw Data"):
    st.write(df.head(50))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Excel dataset
excel_file_path = "data/OLA RIDES DATASET USED.xlsx"
df = pd.read_excel(excel_file_path, sheet_name='OLA RIDES DATASET USED')

st.title("Overall Ola Ride Insights")

# Convert columns for clean analysis
df['Date_backup'] = pd.to_datetime(df['Date_backup'], errors='coerce')
df['Booking_Value'] = pd.to_numeric(df['Booking_Value'], errors='coerce')

# KPIs: Total rides and total revenue
total_rides = df.shape[0]
total_revenue = df['Booking_Value'].sum()

col1, col2 = st.columns(2)
col1.metric("Total Rides", str(total_rides))
col2.metric("Total Booking Value", f"₹{total_revenue:,.0f}")

# Monthly trends for revenue and rides
df['Month'] = df['Date_backup'].dt.to_period('M')
monthly_stats = df.groupby('Month').agg({'Booking_Value':'sum', 'Booking_ID':'count'}).reset_index()
monthly_stats['Month'] = monthly_stats['Month'].dt.to_timestamp()

st.subheader("Monthly Trends: Revenue & Rides")
st.line_chart(monthly_stats.set_index('Month')[['Booking_Value', 'Booking_ID']])

# Pie chart for Booking Status Breakdown
st.subheader("Booking Status Breakdown")
status_counts = df['Booking_Status'].value_counts()
fig, ax = plt.subplots()
ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Date filter
st.subheader("Filter Data by Date Range")
start_date = st.date_input("Start Date", df['Date_backup'].min().date())
end_date = st.date_input("End Date", df['Date_backup'].max().date())
filtered_df = df[
    (df['Date_backup'] >= pd.to_datetime(start_date)) &
    (df['Date_backup'] <= pd.to_datetime(end_date))
]

st.write(f"Showing data from {start_date} to {end_date}")
st.dataframe(filtered_df.head(50))



