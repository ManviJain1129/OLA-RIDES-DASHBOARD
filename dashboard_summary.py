import streamlit as st
import pandas as pd


def dashboard_summary(df):
    st.title("Dashboard Summary: Ola Rides Overview")

    # Key Metrics
    st.subheader("Key Metrics")
    total_rides = df.shape[0]
    total_revenue = df['Booking_Value'].sum()
    col1, col2 = st.columns(2)
    col1.metric("Total Rides", total_rides)
    col2.metric("Total Booking Value (₹)", f"{total_revenue:,.0f}")

    # Booking Status breakdown
    st.subheader("Booking Status Breakdown")
    status_counts = df['Booking_Status'].value_counts()
    st.bar_chart(status_counts)

    # Vehicle Type analysis
    st.subheader("Rides by Vehicle Type")
    vehicle_counts = df['Vehicle_Type'].value_counts()
    st.bar_chart(vehicle_counts)

    # Revenue trend over months
    st.subheader("Monthly Revenue Trend")
    df['Month'] = pd.to_datetime(df['Date_backup']).dt.to_period('M')
    monthly_revenue = df.groupby('Month')['Booking_Value'].sum()
    st.line_chart(monthly_revenue)

    # Cancellations overview
    st.subheader("Cancellation Reasons")
    cancel_by_customer = df[df['Booking_Status'] == 'Canceled by Customer'].shape[0]
    cancel_by_driver = df[df['Booking_Status'] == 'Canceled by Driver'].shape[0]
    st.write(f"Total cancellations by customers: {cancel_by_customer}")
    st.write(f"Total cancellations by drivers: {cancel_by_driver}")

    # Ratings overview
    df['Customer_Rating'] = pd.to_numeric(df['Customer_Rating'], errors='coerce')
    avg_ratings = df.groupby('Vehicle_Type')['Customer_Rating'].mean()
    st.bar_chart(avg_ratings)

    
    print("dashboard_summary module loaded")



