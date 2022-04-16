'''
Title: Partial Pressure Calculator
By: Ka Hung Lee
Date: 04/14/2022
Description: Simple Python code to calculate partial pressures of molecules
             given their mass and total pressure of surroundings.
'''
# Import Dependencies
from molecular_weight_solver import total_mass_solver
import sys
import os

# Inputs from Bash Script
run_type = sys.argv[1]

# Function to get variables
def get_variables(run_type):
    if run_type.lower() == "interactive":
        molecule_and_weight = input("Insert input as a tuple in a Python List (i.e. [('N2', 75.52), ('O2', 23.15), etc.])")
        weight_type = input("Input weight units (g or kg): ")
        total_pressure = input("Input total pressure: ")
        pressure_type = input("Input pressure units (atm, Pa, torr, or barr): ")
    else:
        curr_dir = os.getcwd()
        filename = os.path.join(curr_dir, "input_file.txt")
        file_inputs = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                input_line = line.split()
                file_inputs.append(input_line[2])
        
        molecule_and_weight = list(eval(file_inputs[0]))
        weight_type = file_inputs[1]
        total_pressure = float(file_inputs[2])
        pressure_type = file_inputs[3]

    # Debug routines (comment out in production)    
    #print(molecule_and_weight, weight_type, total_pressure, pressure_type)

    return molecule_and_weight, weight_type, total_pressure, pressure_type

# Functions for calculator
def weight_conversion(weight_type, molecule_and_weight):
    """ Function converts weight units into grams """
    molecule_only = [molecule[0] for molecule in molecule_and_weight]
    if weight_type.lower() == "g":
        pass
    elif weight_type.lower() == "kg":
        for molecule in molecule_and_weight:
            temp = molecule[1] * 1000
            molecule[1] = temp
    else:
        print("Please enter as g or kg")
    
    return molecule_and_weight, molecule_only

def pressure_conversion(pressure_type, total_pressure):
    """ Function converts pressure units into atmospheres """
    if pressure_type.lower() == "atm":
        pass
    elif pressure_type.lower() == "pa":
        temp = total_pressure / 101325
        total_pressure = temp
    elif pressure_type.lower() == "bar":
        temp = total_pressure * 10**5 / 101325
        total_pressure = temp
    elif pressure_type.lower() == "torr":
        temp = total_pressure / 760
        total_pressure = temp

    return total_pressure

def compute_moles(molecule_and_weight):
    """ Computes number of moles for each component in gas mixture """
    moles = []
    sig_figs = []
    for molecule in molecule_and_weight:
        molecular_mass = total_mass_solver(molecule[0])
        mass = molecule[1]
        mole = mass/molecular_mass
        moles.append(mole)
    
    return moles

def compute_partial_pressures(weight_type, molecule_and_weight, pressure_type, total_pressure):
    """ Function computes for partial pressures from moles of components and total pressure """
    cleaned_molecule_and_weight, molecule_only = weight_conversion(weight_type, molecule_and_weight)
    total_pressure = pressure_conversion(pressure_type, total_pressure)
    moles = compute_moles(cleaned_molecule_and_weight)

    total_moles = sum(moles)
    mole_fractions = [mole/total_moles for mole in moles]

    partial_pressures = [round(mole*total_pressure, 6) for mole in mole_fractions]
    partial_pressures_molecule = list(zip(molecule_only, partial_pressures, moles, mole_fractions))

    return partial_pressures_molecule

# Run Solver
molecule_and_weight, weight_type, total_pressure, pressure_type = get_variables(run_type)
results = compute_partial_pressures(weight_type, molecule_and_weight, pressure_type, total_pressure)

for result in results:
    print(f"Component: {result[0]}")
    print(f"Moles (in mol): {result[2]:.6f}")
    print(f"Mole Fraction: {result[3]:.6f}")
    print(f"Partial Pressure (in atm): {result[1]}")
