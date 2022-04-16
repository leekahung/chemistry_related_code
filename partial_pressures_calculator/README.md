# Partial Pressure Calculator

Usage: bash run_solver.sh -r <"interactive"|"file">
Output: Component Name and partial pressure of component in atmospheres.

Usage help: bash run_solver.sh -h
Output: Syntax for bash script and python inputs.

A simple Python code that computes partial pressures of gases given the total\
pressure of their surroundings and their mass. It utilizes another code,\
molecular_weight_solver.py, to calculate molecular weights for determining the\
mole fraction of components.

- Check [molecular weight calculator](https://github.com/leekahung/molecular_weight_calculator) for reference

Input currently accepts inputs that works for the molecular weight calculator\
in terms of gases/components, masses in grams or kilograms, and pressures in\
atmospheres, pascals, bars, and torrs.

# Validation Test
<h2>Test Case #1:</h2>
- N2: 75.5g
- O2: 23.2g
- Ar: 1.3g
- Total Pressure: 1 atm

- Partial Pressures to same significant figure:
- N2: (Expected) 0.780 atm, (Calculated) 0.781 atm
- O2: (Expected) 0.210 atm, (Calculated) 0.210 atm
- Ar: (Expected) 0.0096 atm, (Calcualted) 0.0094 atm

<h2>Test Case #2:</h2>
- N2: 75.52g
- O2: 23.15g
- Ar: 1.28g
- CO2: 0.046g
- Total Pressure: 0.900 atm

- Partial Pressures to the same significant figure:
- N2: (Expected) 0.703 atm, (Calculated) 0.703 atm
- O2: (Expected) 0.189 atm, (Calculated) 0.189 atm
- Ar: (Expected) 0.0084 atm, (Calculated) 0.0084 atm
- CO2: (Expected) 0.00027 atm, (Calculated) 0.00027 atm
