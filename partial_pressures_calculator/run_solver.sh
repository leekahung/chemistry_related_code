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
   echo "molecule_and_weight = [(molecule1, mass value 1), (molecule2, mass value 2), ...]"
   echo "weight_type = weight unit"
   echo "total_pressure = pressure value"
   echo "pressure_type = pressure unit"
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
python partial_pressure_calculator.py $RunType
