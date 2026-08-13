import tkinter as tk
from tkinter import ttk


# -----------------------------
# Unit Conversion Data
# -----------------------------

units = {
    "Force": {
        "SI": {
            "Newton (N)": 1
        },
        "CGS": {
            "Dyne (dyn)": 1,
            "Newton (N)": 100000
        }
    },

    "Length": {
        "SI": {
            "Meter (m)": 1,
            "Kilometer (km)": 1000,
            "Centimeter (cm)": 0.01
        },
        "CGS": {
            "Centimeter (cm)": 1,
            "Meter (m)": 100
        }
    },

    "Mass": {
        "SI": {
            "Kilogram (kg)": 1,
            "Gram (g)": 0.001
        },
        "CGS": {
            "Gram (g)": 1,
            "Kilogram (kg)": 1000
        }
    },

    "Time": {
        "SI": {
            "Second (s)": 1,
            "Minute (min)": 60,
            "Hour (h)": 3600
        },
        "CGS": {
            "Second (s)": 1,
            "Minute (min)": 60,
            "Hour (h)": 3600
        }
    }
}


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()

root.title("Unit Converter")
root.geometry("700x750")
root.configure(bg="white")


# -----------------------------
# Title
# -----------------------------

title = tk.Label(
    root,
    text="Unit Converter",
    font=("Arial", 28, "bold"),
    bg="#3159b7",
    fg="white",
    pady=20
)

title.pack(fill="x")


# -----------------------------
# 1. Convert in
# -----------------------------

tk.Label(
    root,
    text="1. Convert in",
    font=("Arial", 18, "bold"),
    fg="#3159b7",
    bg="white"
).pack(anchor="w", padx=40, pady=(30, 10))


system = ttk.Combobox(
    root,
    values=["SI", "CGS"],
    state="readonly",
    font=("Arial", 16)
)

system.pack(fill="x", padx=40, ipady=8)

system.set("CGS")


# -----------------------------
# 2. Physical Quantity
# -----------------------------

tk.Label(
    root,
    text="2. Physical Quantity",
    font=("Arial", 18, "bold"),
    fg="#3159b7",
    bg="white"
).pack(anchor="w", padx=40, pady=(30, 10))


quantity = ttk.Combobox(
    root,
    values=list(units.keys()),
    state="readonly",
    font=("Arial", 16)
)

quantity.pack(fill="x", padx=40, ipady=8)

quantity.set("Force")


# -----------------------------
# 3. Enter Value
# -----------------------------

tk.Label(
    root,
    text="3. Enter value",
    font=("Arial", 18, "bold"),
    fg="#3159b7",
    bg="white"
).pack(anchor="w", padx=40, pady=(30, 10))


value_frame = tk.Frame(root, bg="white")
value_frame.pack(fill="x", padx=40)


value = tk.Entry(
    value_frame,
    font=("Arial", 18)
)

value.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10
)

value.insert(0, "50")


from_unit = ttk.Combobox(
    value_frame,
    state="readonly",
    font=("Arial", 14)
)

from_unit.pack(
    side="right",
    padx=(15, 0),
    ipady=8
)


# -----------------------------
# 4. Answer
# -----------------------------

tk.Label(
    root,
    text="4. Your answer",
    font=("Arial", 18, "bold"),
    fg="#4d9367",
    bg="white"
).pack(anchor="w", padx=40, pady=(30, 10))


answer_frame = tk.Frame(root, bg="#f2faf5")
answer_frame.pack(fill="x", padx=40)


answer = tk.Entry(
    answer_frame,
    font=("Arial", 18),
    state="readonly"
)

answer.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=10
)


to_unit = ttk.Combobox(
    answer_frame,
    state="readonly",
    font=("Arial", 14)
)

to_unit.pack(
    side="right",
    padx=(15, 0),
    ipady=8
)


# -----------------------------
# Update Units
# -----------------------------

def update_units(event=None):

    selected_system = system.get()
    selected_quantity = quantity.get()

    available_units = list(
        units[selected_quantity][selected_system].keys()
    )

    from_unit["values"] = available_units
    to_unit["values"] = available_units

    if len(available_units) > 0:
        from_unit.set(available_units[0])

    if len(available_units) > 1:
        to_unit.set(available_units[1])
    else:
        to_unit.set(available_units[0])


# -----------------------------
# Convert
# -----------------------------

def convert():

    try:

        number = float(value.get())

        selected_system = system.get()
        selected_quantity = quantity.get()

        source = from_unit.get()
        target = to_unit.get()

        source_factor = units[
            selected_quantity
        ][selected_system][source]

        target_factor = units[
            selected_quantity
        ][selected_system][target]

        # Convert to base unit
        base_value = number * source_factor

        # Convert to target
        result = base_value / target_factor

        answer.config(state="normal")

        answer.delete(0, tk.END)

        answer.insert(
            0,
            f"{result:.6g}"
        )

        answer.config(state="readonly")

    except ValueError:

        answer.config(state="normal")

        answer.delete(0, tk.END)

        answer.insert(0, "Invalid value")

        answer.config(state="readonly")


# -----------------------------
# Convert Button
# -----------------------------

convert_button = tk.Button(
    root,
    text="Convert",
    command=convert,
    font=("Arial", 16, "bold"),
    bg="#3159b7",
    fg="white",
    padx=30,
    pady=10
)

convert_button.pack(pady=30)


# -----------------------------
# Events
# -----------------------------

system.bind(
    "<<ComboboxSelected>>",
    update_units
)

quantity.bind(
    "<<ComboboxSelected>>",
    update_units
)


# -----------------------------
# Start
# -----------------------------

update_units()

root.mainloop()
