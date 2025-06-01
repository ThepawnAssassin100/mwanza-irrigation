import streamlit as st
from supabase import create_client, Client
import datetime

st.set_page_config(page_title="Mwanza Irrigation Data Tool", layout="centered")

# Supabase credentials
url = "https://iblpdptgmrrejgkfevuv.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlibHBkcHRnbXJyZWpna2ZldnV2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDg3Nzk5OTMsImV4cCI6MjA2NDM1NTk5M30.EaHt6eLtIA6eVph7oZxiwm4jMMhWyXBfA4br4IbyKbQ"

supabase: Client = create_client(url, key)

st.title("🌿 Mwanza Irrigation Data Collection Tool")

with st.form("irrigation_form"):
    epa = st.text_input("EPA Name")
    scheme = st.text_input("Scheme Name")
    date = st.date_input("Visit Date", datetime.date.today())
    male = st.number_input("Male", 0)
    female = st.number_input("Female", 0)
    area = st.number_input("Developed Area (ha)", 0.0)

    submit = st.form_submit_button("Submit Data")

    if submit:
        data = {
            "epa_name": epa,
            "scheme_name": scheme,
            "visit_date": str(date),
            "male": male,
            "female": female,
            "area_ha": area
        }
        try:
            supabase.table("irrigation_data").insert(data).execute()
            st.success("✅ Data saved successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
