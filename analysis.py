import numpy as np
import pandas as pd
import matplotlib as plt

heights_df = pd.read_excel('data\Heights.xlsx')

print(heights_df.describe())
