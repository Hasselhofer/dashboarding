import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Salmon Site Dashboard", layout="wide")
st.title("📍 Site A Summary Dashboard")

df = pd.read_csv("data/site_a_summary.csv", parse_dates=["Date", "Next Feed Date", "Next Harvest Date"])

# Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Mobile Lice", f"{df['Avg Lice Count (Mobile)'].iloc[-1]:.2f}")
col2.metric("Avg Adult Lice", f"{df['Avg Lice Count (Adult)'].iloc[-1]:.2f}")
col3.metric("Wound Rate", f"{df['Wounds (%)'].iloc[-1]:.1f}%")
col4.metric("Biomass", f"{df['Biomass (tonnes)'].iloc[-1]:.0f} t")

st.markdown("### Biomass Over Time")
fig, ax = plt.subplots()
ax.plot(df["Date"], df["Biomass (tonnes)"], marker='o')
ax.axhline(500, color='red', linestyle='--', label='Regulatory Limit')
ax.set_ylabel("Biomass (tonnes)")
ax.set_xlabel("Date")
ax.legend()
st.pyplot(fig)

st.markdown("### Next Feed & Harvest")
st.write("📅 **Next Feed:**", df["Next Feed Date"].iloc[0].strftime("%Y-%m-%d"))
st.write("📅 **Next Harvest:**", df["Next Harvest Date"].iloc[0].strftime("%Y-%m-%d"))
