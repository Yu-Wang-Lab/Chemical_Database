# Starting with a list of CAS numbers.

The code here can taka list of CAS numbers, convert them into SMILES. Output an excel file with the CAS and SMILES. This information can be
used to convert the SMILES into chemical formula, exact molecular weight, and a MOL file. 

## Instructions

Assuming you have downloaded the code and installed the dependencies.
Create a list of CAS numbers in a single column in a CSV file. The first row should be "CAS".
Open 1_CAS_to_SMILES.ipynb and change the file name as needed. 
If you have more than 500 CAS numbers it needs to be broken into smaller sub files to prevent a time-out error. This is done already
but you may need to change the specifica numbers. 
Run the function and save the CSV file.
Run 2_SMILES_to_MOL.ipynb. CHange file names as needed.
Once the environment is properly set up all that needs to be done is to run the file.
Run function and save the CSV.

## Dependencies

You will need to install:
cirpy
rdkit*
pandas

rdkit needs its own environment and therefore is treated seperatly.


## Installation

Use conda and/or pip to install dependencies. rdkit specifically needs  conda. 

## Usage

Convert a list of CAS numbers to SMILES.
Convert a list of SMILES to chemical fomula, molecular weight, and mol files. 
Export all this information to excel.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
