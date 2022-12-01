# %%
# https://adventofcode.com/2022/day/1

# %%
# Imports
import pandas as pd
import numpy as np

# %%
# Part one
# Which elf is carrying the most calories?
# https://adventofcode.com/2022/day/1

# Read data
filename = "./../Data/day1_input.txt"

data = pd.read_csv(filename,
                   sep="\t",
                   header=None,
                   names=["Calories"],
                   skip_blank_lines=False)

# %%
# Split out data for each elf
elf_list = np.split(data, data[data.isnull().all(1)].index)

df = pd.DataFrame()

for i in range(len(elf_list)):
    tmp = pd.DataFrame(columns=["Calories", "Elf"])
    tmp["Calories"] = elf_list[i].squeeze().tolist()
    tmp["Elf"] = i
    df = pd.concat([df, tmp])
    
df = df.dropna()
df = df.reset_index(drop=True)

# %%
# Work out the total calories for each elf
total_calories = df.groupby(by = ["Elf"]).sum()
most_calories = total_calories["Calories"].max()
most_calories

# %%
# Part two
# How many calories are the three elves carrying the most calories carrying?
# https://adventofcode.com/2022/day/1#part2

top3_total_calories = total_calories.sort_values(by="Calories", ascending = False).head(3).sum()
top3_total_calories
# %%
