"""
Pandas kütüphanesinde DataFrame çalışması
"""

import pandas as pd

s1 = pd.Series([3, 2, 0, 1])
s2 = pd.Series([0, 3, 7, 2])

data_list = dict(apples=s1, oranges=s2)

df = pd.DataFrame(data_list)

print(data_list)
print("-" * 75)

####################################################################################################

data_list = [["Utku", 100], ["Mert", 50], ["Malman", 30], ["Denizhan", 75]]
data_dict = {"Name": ["Utku", "Mert", "Malman", "Denizhan"], "Grade": [100, 50, 30, 75]}
dict_list = [
    {"Name": "Utku", "Grade": 100},
    {"Name": "Mert", "Grade": 50},
    {"Name": "Malman", "Grade": 30},
    {"Name": "Denizhan", "Grade": 75},
]


df_list = pd.DataFrame(
    data_list,
    columns=["Name", "Grade"],
    index=[1, 2, 3, 4],
)  # Belirtmezsen ilkini index alır

df_list["Grade"] = df_list["Grade"].astype(float)  # Float böyle çevriliyor

print((df_list))
####################################################################################################
df_dict = pd.DataFrame(data_dict, index=[356, 1010, 810, 245])

print(df_dict)
####################################################################################################

df_dict_list = pd.DataFrame(dict_list, index=[356, 1010, 810, 245])
print(df_dict_list)
