import streamlit as st
from supabase import create_client, Client
import datetime

st.set_page_config(page_title="Mwanza Irrigation Data Collection Tool", layout="centered")

st.title("🌿 Mwanza Irrigation Data Collection Tool")

# Connect to Supabase using secrets stored on Streamlit Cloud
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]

supabase: Client = create_client(url, key)

def submit_data(data):
    response = supabase.table("irrigation_data").insert(data).execute()
    if response.error:
        st.error(f"Error: {response.error.message}")
    else:
        st.success("✅ Data submitted successfully!")

with st.form("irrigation_form"):
    st.subheader("🔍 Basic Information")
    epa = st.text_input("EPA Name")
    section = st.text_input("Section")
    visit_date = st.date_input("Date of Visit", datetime.date.today())
    scheme_name = st.text_input("Irrigation Scheme Name")
    gps_e = st.text_input("GPS Easting")
    gps_n = st.text_input("GPS Northing")
    project_name = st.text_input("Project Name")
    financial_year = st.text_input("Financial Year")
    quarter = st.selectbox("Quarter", ["Q1", "Q2", "Q3", "Q4"])
    month = st.text_input("Month")

    st.subheader("👥 Beneficiaries")
    male = st.number_input("Male", min_value=0, step=1)
    female = st.number_input("Female", min_value=0, step=1)
    total = male + female

    st.subheader("📏 Irrigation Area")
    potential = st.number_input("Potential Area (Ha)", step=0.1)
    developed = st.number_input("Developed Area (Ha)", step=0.1)
    actual = st.number_input("Actual Area under Irrigation (Ha)", step=0.1)
    newly = st.number_input("Newly Developed Area (Ha)", step=0.1)

    st.subheader("💧 Water Sources")
    water_sources = st.multiselect("Select Water Sources", ["Dam", "Stream", "Shallow Well", "Deep Well", "Borehole"])

    st.subheader("🚜 Irrigation Systems Used")
    systems = st.multiselect("Select Irrigation Systems", ["Watering cans/buckets", "Motorized pumps", "Solar Pumps", "River diversion", "Treadle Pumps"])

    st.subheader("🌾 Cropping Area")
    area_1 = st.number_input("Area under 1 Cropping Cycle (Ha)", step=0.1)
    area_2 = st.number_input("Area under 2 Cropping Cycles (Ha)", step=0.1)
    area_3 = st.number_input("Area under 3 Cropping Cycles (Ha)", step=0.1)
    area_4 = st.number_input("Area under 4 Cropping Cycles (Ha)", step=0.1)

    st.subheader("⚠️ Challenges & Solutions")
    challenges = st.text_area("Challenges")
    solutions = st.text_area("Proposed Solutions")

    submitted = st.form_submit_button("Submit Entry")

    if submitted:
        data = {
            "epa_name": epa,
            "section": section,
            "visit_date": visit_date.isoformat(),
            "scheme_name": scheme_name,
            "gps_easting": gps_e,
            "gps_northing": gps_n,
            "project_name": project_name,
            "financial_year": financial_year,
            "quarter": quarter,
            "month": month,
            "male_beneficiaries": male,
            "female_beneficiaries": female,
            "total_beneficiaries": total,
            "potential_area_ha": potential,
            "developed_area_ha": developed,
            "actual_area_ha": actual,
            "new_developed_ha": newly,
            "water_sources": water_sources,
            "irrigation_systems": systems,
            "area_1_cycle": area_1,
            "area_2_cycle": area_2,
            "area_3_cycle": area_3,
            "area_4_cycle": area_4,
            "challenges": challenges,
            "solutions": solutions,
        }
        submit_data(data)