import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄")

st.title("🔄 Unit Converter")
st.write("Convert common units easily.")

value = st.number_input("Enter value", value=1.0)

conversion = st.selectbox(
    "Choose conversion",
    [
        "Kilometer → Meter",
        "Meter → Kilometer",
        "Meter → Centimeter",
        "Centimeter → Meter",
        "Kilogram → Gram",
        "Gram → Kilogram",
        "Celsius → Fahrenheit",
        "Fahrenheit → Celsius",
        "Liter → Milliliter",
        "Milliliter → Liter"
    ]
)

if conversion == "Kilometer → Meter":
    result = value * 1000
elif conversion == "Meter → Kilometer":
    result = value / 1000
elif conversion == "Meter → Centimeter":
    result = value * 100
elif conversion == "Centimeter → Meter":
    result = value / 100
elif conversion == "Kilogram → Gram":
    result = value * 1000
elif conversion == "Gram → Kilogram":
    result = value / 1000
elif conversion == "Celsius → Fahrenheit":
    result = (value * 9 / 5) + 32
elif conversion == "Fahrenheit → Celsius":
    result = (value - 32) * 5 / 9
elif conversion == "Liter → Milliliter":
    result = value * 1000
elif conversion == "Milliliter → Liter":
    result = value / 1000

st.success(f"Result: {result:g}")
