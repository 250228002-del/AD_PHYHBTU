<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Unit Converter</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: #ffffff;
    color: #111;
}

/* Header */
.header {
    height: 125px;
    background: linear-gradient(135deg, #3159b7, #294fa9);
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 40px;
}

.menu {
    font-size: 42px;
    cursor: pointer;
}

.title {
    font-size: 42px;
    font-weight: bold;
}

.star {
    font-size: 52px;
    cursor: pointer;
}

/* Main */
.container {
    width: 92%;
    max-width: 1000px;
    margin: 45px auto;
}

/* Cards */
.card {
    background: #f9faff;
    border: 1px solid #dce2ee;
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 28px;
}

.card.answer-card {
    background: #f2faf5;
    border-color: #cfe7d7;
}

.heading {
    color: #3159b7;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 22px;
}

.answer-heading {
    color: #4d9568;
}

/* Inputs */
select,
input {
    width: 100%;
    height: 70px;
    border: 1px solid #bfc2c8;
    border-radius: 14px;
    background: white;
    padding: 0 25px;
    font-size: 23px;
    outline: none;
}

select:focus,
input:focus {
    border: 2px solid #3159b7;
}

/* Value row */
.value-row,
.answer-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
}

/* Buttons */
.buttons {
    display: flex;
    gap: 15px;
    margin-top: 20px;
}

button {
    border: none;
    border-radius: 10px;
    padding: 15px 30px;
    font-size: 18px;
    cursor: pointer;
}

.convert-btn {
    background: #3159b7;
    color: white;
}

.swap-btn {
    background: white;
    color: #3159b7;
    border: 1px solid #3159b7;
}

.clear-btn {
    background: white;
    color: #555;
    border: 1px solid #aaa;
}

button:hover {
    opacity: 0.85;
}

.status {
    margin-top: 15px;
    color: #666;
    font-size: 15px;
}

/* Mobile */
@media (max-width: 700px) {

    .header {
        height: 90px;
        padding: 0 20px;
    }

    .menu {
        font-size: 30px;
    }

    .title {
        font-size: 25px;
    }

    .star {
        font-size: 35px;
    }

    .container {
        width: 94%;
        margin-top: 25px;
    }

    .card {
        padding: 20px;
    }

    .heading {
        font-size: 22px;
    }

    .value-row,
    .answer-row {
        grid-template-columns: 1fr;
        gap: 15px;
    }

    select,
    input {
        height: 60px;
        font-size: 18px;
    }

    .buttons {
        flex-wrap: wrap;
    }
}
</style>
</head>

<body>

<!-- Header -->
<div class="header">

    <div class="menu">☰</div>

    <div class="title">
        Unit Converter
    </div>

    <div class="star" onclick="toggleFavorite()">
        ☆
    </div>

</div>


<div class="container">

    <!-- 1 -->
    <div class="card">

        <div class="heading">
            1. Convert in
        </div>

        <select id="system">
            <option value="SI">SI</option>
            <option value="CGS" selected>CGS</option>
        </select>

    </div>


    <!-- 2 -->
    <div class="card">

        <div class="heading">
            2. Physical Quantity
        </div>

        <select id="quantity">
            <option value="Length">Length</option>
            <option value="Mass">Mass</option>
            <option value="Time">Time</option>
            <option value="Area">Area</option>
            <option value="Volume">Volume</option>
            <option value="Speed">Speed</option>
            <option value="Acceleration">Acceleration</option>
            <option value="Force" selected>Force</option>
            <option value="Pressure">Pressure</option>
            <option value="Energy">Energy / Work</option>
            <option value="Power">Power</option>
            <option value="Frequency">Frequency</option>
            <option value="Density">Density</option>
            <option value="Momentum">Momentum</option>
            <option value="Charge">Electric Charge</option>
            <option value="Voltage">Voltage</option>
            <option value="Resistance">Resistance</option>
            <option value="Capacitance">Capacitance</option>
            <option value="Temperature">Temperature</option>
        </select>

    </div>


    <!-- 3 -->
    <div class="card">

        <div class="heading">
            3. Enter value
        </div>

        <div class="value-row">

            <input
                type="number"
                id="value"
                value="50"
                placeholder="Enter value"
            >

            <select id="fromUnit"></select>

        </div>

    </div>


    <!-- 4 -->
    <div class="card answer-card">

        <div class="heading answer-heading">
            4. Your answer
        </div>

        <div class="answer-row">

            <input
                type="text"
                id="answer"
                value="5.0 × 10⁶"
                readonly
            >

            <select id="toUnit"></select>

        </div>

        <div class="status" id="status">
            Ready
        </div>

    </div>


    <!-- Buttons -->
    <div class="buttons">

        <button class="convert-btn" onclick="convert()">
            Convert
        </button>

        <button class="swap-btn" onclick="swapUnits()">
            ⇄ Swap
        </button>

        <button class="clear-btn" onclick="clearValue()">
            Clear
        </button>

    </div>

</div>


<script>

/*
=========================================================
UNIT DATABASE
factor = value of one unit in SI base unit
=========================================================
*/

const units = {

    Length: {

        SI: {
            "Meter (m)": 1,
            "Kilometer (km)": 1000,
            "Centimeter (cm)": 0.01,
            "Millimeter (mm)": 0.001,
            "Micrometer (µm)": 0.000001
        },

        CGS: {
            "Centimeter (cm)": 1,
            "Millimeter (mm)": 0.1,
            "Meter (m)": 100,
            "Micrometer (µm)": 0.0001
        }
    },


    Mass: {

        SI: {
            "Kilogram (kg)": 1,
            "Gram (g)": 0.001,
            "Milligram (mg)": 0.000001,
            "Tonne (t)": 1000
        },

        CGS: {
            "Gram (g)": 1,
            "Kilogram (kg)": 1000,
            "Milligram (mg)": 0.001
        }
    },


    Time: {

        SI: {
            "Second (s)": 1,
            "Millisecond (ms)": 0.001,
            "Minute (min)": 60,
            "Hour (h)": 3600,
            "Day (day)": 86400
        },

        CGS: {
            "Second (s)": 1,
            "Millisecond (ms)": 0.001,
            "Minute (min)": 60,
            "Hour (h)": 3600
        }
    },


    Area: {

        SI: {
            "Square meter (m²)": 1,
            "Square kilometer (km²)": 1000000,
            "Square centimeter (cm²)": 0.0001,
            "Square millimeter (mm²)": 0.000001
        },

        CGS: {
            "Square centimeter (cm²)": 1,
            "Square meter (m²)": 10000,
            "Square millimeter (mm²)": 0.01
        }
    },


    Volume: {

        SI: {
            "Cubic meter (m³)": 1,
            "Liter (L)": 0.001,
            "Milliliter (mL)": 0.000001,
            "Cubic centimeter (cm³)": 0.000001
        },

        CGS: {
            "Cubic centimeter (cm³)": 1,
            "Milliliter (mL)": 1,
            "Cubic meter (m³)": 1000000
        }
    },


    Speed: {

        SI: {
            "Meter/second (m/s)": 1,
            "Kilometer/hour (km/h)": 1000 / 3600
        },

        CGS: {
            "Centimeter/second (cm/s)": 1,
            "Meter/second (m/s)": 100,
            "Kilometer/hour (km/h)": 100000 / 3600
        }
    },


    Acceleration: {

        SI: {
            "Meter/second² (m/s²)": 1,
            "Centimeter/second² (cm/s²)": 0.01
        },

        CGS: {
            "Centimeter/second² (cm/s²)": 1,
            "Meter/second² (m/s²)": 100,
            "Gal (Gal)": 1
        }
    },


    Force: {

        SI: {
            "Newton (N)": 1,
            "Kilonewton (kN)": 1000,
            "Millinewton (mN)": 0.001
        },

        CGS: {
            "Dyne (dyn)": 0.00001,
            "Newton (N)": 100000,
            "Kilodyne (kdyne)": 0.01
        }
    },


    Pressure: {

        SI: {
            "Pascal (Pa)": 1,
            "Kilopascal (kPa)": 1000,
            "Megapascal (MPa)": 1000000,
            "Bar (bar)": 100000,
            "Atmosphere (atm)": 101325
        },

        CGS: {
            "Barye (Ba)": 0.1,
            "Dyne/cm² (dyn/cm²)": 0.1,
            "Pascal (Pa)": 10
        }
    },


    Energy: {

        SI: {
            "Joule (J)": 1,
            "Kilojoule (kJ)": 1000,
            "Watt-hour (Wh)": 3600,
            "Kilowatt-hour (kWh)": 3600000
        },

        CGS: {
            "Erg (erg)": 0.0000001,
            "Joule (J)": 10000000
        }
    },


    Power: {

        SI: {
            "Watt (W)": 1,
            "Kilowatt (kW)": 1000,
            "Megawatt (MW)": 1000000
        },

        CGS: {
            "Erg/second (erg/s)": 0.0000001,
            "Watt (W)": 10000000
        }
    },


    Frequency: {

        SI: {
            "Hertz (Hz)": 1,
            "Kilohertz (kHz)": 1000,
            "Megahertz (MHz)": 1000000,
            "Gigahertz (GHz)": 1000000000
        },

        CGS: {
            "Hertz (Hz)": 1,
            "Kilohertz (kHz)": 1000,
            "Megahertz (MHz)": 1000000
        }
    },


    Density: {

        SI: {
            "Kilogram/m³ (kg/m³)": 1,
            "Gram/cm³ (g/cm³)": 1000,
            "Gram/liter (g/L)": 1
        },

        CGS: {
            "Gram/cm³ (g/cm³)": 1,
            "Kilogram/m³ (kg/m³)": 0.001,
            "Gram/liter (g/L)": 0.001
        }
    },


    Momentum: {

        SI: {
            "kg·m/s": 1,
            "g·cm/s": 0.00001
        },

        CGS: {
            "g·cm/s": 1,
            "kg·m/s": 100000
        }
    },


    "Charge": {

        SI: {
            "Coulomb (C)": 1,
            "Millicoulomb (mC)": 0.001,
            "Microcoulomb (µC)": 0.000001,
            "Nanocoulomb (nC)": 0.000000001
        },

        CGS: {
            "Coulomb (C)": 1,
            "Statcoulomb (statC)": 2997924580
        }
    },


    Voltage: {

        SI: {
            "Volt (V)": 1,
            "Millivolt (mV)": 0.001,
            "Kilovolt (kV)": 1000
        },

        CGS: {
            "Volt (V)": 1,
            "Millivolt (mV)": 0.001
        }
    },


    Resistance: {

        SI: {
            "Ohm (Ω)": 1,
            "Kiloohm (kΩ)": 1000,
            "Megaohm (MΩ)": 1000000
        },

        CGS: {
            "Ohm (Ω)": 1,
            "Kiloohm (kΩ)": 1000
        }
    },


    Capacitance: {

        SI: {
            "Farad (F)": 1,
            "Microfarad (µF)": 0.000001,
            "Nanofarad (nF)": 0.000000001,
            "Picofarad (pF)": 0.000000000001
        },

        CGS: {
            "Farad (F)": 1,
            "Microfarad (µF)": 0.000001,
            "Nanofarad (nF)": 0.000000001
        }
    },


    Temperature: {

        SI: {
            "Kelvin (K)": 1,
            "Celsius (°C)": 1
        },

        CGS: {
            "Celsius (°C)": 1,
            "Kelvin (K)": 1,
            "Fahrenheit (°F)": 1
        }
    }

};


/*
=========================================================
ELEMENTS
=========================================================
*/

const systemSelect = document.getElementById("system");
const quantitySelect = document.getElementById("quantity");
const valueInput = document.getElementById("value");
const fromUnit = document.getElementById("fromUnit");
const toUnit = document.getElementById("toUnit");
const answer = document.getElementById("answer");
const statusText = document.getElementById("status");


/*
=========================================================
UPDATE UNITS
=========================================================
*/

function updateUnits() {

    const system = systemSelect.value;
    const quantity = quantitySelect.value;

    const list = units[quantity][system];

    fromUnit.innerHTML = "";
    toUnit.innerHTML = "";

    const unitNames = Object.keys(list);

    unitNames.forEach((unit, index) => {

        const option1 = document.createElement("option");
        option1.value = unit;
        option1.textContent = unit;

        const option2 = document.createElement("option");
        option2.value = unit;
        option2.textContent = unit;

        fromUnit.appendChild(option1);
        toUnit.appendChild(option2);

    });

    if (unitNames.length > 1) {
        fromUnit.selectedIndex = 0;
        toUnit.selectedIndex = 1;
    }

    convert();
}


/*
=========================================================
TEMPERATURE CONVERSION
=========================================================
*/

function temperatureToCelsius(value, unit) {

    if (unit.includes("Celsius")) {
        return value;
    }

    if (unit.includes("Kelvin")) {
        return value - 273.15;
    }

    if (unit.includes("Fahrenheit")) {
        return (value - 32) * 5 / 9;
    }

}


function celsiusToTemperature(value, unit) {

    if (unit.includes("Celsius")) {
        return value;
    }

    if (unit.includes("Kelvin")) {
        return value + 273.15;
    }

    if (unit.includes("Fahrenheit")) {
        return (value * 9 / 5) + 32;
    }

}


/*
=========================================================
FORMAT NUMBER
=========================================================
*/

function formatNumber(number) {

    if (!isFinite(number)) {
        return "—";
    }

    if (number === 0) {
        return "0";
    }

    const abs = Math.abs(number);

    if (abs >= 0.0001 && abs < 1000000) {

        return Number(number.toPrecision(10)).toString();

    }

    const exponent = Math.floor(Math.log10(abs));
    const mantissa = number / Math.pow(10, exponent);

    return mantissa.toFixed(3).replace(/\.?0+$/, "")
        + " × 10" + superscript(exponent);

}


/*
=========================================================
SUPERSCRIPT
=========================================================
*/

function superscript(number) {

    const map = {
        "0":"⁰",
        "1":"¹",
        "2":"²",
        "3":"³",
        "4":"⁴",
        "5":"⁵",
        "6":"⁶",
        "7":"⁷",
        "8":"⁸",
        "9":"⁹",
        "-":"⁻"
    };

    return String(number)
        .split("")
        .map(char => map[char] || char)
        .join("");
}


/*
=========================================================
MAIN CONVERSION
=========================================================
*/

function convert() {

    const value = parseFloat(valueInput.value);

    if (isNaN(value)) {

        answer.value = "—";
        statusText.textContent = "Please enter a valid number.";
        return;

    }

    const system = systemSelect.value;
    const quantity = quantitySelect.value;

    const from = fromUnit.value;
    const to = toUnit.value;

    if (!from || !to) {
        return;
    }


    /* Temperature */
    if (quantity === "Temperature") {

        const celsius = temperatureToCelsius(value, from);

        const result = celsiusToTemperature(celsius, to);

        answer.value = formatNumber(result);

        statusText.textContent =
            value + " " + from +
            " = " +
            formatNumber(result) + " " + to;

        return;
    }


    /*
    For all other quantities:

    value → SI base → target unit
    */

    const fromFactor = units[quantity][system][from];

    const toFactor = units[quantity][system][to];


    const siValue = value * fromFactor;

    const result = siValue / toFactor;


    answer.value = formatNumber(result);


    statusText.textContent =
        formatNumber(value) + " " + from +
        " = " +
        formatNumber(result) + " " + to;
}


/*
=========================================================
SWAP
=========================================================
*/

function swapUnits() {

    const temp = fromUnit.value;

    fromUnit.value = toUnit.value;

    toUnit.value = temp;

    convert();
}


/*
=========================================================
CLEAR
=========================================================
*/

function clearValue() {

    valueInput.value = "";

    answer.value = "—";

    statusText.textContent =
        "Enter a value to convert.";

    valueInput.focus();
}


/*
=========================================================
FAVORITE BUTTON
=========================================================
*/

function toggleFavorite() {

    const star = document.querySelector(".star");

    if (star.textContent === "☆") {
        star.textContent = "★";
    } else {
        star.textContent = "☆";
    }

}


/*
=========================================================
EVENTS
=========================================================
*/

systemSelect.addEventListener("change", updateUnits);

quantitySelect.addEventListener("change", updateUnits);

fromUnit.addEventListener("change", convert);

toUnit.addEventListener("change", convert);

valueInput.addEventListener("input", convert);


/*
=========================================================
START APPLICATION
=========================================================
*/

updateUnits();

</script>

</body>
</html>
