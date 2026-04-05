import streamlit as st
import plotly.express as px

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Advanced Carbon Footprint Calculator",
    page_icon="🌍",
    layout="wide"
)

# ---------- STYLING ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #d4fc79, #96e6a1);
}
.block-container {
    background-color: rgba(255,255,255,0.92);
    padding: 2rem;
    border-radius: 15px;
}
h1, h2, h3 {
    color:#145A32;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🌍 Advanced Carbon Footprint Calculator")
st.write("A detailed personal carbon tracker with realistic lifestyle inputs.")

# ---------- USER TYPE ----------
st.sidebar.header("👤 Profile")
user_type = st.sidebar.selectbox(
    "Select your profile",
    ["Student", "Working Professional", "Family"]
)

# ---------- TIME MODE ----------
time_mode = st.sidebar.radio("Select calculation mode", ["Daily", "Monthly", "Yearly"])

multiplier = 1
if time_mode == "Monthly":
    multiplier = 30
elif time_mode == "Yearly":
    multiplier = 365

# =========================================================
# 🚗 TRANSPORT
# =========================================================
st.header("🚗 Transport")

car_km = st.number_input("Car travel (km/day)", 0.0)
bike_km = st.number_input("Bike travel (km/day)", 0.0)
bus_km = st.number_input("Bus travel (km/day)", 0.0)
train_km = st.number_input("Train travel (km/day)", 0.0)

car_factor = 0.21
bike_factor = 0.1
bus_factor = 0.05
train_factor = 0.04

transport_emission = (
    car_km * car_factor +
    bike_km * bike_factor +
    bus_km * bus_factor +
    train_km * train_factor
)

# =========================================================
# ⚡ ELECTRICITY
# =========================================================
st.header("⚡ Electricity")

ac_hours = st.number_input("AC usage (hours/day)", 0.0)
fan_hours = st.number_input("Fan usage (hours/day)", 0.0)
tv_hours = st.number_input("TV usage (hours/day)", 0.0)
fridge = st.selectbox("Refrigerator usage", ["Yes", "No"])

ac_emission = ac_hours * 1.5
fan_emission = fan_hours * 0.05
tv_emission = tv_hours * 0.08
fridge_emission = 1.0 if fridge == "Yes" else 0

electricity_emission = ac_emission + fan_emission + tv_emission + fridge_emission

# =========================================================
# 🍽 FOOD
# =========================================================
st.header("🍽 Food Consumption")

veg_meals = st.number_input("Veg meals/week", 0)
chicken_meals = st.number_input("Chicken meals/week", 0)
mutton_meals = st.number_input("Mutton/Beef meals/week", 0)
dairy = st.number_input("Dairy (litres/week)", 0.0)

veg_factor = 1.0
chicken_factor = 3.0
mutton_factor = 7.0
dairy_factor = 1.9

food_emission = (
    veg_meals * veg_factor +
    chicken_meals * chicken_factor +
    mutton_meals * mutton_factor +
    dairy * dairy_factor
) / 7

# =========================================================
# 🗑 WASTE
# =========================================================
st.header("🗑 Waste")

waste = st.number_input("Waste generated (kg/day)", 0.0)
recycle = st.selectbox("Do you recycle?", ["Yes", "No"])

waste_factor = 0.5
recycle_bonus = -0.2 if recycle == "Yes" else 0

waste_emission = waste * waste_factor + recycle_bonus

# =========================================================
# ✈ TRAVEL
# =========================================================
st.header("✈ Air Travel")

flights = st.number_input("Flights per year", 0)

flight_emission = (flights * 90) / 365

# =========================================================
# 📊 TOTAL
# =========================================================
total_emission = (
    transport_emission +
    electricity_emission +
    food_emission +
    waste_emission +
    flight_emission
) * multiplier

# =========================================================
# 🎯 RESULT
# =========================================================
st.header("📊 Your Carbon Footprint")

st.success(f"Estimated {time_mode.lower()} carbon footprint: **{total_emission:.2f} kg CO₂**")

# =========================================================
# 🧠 SCORE
# =========================================================
if total_emission < 5:
    score = 90
    status = "🌱 Excellent Sustainable Lifestyle"
elif total_emission < 10:
    score = 65
    status = "⚠ Moderate Impact"
else:
    score = 35
    status = "🚨 High Carbon Lifestyle"

st.subheader("Sustainability Score")
st.write(f"Score: **{score}/100**")
st.write(status)

# =========================================================
# 📈 CHART
# =========================================================
st.header("📊 Emission Breakdown")

data = {
    "Category": ["Transport", "Electricity", "Food", "Waste", "Flights"],
    "Emission": [
        transport_emission,
        electricity_emission,
        food_emission,
        waste_emission,
        flight_emission
    ]
}

fig = px.pie(data, names="Category", values="Emission", title="Emission Distribution")
st.plotly_chart(fig)

# =========================================================
# 🌍 COMPARISON
# =========================================================
st.header("🌍 Global Comparison")

india_avg = 1.9 * multiplier
world_avg = 4.5 * multiplier

st.write(f"Your footprint: **{total_emission:.2f} kg**")
st.write(f"India average: **{india_avg} kg**")
st.write(f"World average: **{world_avg} kg**")

# =========================================================
# 💡 SMART SUGGESTIONS
# =========================================================
st.header("💡 Smart Suggestions")

if car_km > 20:
    st.write("🚗 Reduce car usage, try carpooling or public transport.")

if electricity_emission > 5:
    st.write("⚡ Switch to energy-efficient appliances.")

if mutton_meals > 3:
    st.write("🥩 Reduce red meat consumption.")

if waste > 2:
    st.write("🗑 Reduce waste and improve recycling habits.")

if total_emission < 5:
    st.success("Great job! You are eco-friendly.")

# =========================================================
# 🌳 CARBON OFFSET
# =========================================================
st.header("🌳 Carbon Offset")

trees_needed = total_emission / 21

st.write(f"You need approx **{trees_needed:.1f} trees/year** to offset emissions.")

# =========================================================
# 📚 INFO
# =========================================================
with st.expander("ℹ About this calculator"):
    st.write("""
    This calculator uses approximate emission factors based on global research.
    It is designed for awareness and lifestyle improvement, not exact scientific measurement.
    """)

# =========================================================
# 🚀 FOOTER
# =========================================================
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")