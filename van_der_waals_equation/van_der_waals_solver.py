"""
Title: Van der Waals Equation for Molar Volume
By: Ka Hung Lee
Date: 4/14/2022
Description: Solves the pressure, temperature, or molar volume of imperfect gas 
             using the van der Waals Equation: p = (R*T)/(V_m - b) - (a/(V_m)^2), 
             where p = pressure, R = Gas Constant, T = temperature, V_m = molar 
             volume, and a and b are particle specific van der Waals coefficients.
             If solves for perfect gas, a and be would be set to 0.

             For temperature, T = ((p + (a/(V_m)^2)) * (V_m - b))/R

             For molar volume, V_m is derived from the cube root of:
             (V_m)^3 - (b + ((R*T)/p)) * (V_m)^2 + (a/p) * V_m - (a*b)/p = 0, which 
             is derived directly from the van der Waals Equation, where the root 
             that does not contain an imaginary component being the true molar 
             volume.

             The Gas Constant used here is in units of dm^3 atm K^-1 mol^-1,
             or 8.20574 * 10^-2 dm^3 atm K^-1 mol^-1. 
"""
# Import Dependencies
import numpy as np
import sys
import os
import re

# Inputs from Bash Script
run_type = sys.argv[1]

# Gas Constant
R_gc = 8.20574 * (10**-2)

# Function to convert and collect variables
def get_digits(variable_string):
    digits = re.findall(r"[0-9\.]+", variable_string)[0]
    return float(digits)

def variable_conversion(variable):
    if variable == 'na':
        return variable
    else:
        if isinstance(variable, list) == True:
            if variable[-1][-1] == 'K':
                variable = float(variable[0])
            elif variable[-1][-1] == 'C':
                variable = float(variable[0]) + 273.15
            elif variable[-1][-1] == 'F':
                variable = ((float(variable[0]) - 32) * (9/5)) + 273.15
            elif variable[-1][-1] == 'm':
                variable = float(variable[0])
            elif variable[-1][-1] == 'a':
                variable = float(variable[0]) / 101325
            elif variable[-1][-2:] == 'ar':
                variable = (float(variable[0]) * (10**5)) / 101325
            elif variable[-1][-2:] == 'rr':
                variable = float(variable[0]) / 760
        else:
            if variable[-1] == 'K':
                variable = get_digits(variable)
            elif variable[-1] == 'C':
                variable = get_digits(variable) + 273.15
            elif variable[-1] == 'F':
                variable = ((get_digits(variable) - 32) * (9/5)) + 273.15
            elif variable[-1] == 'm':
                variable = get_digits(variable)
            elif variable[-1] == 'a':
                variable = get_digits(variable) / 101325
            elif variable[-2:] == 'ar':
                variable = (get_digits(variable) * (10**5)) / 101325
            elif variable[-2:] == 'rr':
                variable = get_digits(variable) / 760
        return variable

def get_variables(run_type):
    if run_type.lower() == 'interactive':
        system_type = input("Perfect gas or real gas? ")
        Temp = input("Temperature (in F, C, or K) or na if not given: ")
        p = input("Pressure (in atm, Pa, bar, or torr) or na if not given: ")
        a = input("a coefficient (in atm dm^6 mol^-2): ")
        b = input("b coefficient (in dm^3 mol^-1): ")
        V_m = input("Molar Volume (in dm^3) or na if not given: ")

        if system_type.lower() == 'perfect gas' or system_type.lower() == 'perfect':
            a = 0.0
            b = 0.0
            Temp = variable_conversion(Temp)
            p = variable_conversion(p)
            if V_m != 'na':
                V_m = float(V_m)

            return Temp, p, a, b, V_m
        else:
            Temp = variable_conversion(Temp)
            p = variable_conversion(p) 
            if V_m != 'na':
                V_m = float(V_m)

            return Temp, p, a, b, V_m
    else:
        curr_dir = os.getcwd()
        filename = os.path.join(curr_dir, "input_file.txt")
        file_inputs = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                input_line = line.split()
                if input_line[-1].isalpha() == True and len(input_line) > 3:
                    file_inputs.append(input_line[-2:])
                else:
                    file_inputs.append(input_line[-1])
        
        if file_inputs[0].lower() == 'perfect gas' or file_inputs[0].lower() == 'perfect': 
            Temp = variable_conversion(file_inputs[1])
            p = variable_conversion(file_inputs[2])
            a = 0.0
            b = 0.0
            V_m = file_inputs[5]
            if V_m != 'na':
                V_m = float(V_m)
        else:
            Temp = variable_conversion(file_inputs[1])
            p = variable_conversion(file_inputs[2])
            a = float(file_inputs[3])
            b = float(file_inputs[4])
            V_m = file_inputs[5]
            if V_m != 'na':
                V_m = float(V_m)
    
    #Debug routine (comment out in production)
    #print(Temp, p, a, b, V_m)

    return Temp, p, a, b, V_m

# Functions for solver
def solve_pressure(Temp, a, b, V_m):
    """ Fuction solves for pressure """
    return ((R_gc * Temp)/(V_m - b)) - (a/(V_m**2))

def solve_temperature(p, a, b, V_m):
    """ Function solves for temperature """
    return ((p + (a/(V_m**2))) * (V_m - b))/R_gc

def solve_molar_volume(p, Temp, a, b):
    """ Function solves for molar volume """
    coeff_list = [1, -(b + ((R_gc*Temp)/p)), (a/p), -((a*b)/p)]
    roots_list = np.roots(coeff_list)
    real_value = roots_list.real[abs(roots_list.imag)<1e-5] 

    return round(real_value[0], 6)

def run_solver(Temp, p, a, b, V_m):
    if isinstance(p, str) == True:
        solver = 'Pressure'
        result = solve_pressure(Temp, a, b, V_m)
        units = 'atm'
    elif isinstance(Temp, str) == True:
        solver = 'Temperature'
        result = solve_temperature(p, a, b, V_m)
        units = 'K'
    else:
        solver = 'Molar Volume'
        result = solve_molar_volume(p, Temp, a, b)
        units = "dm^3 mol^-1"

    return solver, result, units

# Run Solver
Temp, p, a, b, V_m = get_variables(run_type)

# Debug Routines (comment out in production)
#print(Temp, p, a, b, V_m)
#for ele in [Temp, p, a, b, V_m]:
#    print(type(ele))

solver, result, units = run_solver(Temp, p, a, b, V_m)

print("---------------------------")
print(f"Solving for {solver}")
print(f"{solver}: {result} {units}")
