import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('crime.csv', encoding = "windows-1252")

SimpleDF = df.to_json()