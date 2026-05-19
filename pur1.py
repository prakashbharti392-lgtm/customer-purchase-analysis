import pandas as pd

df = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\Custermors.csv')

print("Total Rows aur Columns:", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nPehle 5 rows:")
print(df.head())

# City wise total purchase
print("\nCity wise Total Purchase:")
print(df.groupby('City')['Purchase_Amount'].sum().sort_values(ascending=False))

import matplotlib.pyplot as plt

# City wise bar graph
city_purchase = df.groupby('City')['Purchase_Amount'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
city_purchase.plot(kind='bar', color='skyblue')
plt.title('City wise Total Purchase')
plt.xlabel('City')
plt.ylabel('Purchase Amount')
plt.xticks(rotation=45)
plt.tight_layout()
# City wise average purchase
print("\nCity wise Average Purchase:")
print(df.groupby('City')['Purchase_Amount'].mean().round(2).sort_values(ascending=False))

# Top 10 customers
print("\nTop 10 Customers:")
print(df.nlargest(10, 'Purchase_Amount')[['Name', 'City', 'Purchase_Amount']])
# Top 10 customers graph
top10 = df.nlargest(10, 'Purchase_Amount')

plt.figure(figsize=(10, 5))
plt.barh(top10['Name'], top10['Purchase_Amount'], color='orange')
plt.title('Top 10 Customers by Purchase Amount')
plt.xlabel('Purchase Amount')
plt.tight_layout()
plt.show()
# Customer categories
def category(amount):
    if amount >= 4000:
        return 'High Spender'
    elif amount >= 2000:
        return 'Medium Spender'
    else:
        return 'Low Spender'

df['Category'] = df['Purchase_Amount'].apply(category)

print("\nCustomer Categories:")
print(df['Category'].value_counts())
# Category pie chart
df['Category'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
plt.title('Customer Categories')
plt.ylabel('')
plt.show()