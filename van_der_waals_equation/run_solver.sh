#!/bin/bash

# Help
Help()
{
   # Display Help
   echo "Script flags for run_solver script."
   echo
   echo "Syntax: bash run_solver.sh [-h|r]"
   echo "options:"
   echo "-h     Print this Help."
   echo "-r     Run type."
   echo
   echo "Input file syntax:"
   echo "system_type = perfect or real"
   echo "Temp = temperature value or na"
   echo "p = pressure value or na"
   echo "a = a coefficient, van der Waals or 0 if perfect gas"
   echo "b = b coefficient, van der Waals or 0 if perfect gas"
   echo "V_m = molar volume value or na"
   echo
}

# Main Peogram

# Set variables
RunType="interactive"

# Get options
while getopts ":hr:" option; do
    case $option in
        h) # display Help
           Help
           exit;;
        r) # Enter run type
           RunType=$OPTARG;;
        \?) # Invalid option
           echo "Error: Invalid option"
           exit;;
    esac
done

# Main Program
# Set variables
echo "Run Type: ${RunType^}"
python van_der_waals_solver.py $RunType
