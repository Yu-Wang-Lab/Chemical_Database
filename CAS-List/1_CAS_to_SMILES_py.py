# Importing required packages.

import cirpy
import pandas as pd
import csv

# Loading the data. This package cannot handle 
# large datasets. Therefore I must break the 
# datasets into smaller pieces. This is not 
# dependent on the computational power available.
#  It seems to time out if taking too long.  
# About 500 data points should be sufficiently small. 

# Loading data.
Just_CAS_csv = pd.read_csv(r"0_TEST_CAS_List.csv")

# Making a list of just CAS numbers from File.
Just_CAS_list = Just_CAS_csv["CAS"].values.tolist()

# Removing any empty spaces for ease of processing.
CAS_data = [i.replace(" ", "") for i in Just_CAS_list]

# Splitting the data set into smaller pieces.

first_CAS_data = CAS_data[0:500]
second_CAS_data = CAS_data[500:1000]
third_CAS_data = CAS_data[1000:1500]
fourth_CAS_data = CAS_data[1500:2000]
fifth_CAS_data = CAS_data[2000:2500]
sixth_CAS_data = CAS_data[2500:3000]
seventh_CAS_data = CAS_data[3000:3500]
eighth_CAS_data = CAS_data[3500:3974]


# Function that converts to smiles.

def CAS_to_SMILES(CAS):

    """
    The purpose of this function is to take a CAS number and convert it into a SMILES string.
    In order for this function to work there must be an internet connection.

    Args:
        CAS: This can be either a singe string of CAS numbers or a list of strings.
        
    Returns:
        A data frame will be returned that has a column headers of the original CAS number
        and the resolved SMILES.

    Important Notes:
        If something that is entered is not a CAS number it will still add the CAS number to
        the data frame but the SMILES will be blank. 

    Time:
        This takes me 68 minutes to work on 4000 values. 

    """
    
    # Creating an empty list to store the data for later.
    CAS_list = []
    SMILES_list = []

    for i in CAS:

        # Adds a ' to the end as some CAS numbers will be converted into dates on excel.
        CAS_list.append(i + "'")
        SMILES_list.append(cirpy.resolve(i, "smiles"))
        


    df = pd.DataFrame({"CAS": CAS_list, "SMILES": SMILES_list})
    return df

# Running function on data.

part_1 = CAS_to_SMILES(first_CAS_data)
print("1 done")
part_2 = CAS_to_SMILES(second_CAS_data)
print("2 done")
part_3 = CAS_to_SMILES(third_CAS_data)
print("3 done")
part_4 = CAS_to_SMILES(fourth_CAS_data)
print("4 done")
part_5 = CAS_to_SMILES(fifth_CAS_data)
print("5 done")
part_6 = CAS_to_SMILES(sixth_CAS_data)
print("6 done")
part_7 = CAS_to_SMILES(seventh_CAS_data)
print("7 done")
part_8 = CAS_to_SMILES(eighth_CAS_data)
print("8 done")

# Concatenating the data together and saving it to a csv.

df_concat = pd.concat([part_1, part_2, part_3, part_4, part_5, part_6, part_7, part_8], axis=0)
df_concat.to_csv("TEST_CAS_and_SMILES.csv", index= False)