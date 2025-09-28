import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Excel dataset
excel_file_path = r"C:\Users\pc\Desktop\MANVI LABMENTIX\OLA RIDES DATASET USED.xlsx"
df = pd.read_excel(excel_file_path, sheet_name='OLA RIDES DATASET USED')

st.title("Ratings Analysis - Detailed")

# Convert columns to numeric
df['Driver_Ratings'] = pd.to_numeric(df['Driver_Ratings'], errors='coerce')
df['Customer_Rating'] = pd.to_numeric(df['Customer_Rating'], errors='coerce')

# Show unique values and counts for Driver Ratings
st.subheader("Driver Ratings - Unique Values and Counts")
st.write(df['Driver_Ratings'].value_counts().sort_index())

# Show unique values and counts for Customer Ratings
st.subheader("Customer Ratings - Unique Values and Counts")
st.write(df['Customer_Rating'].value_counts().sort_index())

# Group customer ratings by rounding to nearest 0.5 for pie chart readability
st.header("Customer Rating Distribution (Rounded)")
df['Customer_Rating_Rounded'] = df['Customer_Rating'].round(1)
rating_counts = df['Customer_Rating_Rounded'].value_counts().sort_index()

fig2, ax2 = plt.subplots()
ax2.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax2.axis('equal')
st.pyplot(fig2)

# Median Driver Ratings by Vehicle Type (horizontal bar)
st.header("Median Driver Ratings by Vehicle Type")
median_driver_ratings = df.groupby('Vehicle_Type')['Driver_Ratings'].median().sort_values()

fig, ax = plt.subplots()
median_driver_ratings.plot(kind='barh', ax=ax, color='steelblue')
ax.set_xlabel('Median Driver Rating')
st.pyplot(fig)

# Show raw data option
if st.checkbox("Show Raw Data"):
    st.write(df[['Vehicle_Type', 'Driver_Ratings', 'Customer_Rating']].head(50))
