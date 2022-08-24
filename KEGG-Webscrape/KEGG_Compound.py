import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
from random import randint



# This the URL of interest for the KEGG compound dataset. C must be used.
# Creating empty lists for later use. 
# l[] will store all the data.

KEGG_url = "https://www.genome.jp/entry/C"
list_KEGG = []
C_list_KEGG = []
l = []

# creating a list of numbers. KEGG uses a number system for their compound webpages. 
# Consists of https://www.genome.jp/entry/C PLUS a 5 digit number that includes the 0s. 
# For example https://www.genome.jp/entry/C00005. 
for i in range(1, 25000):
    C_list_KEGG.append('{0:05}'.format(i))

# looping though all possible numbers combinations (99,999 of them) to find webpages.

for page in C_list_KEGG:

    # Printing where in the process the program is.
    print(KEGG_url+str(page))

    # At first the program will try to access the webpage. If the webpage is not present (C05555 does not 
    # exist for example), the program will pass on this number and try the next. 
    try:

        # Requesting the webpage.
        r1 = requests.get(KEGG_url+str(page))

        # Making it readable for us. 
        c1 = r1.content
        soup = BeautifulSoup(c1, "html.parser")

        # Specifying where to look. Most of the data wanted is stored in the <div class:cel>.

        all = soup.find_all("div", {"class": "cel"})

        # Using a while loop so we can stay the program as long as loop_state is True. Can change this if there
        # is an undesired outcome. 
        loop_state = True

        while loop_state:

            # Creating a dictionary for each compound. This stores the information.
            d = {}

            # Retrieves the compound number from KEGG.
            compound_number = soup.find_all("span", {"class": "nowrap"})
            d["Compound_Number"] = compound_number[1].text.replace("\xa0","").replace("\n","").replace("Compound","")

            # Retrieves the name of the compound
            d["Name"] = all[1].text.replace("\n"," ")

            # Retrieves chemical formula for compound
            d["Formula"] = all[2].text.replace("\n","")

            # Some compounds in the database are generalized. That is to say, contain an R group.
            # Is is present on repeating structures, lipids, etc. When this occurs, the webpage 
            # changes structure and therefore we need to check if there is an R group.
            formula = all[2].text.replace("\n","")

            # Naming variables.
            d["Exact_mass"] = "None"
            d["Molecular_weight"] = "None"

            # An R group will first be present in the formula so we will check that now. 
            # If there is no R, add masses. 
            if not bool(re.search('([R])', formula)):
                d["Exact_mass"] = all[3].text.replace("\n","")
                d["Molecular_weight"] = all[4].text.replace("\n","")
                
            # When there is an R...
            else:
                # No mass can be added. Skip this step.
                pass

            # Adding the various database numbers. It is stored differently from the above 
            # so changing what data is accessed. 
            links = soup.find_all("table", {"class": "w1"})

            # This for loop checks for the major databases of interest. When found the information
            # is added. Otherwise there is a blank spot.
            for i in range(0,len(links)):

                if "CAS" in links[i].text.replace("\xa0",""):
                    d["CAS"] = links[i].text.replace("CAS:\xa0","")
            
                if "PubChem" in links[i].text.replace("\xa0",""):
                    d["PubChem"] = links[i].text.replace("PubChem:\xa0","")
                
                if "ChEBI" in links[i].text.replace("\xa0",""):
                    d["ChEBI"] = links[i].text.replace("ChEBI:\xa0","").replace(" ", ";")
                
                if "KNApSAcK" in links[i].text.replace("\xa0",""):
                    d["KNApSAcK"] = links[i].text.replace("KNApSAcK:\xa0","")
                
                if "PDB-CCD" in links[i].text.replace("\xa0",""):
                    d["PDB-CCD"] = links[i].text.replace("PDB-CCD:\xa0","").replace(" ", ";")
                
                if "NIKKAJI" in links[i].text.replace("\xa0",""):
                    d["NIKKAJI"] = links[i].text.replace("NIKKAJI:\xa0","").replace(" ", ";")
                
                if "LIPIDMAPS" in links[i].text.replace("\xa0",""):
                    d["LIPIDMAPS"] = links[i].text.replace("LIPIDMAPS:\xa0","")
                
                if "3DMET" in links[i].text.replace("\xa0",""):
                    d["3DMET"] = links[i].text.replace("3DMET:\xa0","").replace(" ", ";")
                


            # The mol file is stored on a different webpage. Same process as before with the new webpage.
            mol_url = "https://www.genome.jp/entry/-f+m+C"
            
            print(mol_url+str(page))
            r2 = requests.get(mol_url+str(page))
            c2 = r2.content
            soup = BeautifulSoup(c2, "html.parser")
            # Something to note is that some compounds do not have mol file. They will just be stored as blanks.
            # A space is added to the front to make the final import readable.
            d["Mol"] = " " + soup.text.strip()

            # Storing the dictionary into a list.
            l.append(d)
            
            # Waiting about 10 seconds so I do not get blocked.
            time.sleep(randint(7.5,12.5))

            # Ending the while loop.
            loop_state = False

    except:
        pass

# Converting the list to a data frame and saving as csv.

df = pd.DataFrame(l)
df.to_csv("KEGG_Compound_Database.csv")
