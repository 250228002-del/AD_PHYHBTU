# SI to CGS Unit Converter

def si_to_cgs(value, unit):
    conversions = {
        "m": ("cm", 100),       
        "kg": ("g", 1000),      
        "s": ("s", 1),          
        "N": ("dyne", 100000),  
        "J": ("erg", 10000000), 
        "Pa": ("Ba", 10),      
    }

    if unit in conversions:
        cgs_unit, factor = conversions[unit]
        result = value * factor
        return f"{result} {cgs_unit}"
    else:
        return "Unit not supported."


# Example
value = float(input("Enter value: "))
unit = input("Enter SI unit (m, kg, s, N, J, Pa): ")

print("CGS value:", si_to_cgs(value, unit))
