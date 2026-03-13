import pandas as pd

# Load datasets
inbound = pd.read_csv("datasets/InboundPerformance.csv")
checking = pd.read_csv("datasets/CheckingPerformance.csv")
putaway = pd.read_csv("datasets/PutAwayPerformance.csv")
dispatch = pd.read_csv("datasets/DispatchPerformance.csv")
inventory = pd.read_csv("datasets/InventoryAccuracy.csv")
labour = pd.read_csv("datasets/LabourUtilisation.csv")

# View first rows
print(inbound.head())
print(checking.head())

# Basic stats
print(inbound.describe())
print(checking.describe())

# Check missing data
print(inbound.isnull().sum())
