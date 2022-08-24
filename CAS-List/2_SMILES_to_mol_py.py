# RDKit needs an environment to run properly. If not done already, setup steps are below.

# Open Anaconda Prompt and run the following line of code.
# conda create -c conda-forge -n my-rdkit-env rdkit
# When running it for the first time this will prompt you to update some packages.

# Go to https://www.rdkit.org/docs/Install.html for the best advice.

# Importing packages needed.

from rdkit import Chem
from rdkit.Chem.rdMolDescriptors import CalcMolFormula
import pandas as pd
import csv

# Creating a function that will convert the SMILES 
# to a MOL object, then get formula, 
# molecular weight (MW), and MOL file. 

def input_SMILES_list_here(SMILES):
    """
    The purpose of this function is to take a SMILES string and convert it into a chemical formula,
    an exact molecular weight, and a MOL file string.

    Args:
        SMILES: This can be either a singe string of SMILES numbers or a list of strings.

    Returns:
        A data frame will be returned that has a column headers of the original SMILES value,
        the chemical formula, the exact MW, and the MOL file.

    Important Notes:
        If something that is entered is not a SMILES it will still add to the data frame.
        The formula, etc. will have values of NaN.

    Time:
        This takes me ~5 seconds to work on 4000 values. 
    """

    # Creating an empty list to store the data for later.
    SMILES_list = []
    formula_list = []
    exactMW_list = []
    MOL_file_list = []
    

    for i in SMILES:

        # For each SMILE, it will attempt to convert the SMILE to a MOL "object". If
        # it fails then the values for formula etc. will be NaN. If successful, the 
        # MOL "object" is converted to formula etc. 
        try:

            SMILES_list.append(i)
            smile_to_mol_object = Chem.MolFromSmiles(i)
            formula_list.append(CalcMolFormula(smile_to_mol_object))
            exactMW_list.append(Chem.rdMolDescriptors.CalcExactMolWt(smile_to_mol_object))
            MOL_file_list.append(str(Chem.MolToMolBlock(smile_to_mol_object)))

        except:
            
            formula_list.append("NaN")
            exactMW_list.append("NaN")
            MOL_file_list.append("None")
        
    df = pd.DataFrame({"SMILES": SMILES_list, "Formula": formula_list, "Exact_MW": exactMW_list, "MOL": MOL_file_list})
    return df


# Loading Data

CAS_SMILES = pd.read_csv("TEST_CAS_to_SMILES.csv", header = None)
just_smiles = CAS_SMILES[1]

# Running the function on the data.

SMILES_to_MOL_df = input_SMILES_list_here(just_smiles)


# Cleaning and saving the data. For some reason I cannot get this to work in the function so it
#  must be a separate step for now. 

SMILES_to_MOL_df["MOL"] = SMILES_to_MOL_df["MOL"].str.strip()
SMILES_to_MOL_df["MOL"] = SMILES_to_MOL_df["MOL"].str.replace("RDKit          2D\n\n ", " ")
# Saving the data frame.
SMILES_to_MOL_df.to_csv("TEST_SMILES_formula_MW_MOL.csv", index = False)