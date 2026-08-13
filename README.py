import streamlit as st
from math import pi


# ============================================================
# UNIT CONVERTER
# SI <-> CGS
# ============================================================

class UnitConverterApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("600x850")
        self.root.minsize(500, 700)
        self.root.configure(bg="#ffffff")

        # ----------------------------------------------------
        # COLORS
        # ----------------------------------------------------
        self.BLUE = "#3158B7"
        self.DARK_BLUE = "#244A9F"
        self.CARD = "#F9F9FD"
        self.BORDER = "#DDE2EE"
        self.GREEN_BG = "#F1FAF4"
        self.GREEN = "#4A9B5D"
        self.TEXT = "#111111"

        # ----------------------------------------------------
        # DATA
        # ----------------------------------------------------
        self.units = {

            "Length": {
                "SI": {
                    "meter (m)": 1,
                    "kilometer (km)": 1000,
                    "centimeter (cm)": 0.01,
                    "millimeter (mm)": 0.001
                },
                "CGS": {
                    "centimeter (cm)": 1,
                    "millimeter (mm)": 0.1,
                    "meter (m)": 100,
                    "kilometer (km)": 100000
                }
            },

            "Mass": {
                "SI": {
                    "kilogram (kg)": 1,
                    "gram (g)": 0.001,
                    "milligram (mg)": 0.000001
                },
                "CGS": {
                    "gram (g)": 1,
                    "milligram (mg)": 0.001,
                    "kilogram (kg)": 1000
                }
            },

            "Time": {
                "SI": {
                    "second (s)": 1,
                    "minute (min)": 60,
                    "hour (h)": 3600
                },
                "CGS": {
                    "second (s)": 1,
                    "minute (min)": 60,
                    "hour (h)": 3600
                }
            },

            "Force": {
                "SI": {
                    "Newton (N)": 1
                },
                "CGS": {
                    "dyne (dyn)": 1e-5
                }
            },

            "Energy": {
                "SI": {
                    "Joule (J)": 1
                },
                "CGS": {
                    "erg (erg)": 1e-7
                }
            },

            "Power": {
                "SI": {
                    "Watt (W)": 1
                },
                "CGS": {
                    "erg/second (erg/s)": 1e-7
                }
            },

            "Pressure": {
                "SI": {
                    "Pascal (Pa)": 1
                },
                "CGS": {
                    "barye (Ba)": 0.1
                }
            },

            "Velocity": {
                "SI": {
                    "meter/second (m/s)": 1,
                    "kilometer/hour (km/h)": 1000 / 3600
                },
                "CGS": {
                    "centimeter/second (cm/s)": 0.01
                }
            },

            "Acceleration": {
                "SI": {
                    "meter/second² (m/s²)": 1
                },
                "CGS": {
                    "gal (Gal)": 0.01
                }
            },

            "Density": {
                "SI": {
                    "kg/m³": 1
                },
                "CGS": {
                    "g/cm³": 1000
                }
            },

            "Momentum": {
                "SI": {
                    "kg·m/s": 1
                },
                "CGS": {
                    "g·cm/s": 1e-5
                }
            },

            "Frequency": {
                "SI": {
                    "Hertz (Hz)": 1
                },
                "CGS": {
                    "Hertz (Hz)": 1
                }
            },

            "Area": {
                "SI": {
                    "m²": 1,
                    "km²": 1e6,
                    "cm²": 0.0001
                },
                "CGS": {
                    "cm²": 1,
                    "m²": 10000
                }
            },

            "Volume": {
                "SI": {
                    "m³": 1,
                    "liter (L)": 0.001,
                    "cm³": 1e-6
                },
                "CGS": {
                    "cm³": 1,
                    "m³": 1e6,
                    "liter (L)": 1000
                }
            },

            "Temperature": {
                "SI": {
                    "Kelvin (K)": 1
                },
                "CGS": {
                    "Celsius (°C)": 1
                }
            }
        }

        self.create_styles()
        self.create_header()
        self.create_main_ui()

        # Initial values
        self.system_var.set("CGS")
        self.quantity_var.set("Force")
        self.update_units()

    # ========================================================
    # STYLES
    # ========================================================

    def create_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "TCombobox",
            font=("Arial", 15),
            padding=12,
            fieldbackground="white",
            background="white"
        )

        style.map(
            "TCombobox",
            fieldbackground=[("readonly", "white")]
        )

    # ========================================================
    # HEADER
    # ========================================================

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg=self.BLUE,
            height=100
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        # Menu icon
        menu = tk.Label(
            header,
            text="☰",
            font=("Arial", 30),
            fg="white",
            bg=self.BLUE
        )
        menu.pack(side="left", padx=25)

        # Title
        title = tk.Label(
            header,
            text="Unit Converter",
            font=("Arial", 27, "bold"),
            fg="white",
            bg=self.BLUE
        )
        title.pack(side="left", expand=True)

        # Star
        star = tk.Label(
            header,
            text="☆",
            font=("Arial", 38),
            fg="white",
            bg=self.BLUE
        )
        star.pack(side="right", padx=25)

    # ========================================================
    # MAIN UI
    # ========================================================

    def create_main_ui(self):

        main = tk.Frame(
            self.root,
            bg="white"
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        # ----------------------------------------------------
        # 1. CONVERT IN
        # ----------------------------------------------------

        card1 = self.create_card(main)

        tk.Label(
            card1,
            text="1. Convert in",
            font=("Arial", 20, "bold"),
            fg=self.BLUE,
            bg=self.CARD
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 12)
        )

        self.system_var = tk.StringVar()

        self.system_combo = ttk.Combobox(
            card1,
            textvariable=self.system_var,
            values=["SI", "CGS"],
            state="readonly"
        )

        self.system_combo.pack(
            fill="x",
            padx=25,
            pady=(0, 22),
            ipady=7
        )

        self.system_combo.bind(
            "<<ComboboxSelected>>",
            lambda e: self.update_units()
        )

        # ----------------------------------------------------
        # 2. PHYSICAL QUANTITY
        # ----------------------------------------------------

        card2 = self.create_card(main)

        tk.Label(
            card2,
            text="2. Physical Quantity",
            font=("Arial", 20, "bold"),
            fg=self.BLUE,
            bg=self.CARD
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 12)
        )

        self.quantity_var = tk.StringVar()

        self.quantity_combo = ttk.Combobox(
            card2,
            textvariable=self.quantity_var,
            values=list(self.units.keys()),
            state="readonly"
        )

        self.quantity_combo.pack(
            fill="x",
            padx=25,
            pady=(0, 22),
            ipady=7
        )

        self.quantity_combo.bind(
            "<<ComboboxSelected>>",
            lambda e: self.update_units()
        )

        # ----------------------------------------------------
        # 3. ENTER VALUE
        # ----------------------------------------------------

        card3 = self.create_card(main)

        tk.Label(
            card3,
            text="3. Enter value",
            font=("Arial", 20, "bold"),
            fg=self.BLUE,
            bg=self.CARD
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 12)
        )

        input_frame = tk.Frame(
            card3,
            bg=self.CARD
        )

        input_frame.pack(
            fill="x",
            padx=25,
            pady=(0, 22)
        )

        self.value_var = tk.StringVar(value="50")

        self.value_entry = tk.Entry(
            input_frame,
            textvariable=self.value_var,
            font=("Arial", 20),
            bd=1,
            relief="solid"
        )

        self.value_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=12
        )

        self.unit_var = tk.StringVar()

        self.unit_combo = ttk.Combobox(
            input_frame,
            textvariable=self.unit_var,
            state="readonly",
            width=22
        )

        self.unit_combo.pack(
            side="left",
            padx=(20, 0),
            ipady=9
        )

        self.value_var.trace_add(
            "write",
            lambda *args: self.convert()
        )

        self.unit_combo.bind(
            "<<ComboboxSelected>>",
            lambda e: self.convert()
        )

        # ----------------------------------------------------
        # 4. YOUR ANSWER
        # ----------------------------------------------------

        card4 = tk.Frame(
            main,
            bg=self.GREEN_BG,
            highlightbackground="#D8E9DC",
            highlightthickness=1
        )

        card4.pack(
            fill="x",
            pady=(15, 0)
        )

        tk.Label(
            card4,
            text="4. Your answer",
            font=("Arial", 20, "bold"),
            fg=self.GREEN,
            bg=self.GREEN_BG
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 12)
        )

        answer_frame = tk.Frame(
            card4,
            bg=self.GREEN_BG
        )

        answer_frame.pack(
            fill="x",
            padx=25,
            pady=(0, 22)
        )

        self.answer_var = tk.StringVar()

        self.answer_entry = tk.Entry(
            answer_frame,
            textvariable=self.answer_var,
            font=("Arial", 19),
            bd=1,
            relief="solid",
            state="readonly",
            readonlybackground="white"
        )

        self.answer_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=12
        )

        self.answer_unit_var = tk.StringVar()

        self.answer_unit_entry = tk.Entry(
            answer_frame,
            textvariable=self.answer_unit_var,
            font=("Arial", 16),
            bd=1,
            relief="solid",
            state="readonly",
            readonlybackground="white",
            width=22
        )

        self.answer_unit_entry.pack(
            side="left",
            padx=(20, 0),
            ipady=13
        )

    # ========================================================
    # CARD
    # ========================================================

    def create_card(self, parent):

        card = tk.Frame(
            parent,
            bg=self.CARD,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=(0, 20)
        )

        return card

    # ========================================================
    # UPDATE UNITS
    # ========================================================

    def update_units(self):

        quantity = self.quantity_var.get()
        target_system = self.system_var.get()

        if not quantity or not target_system:
            return

        available_units = []

        # Input unit can be SI or CGS
        available_units.extend(
            self.units[quantity]["SI"].keys()
        )

        for unit in self.units[quantity]["CGS"].keys():
            if unit not in available_units:
                available_units.append(unit)

        self.unit_combo["values"] = available_units

        # Screenshot example:
        # Target = CGS
        # Force = Newton
        if quantity == "Force" and target_system == "CGS":
            self.unit_var.set("Newton (N)")

        else:
            self.unit_var.set(available_units[0])

        self.convert()

    # ========================================================
    # CONVERSION
    # ========================================================

    def convert(self):

        try:
            value = float(self.value_var.get())

        except ValueError:
            self.answer_var.set("")
            self.answer_unit_var.set("")
            return

        quantity = self.quantity_var.get()
        target_system = self.system_var.get()
        source_unit = self.unit_var.get()

        if not quantity or not target_system or not source_unit:
            return

        # ----------------------------------------------------
        # Temperature special case
        # ----------------------------------------------------

        if quantity == "Temperature":

            result, result_unit = self.convert_temperature(
                value,
                source_unit,
                target_system
            )

        else:

            source_factor = self.get_factor(
                quantity,
                source_unit
            )

            target_unit = self.get_target_unit(
                quantity,
                target_system
            )

            target_factor = self.get_factor(
                quantity,
                target_unit
            )

            # Convert source -> base -> target
            base_value = value * source_factor

            result = base_value / target_factor

            result_unit = target_unit

        self.answer_var.set(
            self.format_number(result)
        )

        self.answer_unit_var.set(
            result_unit
        )

    # ========================================================
    # GET FACTOR
    # ========================================================

    def get_factor(self, quantity, unit):

        if unit in self.units[quantity]["SI"]:
            return self.units[quantity]["SI"][unit]

        if unit in self.units[quantity]["CGS"]:
            return self.units[quantity]["CGS"][unit]

        return 1

    # ========================================================
    # TARGET UNIT
    # ========================================================

    def get_target_unit(self, quantity, target_system):

        return list(
            self.units[quantity][target_system].keys()
        )[0]

    # ========================================================
    # TEMPERATURE
    # ========================================================

    def convert_temperature(
        self,
        value,
        source_unit,
        target_system
    ):

        # Kelvin -> Celsius
        if source_unit == "Kelvin (K)":

            if target_system == "CGS":
                return value - 273.15, "Celsius (°C)"

            return value, "Kelvin (K)"

        # Celsius -> Kelvin
        if source_unit == "Celsius (°C)":

            if target_system == "SI":
                return value + 273.15, "Kelvin (K)"

            return value, "Celsius (°C)"

        return value, source_unit

    # ========================================================
    # FORMAT RESULT
    # ========================================================

    def format_number(self, number):

        if number == 0:
            return "0"

        abs_number = abs(number)

        # Scientific notation for very large/small values
        if abs_number >= 1e4 or abs_number < 1e-3:

            exponent = 0
            mantissa = number

            while abs(mantissa) >= 10:
                mantissa /= 10
                exponent += 1

            while 0 < abs(mantissa) < 1:
                mantissa *= 10
                exponent -= 1

            return f"{mantissa:.2f} × 10{self.superscript(exponent)}"

        # Normal number
        if number.is_integer():
            return f"{int(number):,}"

        return f"{number:.6g}"

    # ========================================================
    # SUPERSCRIPT
    # ========================================================

    def superscript(self, number):

        chars = {
            "0": "⁰",
            "1": "¹",
            "2": "²",
            "3": "³",
            "4": "⁴",
            "5": "⁵",
            "6": "⁶",
            "7": "⁷",
            "8": "⁸",
            "9": "⁹",
            "-": "⁻"
        }

        return "".join(
            chars.get(c, c)
            for c in str(number)
        )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = UnitConverterApp(root)

    root.mainloop()
