import streamlit as st
from tkinter import ttk

# ============================================================
# UNIT CONVERTER - SI / CGS
# ============================================================

BG = "#ffffff"
BLUE = "#2f55b7"
LIGHT_BLUE = "#f8faff"
BORDER_BLUE = "#dbe4fb"
GREEN = "#3d9b59"
LIGHT_GREEN = "#f7fcf8"
BORDER_GREEN = "#d8efdf"
TEXT = "#111111"
ARROW = "#333333"


# ============================================================
# CONVERSION DATA
# ============================================================

# Conversion factors are relative to the SI base unit
UNITS = {

    "Force": {
        "SI": {
            "Newton (N)": 1.0,
            "Kilonewton (kN)": 1000.0,
            "Meganewton (MN)": 1000000.0,
        },

        "CGS": {
            "dyne (dyn)": 0.00001,
            "kilodyne (kdyne)": 0.01,
        },
    },
    "Energy": {
        "SI": {
            "Joule (J)": 1.0,
            "Kilojoule (kJ)": 1000.0,
            "Megajoule (MJ)": 1000000.0,
        },

        "CGS": {
            "erg (erg)": 0.0000001,
            "kilerg (kerg)": 0.0001,
        },
    },

    "Power": {
        "SI": {
            "Watt (W)": 1.0,
            "Kilowatt (kW)": 1000.0,
            "Megawatt (MW)": 1000000.0,
        },

        "CGS": {
            "erg/second (erg/s)": 0.0000001,
        },
    },

    "Pressure": {
        "SI": {
            "Pascal (Pa)": 1.0,
            "Kilopascal (kPa)": 1000.0,
            "Megapascal (MPa)": 1000000.0,
        },

        "CGS": {
            "barye (Ba)": 0.1,
            "kilobarye (kBa)": 100.0,
        },
    },

    "Length": {
        "SI": {
            "meter (m)": 1.0,
            "kilometer (km)": 1000.0,
            "centimeter (cm)": 0.01,
            "millimeter (mm)": 0.001,
        },

        "CGS": {
            "centimeter (cm)": 0.01,
            "meter (m)": 1.0,
            "millimeter (mm)": 0.001,
        },
    },

    "Mass": {
        "SI": {
            "kilogram (kg)": 1.0,
            "gram (g)": 0.001,
            "milligram (mg)": 0.000001,
        },

        "CGS": {
            "gram (g)": 0.001,
            "milligram (mg)": 0.000001,
            "kilogram (kg)": 1.0,
        },
    },

    "Time": {
        "SI": {
            "second (s)": 1.0,
            "minute (min)": 60.0,
            "hour (h)": 3600.0,
        },

        "CGS": {
            "second (s)": 1.0,
            "minute (min)": 60.0,
            "hour (h)": 3600.0,
        },
    },

    "Velocity": {
        "SI": {
            "meter/second (m/s)": 1.0,
            "kilometer/hour (km/h)": 1000 / 3600,
        },

        "CGS": {
            "centimeter/second (cm/s)": 0.01,
            "meter/second (m/s)": 1.0,
        },
    },

    "Acceleration": {
        "SI": {
            "meter/second² (m/s²)": 1.0,
            "kilometer/second² (km/s²)": 1000.0,
        },

        "CGS": {
            "centimeter/second² (cm/s²)": 0.01,
            "meter/second² (m/s²)": 1.0,
        },
    },

    "Momentum": {
        "SI": {
            "kilogram meter/second (kg·m/s)": 1.0,
        },

        "CGS": {
            "gram centimeter/second (g·cm/s)": 0.00001,
        },
    },

    "Density": {
        "SI": {
            "kilogram/meter³ (kg/m³)": 1.0,
            "gram/meter³ (g/m³)": 0.001,
        },

        "CGS": {
            "gram/centimeter³ (g/cm³)": 1000.0,
            "kilogram/meter³ (kg/m³)": 1.0,
        },
    },
}


QUANTITIES = list(UNITS.keys())


# ============================================================
# NUMBER FORMAT
# ============================================================

def format_number(value):

    if value == 0:
        return "0"

    absolute_value = abs(value)

    # Scientific notation
    if absolute_value >= 100000 or absolute_value < 0.0001:

        text = f"{value:.6e}"

        mantissa, exponent = text.split("e")

        exponent = int(exponent)

        mantissa = mantissa.rstrip("0").rstrip(".")

        sign = "+" if exponent >= 0 else "-"

        return f"{mantissa} × 10^{sign}{abs(exponent)}"

    # Integer
    if value.is_integer():
        return str(int(value))

    # Decimal
    return f"{value:.10f}".rstrip("0").rstrip(".")


# ============================================================
# MAIN APPLICATION
# ============================================================

class UnitConverter:

    def __init__(self, root):

        self.root = root

        self.root.title("Unit Converter")

        self.root.geometry("1024x1450")

        self.root.minsize(760, 950)

        self.root.configure(bg=BG)


        # ----------------------------------------------------
        # VARIABLES
        # ----------------------------------------------------

        self.system_var = tk.StringVar(value="CGS")

        self.quantity_var = tk.StringVar(value="Force")

        self.input_value_var = tk.StringVar(value="50")

        self.input_unit_var = tk.StringVar()

        self.output_unit_var = tk.StringVar()


        # ----------------------------------------------------
        # BUILD UI
        # ----------------------------------------------------

        self.build_styles()

        self.build_header()

        self.build_interface()


        # ----------------------------------------------------
        # VARIABLE EVENTS
        # ----------------------------------------------------

        self.system_var.trace_add(
            "write",
            self.on_system_change
        )

        self.quantity_var.trace_add(
            "write",
            self.on_quantity_change
        )

        self.input_value_var.trace_add(
            "write",
            self.update_answer
        )

        self.input_unit_var.trace_add(
            "write",
            self.update_answer
        )

        self.output_unit_var.trace_add(
            "write",
            self.update_answer
        )


        # ----------------------------------------------------
        # INITIAL DATA
        # ----------------------------------------------------

        self.update_units()

        self.update_answer()


    # ========================================================
    # COMBOBOX STYLE
    # ========================================================

    def build_styles(self):

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Converter.TCombobox",

            font=("Arial", 20),

            padding=12,

            foreground=TEXT,

            fieldbackground="white",

            background="white",

            bordercolor="#c8c8c8",

            lightcolor="#c8c8c8",

            darkcolor="#c8c8c8",

            arrowcolor=ARROW,
        )

        style.map(
            "Converter.TCombobox",

            fieldbackground=[
                ("readonly", "white")
            ],

            background=[
                ("readonly", "white")
            ],
        )


    # ========================================================
    # HEADER
    # ========================================================

    def build_header(self):

        header = tk.Frame(
            self.root,

            bg=BLUE,

            height=124
        )

        header.pack(fill="x")

        header.pack_propagate(False)


        # Hamburger menu

        menu = tk.Label(

            header,

            text="☰",

            bg=BLUE,

            fg="white",

            font=("Arial", 38),

            cursor="hand2"
        )

        menu.place(
            x=38,
            y=30
        )


        # Title

        title = tk.Label(

            header,

            text="Unit Converter",

            bg=BLUE,

            fg="white",

            font=("Arial", 35, "bold")
        )

        title.place(

            relx=0.5,

            y=35,

            anchor="n"
        )


        # Star

        star = tk.Label(

            header,

            text="☆",

            bg=BLUE,

            fg="white",

            font=("Arial", 48),

            cursor="hand2"
        )

        star.place(

            relx=0.93,

            y=20,

            anchor="n"
        )


    # ========================================================
    # CARD CREATOR
    # ========================================================

    def make_card(
        self,
        title,
        number,
        answer=False
    ):

        if answer:

            background = LIGHT_GREEN

            border = BORDER_GREEN

            heading_color = GREEN

        else:

            background = LIGHT_BLUE

            border = BORDER_BLUE

            heading_color = BLUE


        outer = tk.Frame(

            self.root,

            bg=background,

            highlightbackground=border,

            highlightthickness=2,

            bd=0
        )

        outer.pack(

            fill="x",

            padx=38,

            pady=(
                42 if number == 1 else 0,
                0
            )
        )


        heading = tk.Label(

            outer,

            text=f"{number}. {title}",

            bg=background,

            fg=heading_color,

            font=("Arial", 26, "bold"),

            anchor="w"
        )

        heading.pack(

            fill="x",

            padx=30,

            pady=(30, 25)
        )


        return outer


    # ========================================================
    # INTERFACE
    # ========================================================

    def build_interface(self):

        # ====================================================
        # 1. CONVERT IN
        # ====================================================

        card1 = self.make_card(

            "Convert in",

            1
        )


        self.system_combo = ttk.Combobox(

            card1,

            textvariable=self.system_var,

            values=[
                "SI",
                "CGS"
            ],

            state="readonly",

            style="Converter.TCombobox"
        )


        self.system_combo.pack(

            fill="x",

            padx=30,

            pady=(0, 42),

            ipady=8
        )


        # ====================================================
        # 2. PHYSICAL QUANTITY
        # ====================================================

        card2 = self.make_card(

            "Physical Quantity",

            2
        )


        self.quantity_combo = ttk.Combobox(

            card2,

            textvariable=self.quantity_var,

            values=QUANTITIES,

            state="readonly",

            style="Converter.TCombobox"
        )


        self.quantity_combo.pack(

            fill="x",

            padx=30,

            pady=(0, 42),

            ipady=8
        )


        # ====================================================
        # 3. ENTER VALUE
        # ====================================================

        card3 = self.make_card(

            "Enter value",

            3
        )


        row3 = tk.Frame(

            card3,

            bg=LIGHT_BLUE
        )


        row3.pack(

            fill="x",

            padx=30,

            pady=(0, 42)
        )


        row3.grid_columnconfigure(

            0,

            weight=1
        )


        row3.grid_columnconfigure(

            1,

            weight=1
        )


        # Value input

        self.value_entry = tk.Entry(

            row3,

            textvariable=self.input_value_var,

            font=("Arial", 22),

            relief="solid",

            bd=1,

            highlightthickness=1,

            highlightbackground="#c8c8c8"
        )


        self.value_entry.grid(

            row=0,

            column=0,

            sticky="ew",

            ipady=18,

            padx=(0, 16)
        )


        # Input unit

        self.input_combo = ttk.Combobox(

            row3,

            textvariable=self.input_unit_var,

            state="readonly",

            style="Converter.TCombobox"
        )


        self.input_combo.grid(

            row=0,

            column=1,

            sticky="ew",

            ipady=8,

            padx=(16, 0)
        )


        # ====================================================
        # 4. YOUR ANSWER
        # ====================================================

        card4 = self.make_card(

            "Your answer",

            4,

            answer=True
        )


        row4 = tk.Frame(

            card4,

            bg=LIGHT_GREEN
        )


        row4.pack(

            fill="x",

            padx=30,

            pady=(0, 42)
        )


        row4.grid_columnconfigure(

            0,

            weight=1
        )


        row4.grid_columnconfigure(

            1,

            weight=1
        )


        # Answer value

        self.answer_value_label = tk.Label(

            row4,

            text="",

            bg="white",

            fg=TEXT,

            font=("Arial", 22),

            anchor="w",

            padx=25,

            relief="solid",

            bd=1
        )


        self.answer_value_label.grid(

            row=0,

            column=0,

            sticky="ew",

            ipady=18,

            padx=(0, 16)
        )


        # Output unit

        self.output_combo = ttk.Combobox(

            row4,

            textvariable=self.output_unit_var,

            state="readonly",

            style="Converter.TCombobox"
        )


        self.output_combo.grid(

            row=0,

            column=1,

            sticky="ew",

            ipady=8,

            padx=(16, 0)
        )


        # ====================================================
        # STATUS
        # ====================================================

        self.status_label = tk.Label(

            self.root,

            text="",

            bg=BG,

            fg="#666666",

            font=("Arial", 13)
        )


        self.status_label.pack(

            pady=24
        )


    # ========================================================
    # SYSTEM CHANGE
    # ========================================================

    def on_system_change(self, *_):

        self.update_units()


    # ========================================================
    # QUANTITY CHANGE
    # ========================================================

    def on_quantity_change(self, *_):

        self.update_units()


    # ========================================================
    # UPDATE UNITS
    # ========================================================

    def update_units(self):

        quantity = self.quantity_var.get()

        system = self.system_var.get()


        if quantity not in UNITS:

            return


        units = list(
            UNITS[quantity][system].keys()
        )


        # Update input dropdown

        self.input_combo["values"] = units


        # Update output dropdown

        self.output_combo["values"] = units


        # ----------------------------------------------------
        # Default units
        # ----------------------------------------------------

        # Screenshot example:
        #
        # 50 Newton
        #
        # becomes
        #
        # 5.0 × 10^6 dyne

        if (
            quantity == "Force"
            and
            system == "CGS"
        ):

            input_default = "Newton (N)"

            output_default = "dyne (dyn)"


        else:

            input_default = units[0]

            if len(units) > 1:

                output_default = units[1]

            else:

                output_default = units[0]


        # Set input unit

        if input_default in units:

            self.input_unit_var.set(
                input_default
            )

        else:

            self.input_unit_var.set(
                units[0]
            )


        # Set output unit

        if output_default in units:

            self.output_unit_var.set(
                output_default
            )

        else:

            self.output_unit_var.set(
                units[0]
            )


        self.update_answer()


    # ========================================================
    # CALCULATE ANSWER
    # ========================================================

    def update_answer(self, *_):

        quantity = self.quantity_var.get()

        system = self.system_var.get()

        input_unit = self.input_unit_var.get()

        output_unit = self.output_unit_var.get()


        if not input_unit or not output_unit:

            return


        # ----------------------------------------------------
        # Read number
        # ----------------------------------------------------

        try:

            value = float(
                self.input_value_var.get().strip()
            )

        except ValueError:

            self.answer_value_label.config(
                text="—"
            )

            self.status_label.config(

                text="Please enter a valid number."
            )

            return


        units = UNITS[quantity][system]


        if (
            input_unit not in units
            or
            output_unit not in units
        ):

            return


        # ----------------------------------------------------
        # Convert
        #
        # Input unit
        #       ↓
        # SI base unit
        #       ↓
        # Output unit
        # ----------------------------------------------------

        base_value = (
            value
            *
            units[input_unit]
        )


        result = (
            base_value
            /
            units[output_unit]
        )


        # ----------------------------------------------------
        # Show result
        # ----------------------------------------------------

        self.answer_value_label.config(

            text=format_number(result)
        )


        # Status text

        self.status_label.config(

            text=(
                f"{format_number(value)} "
                f"{input_unit}"
                f"  =  "
                f"{format_number(result)} "
                f"{output_unit}"
            )
        )


# ============================================================
# MAIN
# ============================================================

def main():

    root = tk.Tk()

    app = UnitConverter(root)

    root.mainloop()


# ============================================================
# RUN PROGRAM
# ============================================================
if __name__ == "__main__":

    main()
