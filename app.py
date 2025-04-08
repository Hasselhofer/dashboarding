import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Salmon Dashboard", layout="wide")

st.title("🐟 Salmon Farm Dashboard")

# Load data
site_df = pd.read_csv("data/site_summary.csv", parse_dates=["Date"])
pen_df = pd.read_csv("data/pen_summary.csv", parse_dates=["Date"])

# Navigation
selected_site = st.selectbox("Select Site", site_df['Site'].unique())

# Site-level chart
st.markdown(f"### 📊 Biomass Over Time – {selected_site}")
site_filtered = site_df[site_df['Site'] == selected_site]
fig, ax = plt.subplots()
ax.plot(site_filtered['Date'], site_filtered['Biomass (tonnes)'], marker='o', label="Biomass")
ax.axhline(500, color='red', linestyle='--', label="Regulatory Limit")
ax.set_ylabel("Biomass (tonnes)")
ax.set_xlabel("Date")
ax.legend()
st.pyplot(fig)

# Expandable list of pens
st.markdown(f"### 🧪 Pen Details for {selected_site}")
pen_filtered = pen_df[pen_df['Site'] == selected_site]
for pen in sorted(pen_filtered['Pen'].unique()):
    with st.expander(f"🔹 {pen}"):
        pen_data = pen_filtered[pen_filtered['Pen'] == pen]
        st.line_chart(pen_data.set_index("Date")[["Avg Weight (kg)", "Avg Lice Count"]])
        st.dataframe(pen_data[["Date", "Avg Weight (kg)", "Avg Lice Count"]].reset_index(drop=True))
