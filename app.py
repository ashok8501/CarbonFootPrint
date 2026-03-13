import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Carbon Footprint Calculator", page_icon="🌍", layout="centered")

# ---------- BACKGROUND + UI STYLING ----------
st.markdown("""
<style>

.stApp{
background: linear-gradient(to right, #d4fc79, #96e6a1);
}

.block-container{
background-color: rgba(255,255,255,0.90);
padding: 2rem;
border-radius: 15px;
}

h1{
color:#0B6623;
text-align:center;
font-size:45px;
}

h2{
color:#145A32;
}

h3{
color:#145A32;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🌍 Carbon Footprint Calculator")
st.write("Measure your environmental impact and learn how to live more sustainably.")

st.header("Enter Your Lifestyle Details")

# ---------- USER INPUT ----------
transport_km = st.number_input("🚗 Distance traveled per day (km)", min_value=0.0)

electricity_units = st.number_input("⚡ Electricity used per month (kWh)", min_value=0.0)

meat_meals = st.number_input("🍖 Meat meals per week", min_value=0)

# ---------- EMISSION FACTORS ----------
transport_factor = 0.21
electricity_factor = 0.82
food_factor = 2.5

# ---------- CALCULATIONS ----------
transport_emission = transport_km * transport_factor
electricity_emission = electricity_units * electricity_factor / 30
food_emission = meat_meals * food_factor

total_emission = transport_emission + electricity_emission + food_emission

# ---------- RESULT ----------
st.header("Your Carbon Footprint")

st.success(f"Your estimated **daily carbon footprint is {total_emission:.2f} kg CO₂**")

# ---------- SUSTAINABILITY SCORE ----------
if total_emission < 5:
    score = 90
    status = "🌱 Sustainable Lifestyle"
elif total_emission < 10:
    score = 60
    status = "⚠ Moderate Impact"
else:
    score = 30
    status = "🚨 High Carbon Lifestyle"

st.subheader("Sustainability Score")

st.write(f"Score: **{score}/100**")
st.write(status)

# ---------- CHART ----------
st.header("Carbon Emission Breakdown")

data = {
"Category":["Transport","Electricity","Food"],
"Emission":[transport_emission,electricity_emission,food_emission]
}

fig = px.pie(data,names="Category",values="Emission",title="Emission Distribution")

st.plotly_chart(fig)

# ---------- GLOBAL COMPARISON ----------
st.header("Global Comparison")

india_avg = 1.9
world_avg = 4.5

st.write(f"Your footprint: **{total_emission:.2f} kg/day**")
st.write(f"Average Indian footprint: **{india_avg} kg/day**")
st.write(f"Global average footprint: **{world_avg} kg/day**")

# ---------- SUGGESTIONS ----------
st.header("Suggestions to Reduce Carbon Footprint")

if transport_emission > 2:
    st.write("🚲 Use public transport, cycling or carpooling.")

if electricity_emission > 2:
    st.write("💡 Use LED lights and energy-efficient appliances.")

if food_emission > 5:
    st.write("🥗 Reduce meat consumption and minimize food waste.")

if total_emission < 5:
    st.success("Great job! Your lifestyle is environmentally friendly.")

# ---------- SDG CONNECTION ----------
st.header("Sustainable Development Goals")

st.write("This project contributes to:")

st.write("🌱 **SDG 7 – Affordable and Clean Energy**")
st.write("🏙 **SDG 11 – Sustainable Cities and Communities**")
st.write("♻ **SDG 12 – Responsible Consumption and Production**")
st.write("🌍 **SDG 13 – Climate Action**")

# ---------- CARBON OFFSET ----------
st.header("Carbon Offset Suggestion")

trees_needed = total_emission / 21

st.write(f"To offset this carbon footprint, you could plant approximately **{trees_needed:.1f} trees per year**.")

st.info("One tree absorbs around **21 kg CO₂ per year**.")