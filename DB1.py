import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Analysis", layout="wide")

# Title
st.title("🛍️ Customer Purchase Analysis Dashboard")
st.markdown("---")

# Data load karo
df = pd.read_csv('Custermors.csv')

# Basic Stats
st.header("📊 Basic Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", len(df))
col2.metric("Total Purchase", f"Rs. {df['Purchase_Amount'].sum():,}")
col3.metric("Avg Purchase", f"Rs. {int(df['Purchase_Amount'].mean())}")

st.markdown("---")

# City wise analysis
st.header("🏙️ City wise Total Purchase")
city_data = df.groupby('City')['Purchase_Amount'].sum().sort_values(ascending=False)
st.bar_chart(city_data)

st.markdown("---")

# Top 10 customers
st.header("🏆 Top 10 Customers")
top10 = df.nlargest(10, 'Purchase_Amount')
st.dataframe(top10)
st.dataframe(top10, use_container_width=True)

st.markdown("---")

# Customer Categories
st.header("👥 Customer Categories")
def category(amount):
    if amount >= 4000:
        return 'High Spender'
    elif amount >= 2000:
        return 'Medium Spender'
    else:
        return 'Low Spender'

df['Category'] = df['Purchase_Amount'].apply(category)
col1, col2 = st.columns(2)

with col1:
    st.bar_chart(df['Category'].value_counts())

with col2:
    fig, ax = plt.subplots()
    df['Category'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_ylabel('')
    st.pyplot(fig)

st.markdown("---")

# City wise Average
st.header("📈 City wise Average Purchase")
avg_data = df.groupby('City')['Purchase_Amount'].mean().round(2).sort_values(ascending=False)
st.bar_chart(avg_data)

st.markdown("---")
st.success("Project by: Data Science Intern | Tools: Python, Pandas, Matplotlib, Streamlit")