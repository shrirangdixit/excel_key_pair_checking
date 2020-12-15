# impoting labraries

import numpy as np
import pandas as pd
import json

# Load the data
sheet_1 = pd.read_excel('Sheet1.xlsx')
sheet_2 = pd.read_excel('Sheet2.xlsx')


def correctness(sheet_1, sheet_2):
    correct_name_count = 0
    correct_DOB_count = 0
    correct_key_value_pair = 0
    for i in range(sheet_1.shape[0]):
            if str(sheet_1['Name'].iloc[i]).strip().lower() == str(sheet_2['Name'].iloc[i]).strip().lower() :
                correct_name_count += 1
            if str(sheet_1['DOB'].iloc[i]).strip().lower() == str(sheet_2['DOB'].iloc[i]).strip().lower():
                correct_DOB_count += 1
            if (str(sheet_1['Name'].iloc[i]).strip().lower() == str(sheet_2['Name'].iloc[i]).strip().lower()) and (str(sheet_1['DOB'].iloc[i]).strip().lower() == str(sheet_2['DOB'].iloc[i]).strip().lower()):
                correct_key_value_pair += 1
                
    results = {'Number of correct name': correct_name_count,'Number of date of birth':correct_DOB_count,
            "Number of correct key value pair": correct_key_value_pair}
    return results


#saving the results in json file

with open('results.json','w') as json_file:
    json.dump(correctness(sheet_1, sheet_2),json_file)
   