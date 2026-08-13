import streamlit as st

st.title("SI to CGS Unit Converter")

value = st.number_input("Enter value", value=1.0)

unit = st.selectbox(
    "Select SI Unit",
    ["Meter (m)", "Kilogram (kg)", "Second (s)", "Newton (N)", "Joule (J)", "Pascal (Pa)"]
)

conversions = {
    "Meter (m)": ("Centimeter (cm)", 100),
    "Kilogram (kg)": ("Gram (g)", 1000),
    "Second (s)": ("Second (s)", 1),
    "Newton (N)": ("Dyne", 100000),
    "Joule (J)": ("Erg", 10000000),
    "Pascal (Pa)": ("Barye (Ba)", 10)
}

if st.button("Convert"):
    cgs_unit, factor = conversions[unit]
    result = value * factor

    st.success(f"{value} {unit.split(' ')[-1][1:-1]} = {result} {cgs_unit}")
