import streamlit as st
st.set_page_config(
    page_title="Unit Converter",
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
        font-size: 35px;
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
    '<div class="topbar">☰ &nbsp;&nbsp;&nbsp; Unit Converter &nbsp;&nbsp;&nbsp; </div>',
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
    ["CGS", "SI"],
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
        "Force(F)",
        "Energy(E)",
        "Power(P)",
        "Pressure(p)",
        "Length(L)",
        "Mass(M)",
        "Time(T)",
        "Magnetic induction(B)",
        "Magnetic field(H)",
        "Magnetization(M)",
        "Magnetic polarization(J)",
        "Magnetic moment(m)",
        "Magnetic moment per unit mass(σ)",
        "Volume magnetic susceptibility(k=M/H)",
        "Mass magnetic susceptibility(χ=κ/ρ)",
        "Molar magnetic susceptibility(χₘ)",
        "Magnetic permeability(μ=B/H)",
        "Magnetic flux(Φ)",
        "Magnetic scalar potential;Magnetive force(φ)",
        "Magnetic vector potential(A)",
        "Magnetic pole strength(p)",
        "Demagnetizing factor(N)",
        "Magnetostriction constant(λ)",
        "Anisotropy constant(K,K₁,Kᵤ)",
        "Magnetostatic energy(Eₘ)",
        "Energy product((BH)ₘₐₓ)",
    ],
    label_visibility="collapsed"
)

st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------
# Units
# -----------------------------
units = {
    "Force(F)": {
        "CGS": ["Newton (N)"],
        "SI": ["dyne (dyn)"]
    },

    "Energy(E)": {
        "CGS": ["Joule (J)", "Kilojoule (kJ)"],
        "SI": ["erg", "Kilerg"]
    },

    "Power(P)": {
        "CGS": ["Watt (W)", "Kilowatt (kW)"],
        "SI": ["erg/second", "Kilerg/second"]
    },

    "Pressure(p)": {
        "CGS": ["Pascal (Pa)", "Kilopascal (kPa)"],
        "SI": ["Barye (Ba)", "Kilobarye (kBa)"]
    },

    "Length(L)": {
        "CGS": ["Meter (m)", "Kilometer (km)", "Centimeter (cm)"],
        "SI": ["Centimeter (cm)", "Millimeter (mm)"]
    },

    "Mass(T)": {
        "CGS": ["Kilogram (kg)", "Gram (g)"],
        "SI": ["Gram (g)", "Milligram (mg)"]
    },

    "Time(T)": {
        "CGS": ["Second (s)", "Minute (min)", "Hour (h)"],
        "SI": ["Second (s)", "Minute (min)", "Hour (h)"]
    },

    "Magnetic induction(B)": {
        "CGS": ["Gauss (G)"],
        "SI": ["Tesla (T)"]
    },

    "Magnetic field(H)": {
        "CGS": ["A m⁻¹"],
        "SI": ["oersted(Oe)"]
    },   

     "Magnetization(M)": {
        "CGS": ["A m⁻¹"],
        "SI": ["emu cm⁻³"]
    }, 

     "Magnetic polarization(J)": {
        "CGS": ["T"],
        "SI": ["emu cm⁻³"]
    }, 

     "Magnetic moment(m)": {
        "CGS": ["A m²"],
        "SI": ["emu = G cm³"]
    }, 

     "Magnetic moment per unit mass(σ)": {
        "CGS": ["A m² kg⁻¹"],
        "SI": ["emu g⁻¹"]
    }, 

     "Volume magnetic susceptibility(k=M/H)": {
        "CGS": ["dimensionless"],
        "SI": ["dimensionless"]
    }, 

     "Mass magnetic susceptibility(χ=κ/ρ)": {
        "CGS": ["m³ kg⁻¹"],
        "SI": ["emu Oe⁻¹ g⁻¹"]
    }, 

     "Molar magnetic susceptibility(χₘ)": {
        "CGS": ["m³ mol⁻¹"],
        "SI": ["emu Oe⁻¹ g⁻¹ mol⁻¹"]
    }, 

     "Magnetic permeability(μ=B/H)": {
        "CGS": ["H m⁻¹"],
        "SI": ["G Oe⁻¹"]
    }, 

     "Magnetic flux(Φ)": {
        "CGS": ["Weber(Wb)"],
        "SI": ["maxwell(Mx)"]
    }, 

     "Magnetic scalar potential;Magnetive force(φ)": {
        "CGS": ["A"],
        "SI": ["gilbert"]
    }, 

     "Magnetic vector potential(A)": {
        "CGS": ["Wb m⁻¹"],
        "SI": ["emu = G cm"]
    }, 

     "Magnetic pole strength(p)": {
        "CGS": ["A m"],
        "SI": ["emu = G cm²"]
    }, 

     "Demagnetizing factor(N)": {
        "CGS": ["dimensionless"],
        "SI": ["dimensionless"]
    }, 

     "Magnetostriction constant(λ)": {
        "CGS": ["dimensionless"],
        "SI": ["dimensionless"]
    }, 

     "Anisotropy constant(K,K₁,Kᵤ)": {
        "CGS": ["J m⁻³"],
        "SI": ["erg cm⁻³"]
    }, 

     "Magnetostatic energy(Eₘ)": {
        "CGS": ["J m⁻³"],
        "SI": ["erg cm⁻³"]
    }, 

     "Energy product((BH)ₘₐₓ)": {
        "CGS": ["J m⁻³"],
        "SI": ["erg cm⁻³"]
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
    elif unit == "dyne (dyn)":
        return value / 100000, "Newton (N)"
    

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


def convert_magnetic_induction(value, unit):
    if unit in ["Tesla (T)", "Tesla(T)", "tesla(T)", "tesla (T)"]:
        return value * 10000, "Gauss (G)"
    elif unit in ["Gauss (G)", "Gauss(G)", "gauss(G)", "gauss (G)"]:
        return value / 10000, "Tesla (T)"
    else:
        return value, unit

import math
def convert_magnetic_field(value, unit):
    if unit in ["Oersted (Oe)", "Oe", "oersted(Oe)", "oersted"]:
        return value / (4 * math.pi * 10**-3), "A m⁻¹"   
    elif unit in ["A m⁻¹", "A/m", "A m−1", "Ampere per meter"]:
        return value * (4 * math.pi * 10**-3), "oersted(Oe)"
    else:
        return value, unit



import math
def convert_magnetization(value, unit):
    if unit in ["A m⁻¹", "A/m", "A m−1", "Ampere per meter"]:
        return value * 10**-3, "emu cm⁻³"   
    elif unit in ["emu cm^-3", "emu/cm^3", "emu cm⁻³"]:
        return value / 10**-3, "A m⁻¹"      
    else:
        return value, unit


import math
def convert_magnetic_polarization(value, unit):
    if unit in ["Tesla (T)", "Tesla(T)", "tesla(T)", "tesla (T)", "T"]:
        return value * (10**4 / (4 * math.pi)), "emu cm⁻³"   
    elif unit in ["G", "Gauss (G)", "gauss(G)", "gauss (G)"]:
        return value / (10**4 / (4 * math.pi)), "T"           
    elif unit in ["emu cm⁻³", "emu/cm^3", "emu cm−3"]:
        return value / (10**4 / (4 * math.pi)), "T"
    else:
        return value, unit


import math
def convert_magnetic_moment(value, unit):
    if unit in ["A m^2", "A/m^2", "A m²", "Am^2"]:
        return value * 10**3, "emu = G cm³"   
    elif unit in ["emu = G cm³", "EMU"]:
        return value / 10**3, "A m²" 
    else:
        return value, unit


import math
def convert_magnetic_moment_per_unit_mass(value, unit):
    if unit in ["A m² kg⁻¹", "A m² kg⁻¹", "A m^2/kg", "A m² kg-1"]:
        return value * 10**3, "emu"   
    elif unit in ["emu g⁻¹", "EMU"]:
        return value / 10**3, "A m² kg⁻¹" 
    else:
        return value, unit




import math
def convert_volume_magnetic_susceptibility(value, unit):
    if unit in ["SI", "SI unit", "dimensionless (SI)", "dimensionless"]:
        return value * (1 / (4 * math.pi)), "cgs"   
    elif unit in ["cgs", "CGS", "cgs unit", "dimensionless (cgs)"]:
        return value / (1 / (4 * math.pi)), "SI"   
    else:
        return value, unit


import math
def convert_mass_magnetic_susceptibility(value, unit):
    if unit in ["m^3 kg^-1", "m³ kg⁻¹", "m^3/kg", "m³/kg"]:
        return value * (10**3 / (4 * math.pi)), "emu Oe^-1 g^-1"
    elif unit in ["emu Oe^-1 g^-1", "emu Oe^-1/g", "emu Oe−1 g−1"]:
        return value / (10**3 / (4 * math.pi)), "m^3 kg^-1"
    else:
        return value, unit


import math
def convert_molar_magnetic_susceptibility(value, unit):
    if unit in ["m^3 mol^-1", "m³ mol⁻¹", "m^3/mol", "m³/mol"]:
        return value * (10**6 / (4 * math.pi)), "emu Oe^-1 g^-1 mol^-1"
    elif unit in ["emu Oe^-1 g^-1 mol^-1", "emu Oe−1 g−1 mol−1"]:
        return value / (10**6 / (4 * math.pi)), "m^3 mol^-1"
    else:
        return value, unit


import math
def convert_magnetic_permeability(value, unit):
    if unit in ["H m^-1", "H/m", "H m−1", "Henry per meter"]:
        return value * (10**7 / (4 * math.pi)), "G Oe^-1"
    elif unit in ["G Oe^-1", "G/Oe", "G Oe−1"]:
        return value / (10**7 / (4 * math.pi)), "H m^-1"
    else:
        return value, unit
        

import math
def convert_magnetic_flux(value, unit):
    if unit in ["Weber (Wb)", "Weber", "Wb"]:
        return value * 10**8, "maxwell (Mx)"
    elif unit in ["maxwell (Mx)", "Maxwell", "Mx", "maxwell"]:
        return value / 10**8, "Weber (Wb)"
    else:
        return value, unit
        

import math
def convert_magnetic_scalar_potential(value, unit):
    if unit in ["A", "Ampere", "ampere"]:
        return value * (4 * math.pi / 10), "gilbert"
    elif unit in ["gilbert", "Gilbert"]:
        return value / (4 * math.pi / 10), "A"
    else:
        return value, unit
        

import math
def convert_magnetic_vector_potential(value, unit):
    if unit in ["Wb m^-1", "Wb/m", "Wb m−1", "Weber per meter"]:
        return value * 10**6, "emu"
    elif unit in ["emu", "EMU"]:
        return value / 10**6, "Wb m^-1"
    else:
        return value, unit
        

import math
def convert_magnetic_pole_strength(value, unit):
    if unit in ["A m", "A m^-1", "A m−1"]:
        return value * 10, "emu"
    elif unit in ["emu", "EMU"]:
        return value / 10, "A m"
    else:
        return value, unit
        

import math
def convert_demagnetizing_factor(value, unit):
    if unit in ["SI", "SI unit", "dimensionless (SI)"]:
        return value * (4 * math.pi), "cgs"
    elif unit in ["cgs", "CGS", "cgs unit", "dimensionless (cgs)"]:
        return value / (4 * math.pi), "SI"
    else:
        return value, unit

import math
def convert_magnetostriction_constant(value, unit):
    if unit in ["SI", "SI unit", "dimensionless (SI)"]:
        return value, "cgs"
    elif unit in ["cgs", "CGS", "cgs unit", "dimensionless (cgs)"]:
        return value, "SI"
    else:
        return value, unit
        

import math
def convert_anisotropy_constant(value, unit):
    if unit in ["J m^-3", "J/m^3", "J m−3"]:
        return value * 10, "erg cm^-3"
    elif unit in ["erg cm^-3", "erg/cm^3", "erg cm−3"]:
        return value / 10, "J m^-3"
    else:
        return value, unit
        

import math
def convert_magnetostatic_energy(value, unit):
    if unit in ["J m^-3", "J/m^3", "J m−3"]:
        return value * 10, "erg cm^-3"
    elif unit in ["erg cm^-3", "erg/cm^3", "erg cm−3"]:
        return value / 10, "J m^-3"
    else:
        return value, unit
        

import math
def convert_energy_product(value, unit):
    if unit in ["J m^-3", "J/m^3", "J m−3"]:
        return value * 10, "erg cm^-3"
    elif unit in ["erg cm^-3", "erg/cm^3", "erg cm−3"]:
        return value / 10, "J m^-3"
    else:
        return value, unit


if quantity == "Force(F)":
    result, result_unit = convert_force(value, selected_unit)

elif quantity == "Energy(E)":
    result, result_unit = convert_energy(value, selected_unit)

elif quantity == "Power(P)":
    result, result_unit = convert_power(value, selected_unit)

elif quantity == "Pressure(p)":
    result, result_unit = convert_pressure(value, selected_unit)

elif quantity == "Length(L)":
    result, result_unit = convert_length(value, selected_unit)

elif quantity == "Mass(M)":
    result, result_unit = convert_mass(value, selected_unit)

elif quantity == "Time(T)":
    result, result_unit = convert_time(value, selected_unit)
    
elif quantity == "Magnetic induction(B)":
    result, result_unit = convert_magnetic_induction(value, selected_unit)
    
elif quantity == "Magnetic field(H)":
    result, result_unit = convert_magnetic_field(value, selected_unit)

elif quantity == "Magnetization(M)":
    result, result_unit = convert_magnetization(value, selected_unit)

elif quantity == "Magnetic polarization(J)":
    result, result_unit = convert_magnetic_polarization(value, selected_unit)

elif quantity == "Magnetic moment(m)":
    result, result_unit = convert_magnetic_moment(value, selected_unit)

elif quantity == "Magnetic moment per unit mass(σ)":
    result, result_unit = convert_magnetic_moment_per_unit_mass(value, selected_unit)

elif quantity == "Volume magnetic susceptibility(κ)":
    result, result_unit = convert_volume_magnetic_susceptibility(value, selected_unit)

elif quantity == "Mass magnetic susceptibility(χ)":
    result, result_unit = convert_mass_magnetic_susceptibility(value, selected_unit)

elif quantity == "Molar magnetic susceptibility(χm)":
    result, result_unit = convert_molar_magnetic_susceptibility(value, selected_unit)

elif quantity == "Magnetic permeability(μ)":
    result, result_unit = convert_magnetic_permeability(value, selected_unit)

elif quantity == "Magnetic flux(Φ)":
    result, result_unit = convert_magnetic_flux(value, selected_unit)

elif quantity == "Magnetic scalar potential(φ)":
    result, result_unit = convert_magnetic_scalar_potential(value, selected_unit)

elif quantity == "Magnetic vector potential(A)":
    result, result_unit = convert_magnetic_vector_potential(value, selected_unit)

elif quantity == "Magnetic pole strength(p)":
    result, result_unit = convert_magnetic_pole_strength(value, selected_unit)

elif quantity == "Demagnetizing factor(N)":
    result, result_unit = convert_demagnetizing_factor(value, selected_unit)

elif quantity == "Magnetostriction constant(λ)":
    result, result_unit = convert_magnetostriction_constant(value, selected_unit)

elif quantity == "Anisotropy constant(K)":
    result, result_unit = convert_anisotropy_constant(value, selected_unit)

elif quantity == "Magnetostatic energy(Em)":
    result, result_unit = convert_magnetostatic_energy(value, selected_unit)

elif quantity == "Energy product((BH)max)":
    result, result_unit = convert_energy_product(value, selected_unit)



# -----------------------------
# 4. Answer
# -----------------------------
st.markdown(
    """<div class="ansewr"><div
class="answer-title">4. Your answer</div>""",
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
