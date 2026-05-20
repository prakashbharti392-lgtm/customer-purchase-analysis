import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Customer Purchase Analysis Dashboard")

# Data load karo
df = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\Custermors.csv')

# Basic Stats
st.header("Basic Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", len(df))
col2.metric("Total Purchase", f"Rs. {df['Purchase_Amount'].sum():,}")
col3.metric("Avg Purchase", f"Rs. {int(df['Purchase_Amount'].mean())}")

# City wise analysis
st.header("City wise Total Purchase")
city_data = df.groupby('City')['Purchase_Amount'].sum().sort_values(ascending=False)
st.bar_chart(city_data)

# Top 10 customers
st.header("Top 10 Customers")
top10 = df.nlargest(10, 'Purchase_Amount')[['Name', 'City', 'Purchase_Amount']]
st.dataframe(top10)

# Customer Categories
st.header("Customer Categories")
def category(amount):
    if amount >= 4000:
        return 'High Spender'
    elif amount >= 2000:
        return 'Medium Spender'
    else:
        return 'Low Spender'

df['Category'] = df['Purchase_Amount'].apply(category)
st.bar_chart(df['Category'].value_counts())