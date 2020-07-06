import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Define relative path to file
file_path = "D:/Research/DataSets/Market Indices Daily.csv"

# Import data using datetime and no data value
CSE_Data = pd.read_csv(file_path, parse_dates=['Date'], index_col=['Date'])
# print(CSE_Data.head())

CSE06_08 = CSE_Data['1985-10-01':'1986-03-01']
plt.figure(figsize=(10,10))
plt.plot(CSE06_08.index, CSE06_08[' Banks Finance & Insurance '])
plt.xlabel("Date")
plt.ylabel("Banks Finance & Insurance")
plt.title("Banks Finance & Insurance")
plt.gcf().autofmt_xdate()
plt.show()

'''CSE06_08["SMA1"] = CSE06_08[' Banks Finance & Insurance '].rolling(window=50).mean()
CSE06_08["SMA2"] = CSE06_08[' Banks Finance & Insurance '].rolling(window=100).mean()

plt.figure(figsize=(10,10))
plt.plot(CSE06_08['SMA1'], 'g--', label="SMA1")
plt.plot(CSE06_08['SMA2'], 'r--', label="SMA2")
plt.plot(CSE06_08[' Banks Finance & Insurance '], label=" Banks Finance & Insurance ")
plt.legend()
plt.show()'''