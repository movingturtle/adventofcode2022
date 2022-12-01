# %%
# https://adventofcode.com/2022/day/1

# %%
# Imports
import pandas as pd
import numpy as np

# %%
# Read data
filename = "./../../../Aisling Spain/OneDrive - MCG Services Limited/Documents/day1_input.txt"

data = pd.read_csv(filename,
                   sep="\t",
                   header=None,
                   names=["Calories"],
                   skip_blank_lines=False)

elf_list = np.split(data, data[data.isnull().all(1)].index)

df = pd.DataFrame()

for i in range(len(elf_list)):
    tmp = pd.DataFrame(columns=["Calories", "Elf"])
    tmp["Calories"] = elf_list[i].dropna().squeeze().tolist()
    tmp["Elf"] = i
    df = pd.concat([df, tmp])

df = df.reset_index()
df.groupby(by = ["Elf"]).sum()
