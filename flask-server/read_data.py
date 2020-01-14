import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('crime.csv', encoding = "windows-1252")

df_head_INCIDENT_NUMBER = df['OFFENSE_CODE'].head(90).to_json()
df_head = df.head(90).to_json()