'''
Title: Molecular Weight Solver
By: Ka Hung Lee
Date: 04/12/2022
Description: Simple Python code to calculate molecular weight of the chemical formula given.
'''

# Importing Dependencies
import pandas as pd
import re

# Loading table of elements and atomic mass
periodic_df = pd.read_csv('iupac_2019_atomic_weights.csv', header=None)
column_names = ['atomic_number', 'element_symbol', 'element_name', 'atomic_mass']
periodic_df.columns = column_names
periodic_df.set_index('element_symbol', inplace=True)

# Dynamic user-input for solver
molecule = input("Enter chemical formula here (if water of hydration exist, preceed number with '.', i.e. MgSO4.7H2O): ")

# Functions for solver
def molecular_groups_weight(molecule):
    """ Function checks for and isolates molecular groups and their counts in formula"""
    # Check for molecular groups in formula
    groups_list = re.findall(r"\(\w+\)\d?", molecule)
    
    # Isolate molecular groups into componenets
    molecule_groups = []
    for group in groups_list:
        molecule_group = re.findall(r"\w+", group)
        if len(molecule_group) == 1:
            molecule_group.append('1')
            molecule_groups.append(molecule_group)
        else:
            molecule_groups.append(molecule_group)
    
    molecular_group_formulas = []
    molecular_group_counts = []
    for group in molecule_groups:
        molecular_group_formulas.append(molecule_group[0])
        molecular_group_counts.append(molecule_group[1])

    # Remove groups from formula
    remaining_molecule = re.sub(r"\(\w+\)\d?", '', molecule) 

    # Debug routines (comment out in production)
    #print(molecular_group_formulas)
    #print(molecular_group_counts)
    #print(remaining_molecule)

    return remaining_molecule, molecular_group_formulas, molecular_group_counts

def detach_water_of_hydration(molecule):
    """ Function serach for water of hydration if exist and detach it from formula"""
    water_of_hydration = 0
    if '.' in molecule:
        water_of_hydration_formula = re.findall(r"(?<=\.).*", molecule)[0]
        if water_of_hydration_formula[0].isnumeric() == True:
            water_of_hydration = re.findall(r".*(?=H2O)", water_of_hydration_formula)[0]
        else:
            water_of_hydration = 1
        
        water_removed = re.sub(r"\.\w+", '', molecule)

        # Debug routines (comment out in production)
        #print(water_of_hydration_formula)
        #print(water_of_hydration)
        #print(water_removed)

        return water_of_hydration, water_removed
    
    else:
        return water_of_hydration, molecule

def molecular_weight(molecule):
    """ Function computes molecular weight of given chemical formula"""
    # Check if molecule is just a single letter element
    if len(molecule) == 1:
        return periodic_df.loc[molecule, 'atomic_mass']

    # Routine to break molecule into parts for calculation
    else:
        elements_list = re.findall(r"[A-Z][a-z]?\d*", molecule)
        for i, component in enumerate(elements_list):
            if component.isalpha() == True:
                elements_list[i] = component + '1'

        # Routine to calculate total mass from components
        mass_list = []
        for element in elements_list:
            ele = re.findall(r"[a-zA-Z]+", element)[0]
            ele_count = re.findall(r"\d+", element)[0]
            mass_list.append(periodic_df.loc[ele, 'atomic_mass'] * float(ele_count))

        # Debug routines (comment out in production)
        #print(mass_list)
        #print(elements_list)        
        
        return sum(mass_list)

def total_mass_solver(molecule):
    """ Function separates groups and computes mass all components before summing them together"""
    water_of_hydration, water_removed = detach_water_of_hydration(molecule)
    remaining_molecule, molecular_group_weights, molecular_group_counts = molecular_groups_weight(water_removed)

    # Mass from hydration
    water_mass = periodic_df.loc['H', 'atomic_mass'] * 2.0 + periodic_df.loc['O', 'atomic_mass']
    total_mass_hydration = float(water_of_hydration) * water_mass

    mass_components = []
    if len(molecular_group_weights) != 0:
        for group_weight, group_count in zip(molecular_group_weights, molecular_group_counts):
            mass_components.append(molecular_weight(group_weight) * float(group_count))

    return sum(mass_components) + molecular_weight(remaining_molecule) + total_mass_hydration

total_mass = total_mass_solver(molecule)

print(f"Total Molecular Weight (in amu): {total_mass:.2f}")
