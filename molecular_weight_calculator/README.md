# Molecular Weight Calculator

Usage: python molecular_weight_solver.py

A simple Python code that computes molecular weights from chemical formulas. It\
currently derives its mass using IUPAC's 2019 atomic weight standard.

- Check out [IUPAC website](https://iupac.qmul.ac.uk/AtWt/) for reference

Existing code accounts for water of hydration in the formula if included. The\
dot notation used for denoting water of hydration can be typed as a "." in the\
formula. Example input: MgSO4.7H2O

Partial water of hydration, i.e. hemihydrates, could also be computed. Example\
input: CaSO4.0.5H2O

The code also accounts for molecular sub-groups in formula too, typically\
denoted within parentheses. Example input: PtCl2(NH3)2

The code could not account for at this time molecular groups within groups, i.e.\
nested groups (for example: Co3(Fe(CN)6)2).

The accepted input characters for the code includes alphanumeric strings with\
or without "." and parenthesis, (), as depicted above.

# Validation Test

<h2>Test Cases:</h2>

(element/molecule/compound name) name\
Expected: in amu - Calculated: in amu

Expected values were derived by hand using atomic weights from IUPAC 2019.\
Calculated values were computed using the code (molecular_weight_solver.py).

<h2>Chemical formula without "." or ()</h2>

(Carbon) C\
Expected: 12.01 - Calculated: 12.01

(Hydrogen cyanide or Hydrocyanic acid) HCN\
Expected: 27.03 - Calculated 27.03

(Water) H2O\
Expected: 18.02 - Calculated: 18.02

(Benzene) C6H6\
Expected: 78.11 - Calculated: 78.11

(Sodium chloride) NaCl\
Expected: 58.44 - Calculated: 58.44

(Thiamine hydrochloride) HC12H17ON4SCl2\
Expected: 337.26 - Calculated: 337.26

(Titin or connectin) C169719H270466N45688O52238S911\
Expected: 3816038.88 - Calculated: 3816038.88

<h2>Chemical formula with ()</h2>

(Aluminum hydroxide) Al(OH)3\
Expected: 78.00 - Calculated: 78.00

(Acrylonitrile) H2C(CH)CN\
Expected: 53.06 - Calcualted: 53.06

(Dichlorodiammineplatinum or DDP) PtCl2(NH3)2\
Expected: 300.05 - Calculated: 300.05

(Triphenylphosphine) (C6H5)3P\
Expected: 262.28 - Calculated: 262.29

(Calcium metaniobate) Ca(NbO3)2\
Expected: 321.89 - Calculated: 321.89

(Cobalt(II) ferricyanide) Co3(Fe(CN)6)2\
Expected: 600.71 - Calculated: 388.75 - Error! (Couldn't compute groups correctly)

<h2>Cases with water of hydration</h2>

(Magnesium sulfate heptahydrate or Epsomite) MgSO4.7H2O\
Expected: 246.47 - Calculated: 246.47

(Lithium nitrate monohydrate) LiNO3.H2O\
Expected: 86.96 - Calculated: 86.96

(Calcium sulfate hemihydrate or Plaster of Paris) CaSO4.0.5H2O\
Expected: 145.14 - Calculated: 145.14

<h2>Cases with both () and water of hydration</h2>

(Calcium nitrate) Ca(NO3)2.4H2O\
Expected: 236.15 - Calculated: 236.15

(Barium bromate monohydrate) Ba(BrO3)2.H2O\
Expected: 411.14 - Calculated: 411.14

(Indium(III) sulfate monohydrate) In2(SO4)3.H2O\
Expected: 535.82 - Calculated: 535.82
