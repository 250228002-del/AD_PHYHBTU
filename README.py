import streamlit as st

st.set_page_config(
    page_title="Unit Converter",
    page_icon="⭐",
    layout="wide"
)

# -----------------------------
# CSS - App Design
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: #ffffff;
    }

    .topbar {
        background: linear-gradient(135deg, #3159b7, #294fa9);
        padding: 5px;
        margin: -10px -10px 35px -10px;
        text-align: center;
        color: white;
        font-size: 40px;
        font-weight: 400;
    }

    .box {
        border: 2px solid #dce5ff;
        border-radius: 2px;
        padding: 5px;
        margin: 5px 0;
        background: #ffffff;
    }

    .heading {
        color: #3159b7;
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .answer {
        border: 5px solid #d5efdc;
        border-radius: 15px;
        padding: 15px;
        margin-top: 20px;
        background: #f5fff7;
    }

    .answer-title {
        color: #3b9b59;
        font-size: 25px;
        font-weight: 700;
    }

    .result {
        font-size: 30px;
        font-weight: 600;
        padding: 15px;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="topbar">☰ &nbsp;&nbsp;&nbsp; Unit Converter &nbsp;&nbsp;&nbsp; ☆</div>',
    unsafe_allow_html=True
)


# -----------------------------
# 1. Convert in
# -----------------------------
st.markdown(
    '<div class="box"><div class="heading">1. Convert in</div>',
    unsafe_allow_html=True
)

system = st.selectbox(
    "Conversion System",
    ["SI", "CGS"],
    label_visibility="collapsed"
)

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# 2. Physical Quantity
# -----------------------------
st.markdown(
    '<div class="box"><div class="heading">2. Physical Quantity</div>',
    unsafe_allow_html=True
)

quantity = st.selectbox(
    "Physical Quantity",
    [
        "Force",
        "Energy",
        "Power",
        "Pressure",
        "Length",
        "Mass",
        "Time",
        "Magnetic induction",
        "Magnetic field",
        "Magnetization",
        "Magnetic polarization",
        "Magnetic moment",
        "Magnetic moment per unit mass",
        "Volume magnetic susceptibility",
        "Mass magnetic susceptibility",
        "Molar magnetic susceptibility",
        "Magnetic permeability",
        "Magnetic flux",
        "Magnetic scalar potential;Magnetive force",
        "Magnetic vector potential",
        "Magnetic pole strength",
        "Demagnetizing factor",
        "Magnetostriction constant",
        "Anisotropy constant",
        "Magnetostatic energy",
        "Energy product",
    ],
    label_visibility="collapsed"
)

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# Units
# -----------------------------
units = {
    "Force": {
        "SI": ["Newton (N)", "Kilonewton (kN)"],
        "CGS": ["dyne (dyn)", "Kilodyne (kdyn)"]
    },

    "Energy": {
        "SI": ["Joule (J)", "Kilojoule (kJ)"],
        "CGS": ["erg", "Kilerg"]
    },

    "Power": {
        "SI": ["Watt (W)", "Kilowatt (kW)"],
        "CGS": ["erg/second", "Kilerg/second"]
    },

    "Pressure": {
        "SI": ["Pascal (Pa)", "Kilopascal (kPa)"],
        "CGS": ["Barye (Ba)", "Kilobarye (kBa)"]
    },

    "Length": {
        "SI": ["Meter (m)", "Kilometer (km)", "Centimeter (cm)"],
        "CGS": ["Centimeter (cm)", "Millimeter (mm)"]
    },

    "Mass": {
        "SI": ["Kilogram (kg)", "Gram (g)"],
        "CGS": ["Gram (g)", "Milligram (mg)"]
    },

    "Time": {
        "SI": ["Second (s)", "Minute (min)", "Hour (h)"],
        "CGS": ["Second (s)", "Minute (min)", "Hour (h)"]
    }
}


# -----------------------------
# 3. Enter Value
# -----------------------------
st.markdown(
    '<div class="box"><div class="heading">3. Enter value</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    value = st.number_input(
        "Value",
        value=50.0,
        label_visibility="collapsed"
    )

with col2:
    unit_list = units[quantity][system]

    selected_unit = st.selectbox(
        "Unit",
        unit_list,
        label_visibility="collapsed"
    )

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# Conversion Logic
# -----------------------------

def convert_force(value, unit):
    if unit == "Newton (N)":
        return value * 100000, "dyne (dyn)"
    elif unit == "Kilonewton (kN)":
        return value * 100000000, "dyne (dyn)"
    elif unit == "dyne (dyn)":
        return value / 100000, "Newton (N)"
    elif unit == "Kilodyne (kdyn)":
        return value * 10000, "Newton (N)"


def convert_energy(value, unit):
    if unit == "Joule (J)":
        return value * 10000000, "erg"
    elif unit == "Kilojoule (kJ)":
        return value * 10000000000, "erg"
    elif unit == "erg":
        return value / 10000000, "Joule (J)"
    elif unit == "Kilerg":
        return value / 1000, "Joule (J)"


def convert_power(value, unit):
    if unit == "Watt (W)":
        return value * 10000000, "erg/second"
    elif unit == "Kilowatt (kW)":
        return value * 10000000000, "erg/second"
    elif unit == "erg/second":
        return value / 10000000, "Watt (W)"
    elif unit == "Kilerg/second":
        return value / 1000, "Watt (W)"


def convert_pressure(value, unit):
    if unit == "Pascal (Pa)":
        return value * 10, "Barye (Ba)"
    elif unit == "Kilopascal (kPa)":
        return value * 10000, "Barye (Ba)"
    elif unit == "Barye (Ba)":
        return value / 10, "Pascal (Pa)"
    elif unit == "Kilobarye (kBa)":
        return value * 100000, "Pascal (Pa)"


def convert_length(value, unit):
    if unit == "Meter (m)":
        return value * 100, "Centimeter (cm)"
    elif unit == "Kilometer (km)":
        return value * 100000, "Centimeter (cm)"
    elif unit == "Centimeter (cm)":
        return value / 100, "Meter (m)"
    elif unit == "Millimeter (mm)":
        return value / 1000, "Meter (m)"


def convert_mass(value, unit):
    if unit == "Kilogram (kg)":
        return value * 1000, "Gram (g)"
    elif unit == "Gram (g)":
        return value / 1000, "Kilogram (kg)"
    elif unit == "Milligram (mg)":
        return value / 1000000, "Kilogram (kg)"


def convert_time(value, unit):
    if unit == "Second (s)":
        return value / 60, "Minute (min)"
    elif unit == "Minute (min)":
        return value * 60, "Second (s)"
    elif unit == "Hour (h)":
        return value * 3600, "Second (s)"


if quantity == "Force":
    result, result_unit = convert_force(value, selected_unit)

elif quantity == "Energy":
    result, result_unit = convert_energy(value, selected_unit)

elif quantity == "Power":
    result, result_unit = convert_power(value, selected_unit)

elif quantity == "Pressure":
    result, result_unit = convert_pressure(value, selected_unit)

elif quantity == "Length":
    result, result_unit = convert_length(value, selected_unit)

elif quantity == "Mass":
    result, result_unit = convert_mass(value, selected_unit)

elif quantity == "Time":
    result, result_unit = convert_time(value, selected_unit)


# -----------------------------
# 4. Answer
# -----------------------------
st.markdown(
    '<div class="answer"><div class="answer-title">4. Your answer</div>',
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="result">
        {result:,.6g} &nbsp;&nbsp; {result_unit}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
