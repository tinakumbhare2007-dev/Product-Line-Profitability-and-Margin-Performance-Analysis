import streamlit as st
import pandas as pd
st.set_page_config(page_title="Nassau Candy Dashboard", layout="wide")
df=pd.read_csv("Nassau Candy Distributor.csv")
sales=df["Sales"].sum(); cost=df["Cost"].sum(); profit=df["Gross Profit"].sum()
margin=(profit/sales)*100
st.title("Product Line Profitability and Margin Performance Analysis")
a,b,c,d=st.columns(4)
a.metric("Total Sales",f"${sales:,.2f}")
b.metric("Total Cost",f"${cost:,.2f}")
c.metric("Total Profit",f"${profit:,.2f}")
d.metric("Profit Margin",f"{margin:.2f}%")
st.subheader("Division-wise Profit")
st.bar_chart(df.groupby("Division")["Gross Profit"].sum())
st.subheader("Top 10 Products by Profit")
st.bar_chart(df.groupby("Product Name")["Gross Profit"].sum().sort_values(ascending=False).head(10))
st.dataframe(df)
