import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random, os

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

# Warehouses and addresses
sites = [
    ("Deal Party", "44 Deal Party Road, Deal Party, Gqeberha, 6012"),
    ("Korsten", "12 Kempston Road, Korsten, Gqeberha, 6020"),
    ("Fairview", "5 Haworthia Drive, Fairview, Gqeberha, 6070"),
    ("Newton Park", "18 Diaz Road, Newton Park, Gqeberha, 6045"),
    ("Walmer Downs", "101 Burman Road, Walmer Downs, Gqeberha, 6070")
]

clients = [
    "BayLine Automotive Logistics",
    "Algoa Fresh Distribution",
    "Coastal Homeware Supply Co.",
    "Eastern Cape Tech Components",
    "HarbourView Retail Distribution"
]

suppliers = ["AutoParts SA", "TechGlobal Imports", "MassRetail Suppliers", "FurnitureDirect", "FreshFoods SA"]
routes = ["PE → Uitenhage", "PE → Despatch", "PE → Jeffreys Bay", "PE → Humansdorp", "PE → Summerstrand"]
zones = ["Zone A1", "Zone B2", "Zone C3", "Rack D4", "Rack F2", "Chill Room 2"]

# Helper function for random datetime ranges
def random_datetime_pair():
    start = datetime(2026, 2, random.randint(1, 28), random.randint(6, 14), random.randint(0, 59))
    end = start + timedelta(minutes=random.randint(20, 180))
    return start, end

# ------- Generate InboundPerformance --------
inbound_rows = []
for i in range(50):
    site, address = random.choice(sites)
    client = random.choice(clients)
    start, end = random_datetime_pair()
    inbound_rows.append([
        1000 + i, site, client, random.randint(200, 3000), start, end,
        random.choice(suppliers), address
    ])

inbound_df = pd.DataFrame(inbound_rows, columns=[
    "InboundID", "Site", "Client", "UnitsReceived", "StartTime", "EndTime",
    "Supplier", "WarehouseAddress"
])

# ------- Generate CheckingPerformance --------
checking_rows = []
for i in range(50):
    site, address = random.choice(sites)
    client = random.choice(clients)
    expected = random.randint(100, 2000)
    actual = expected - random.randint(0, 10)
    checking_rows.append([
        5000 + i, site, client, expected, actual, random.randint(20, 90), address
    ])

checking_df = pd.DataFrame(checking_rows, columns=[
    "CheckID", "Site", "Client", "ExpectedQty", "ActualQty", "DurationMin", "WarehouseAddress"
])

# ------- Generate PutAwayPerformance --------
putaway_rows = []
for i in range(50):
    site, address = random.choice(sites)
    client = random.choice(clients)
    start, end = random_datetime_pair()
    putaway_rows.append([
        8000 + i, site, client, f"SKU-{random.randint(100,999)}", start, end,
        random.choice(zones), address
    ])

putaway_df = pd.DataFrame(putaway_rows, columns=[
    "PAID", "Site", "Client", "ProductCode", "StartTime", "EndTime", "Zone", "WarehouseAddress"
])

# ------- Generate DispatchPerformance --------
dispatch_rows = []
for i in range(50):
    site, address = random.choice(sites)
    client = random.choice(clients)
    dep, arr = random_datetime_pair()
    sla = random.choice(["Met", "Missed"])
    dispatch_rows.append([
        9000 + i, site, client, random.choice(routes), sla, dep, arr, address
    ])

dispatch_df = pd.DataFrame(dispatch_rows, columns=[
    "DispatchID", "Site", "Client", "Route", "SLAStatus", "DepartureTime", "ArrivalTime", "WarehouseAddress"
])

# ------- Generate InventoryAccuracy --------
inv_rows = []
for i in range(50):
    site, address = random.choice(sites)
    client = random.choice(clients)
    expected = random.randint(500, 5000)
    actual = expected - random.randint(0, 30)
    variance = (actual - expected) / expected
    inv_rows.append([
        3000 + i, site, client, expected, actual, round(variance, 4), address
    ])

inventory_df = pd.DataFrame(inv_rows, columns=[
    "AuditID", "Site", "Client", "ExpectedQty", "ActualQty", "Variance", "WarehouseAddress"
])

# ------- Generate LabourUtilisation --------
labour_rows = []
for i in range(50):
    site, address = random.choice(sites)
    total = random.randint(200, 800)
    productive = total - random.randint(10, 100)
    labour_rows.append([
        f"L{100+i}", site, total, productive, address
    ])

labour_df = pd.DataFrame(labour_rows, columns=[
    "ShiftID", "Site", "TotalHours", "ProductiveHours", "WarehouseAddress"
])

# Save all files
os.makedirs("datasets", exist_ok=True)
inbound_df.to_csv("datasets/InboundPerformance.csv", index=False)
checking_df.to_csv("datasets/CheckingPerformance.csv", index=False)
putaway_df.to_csv("datasets/PutAwayPerformance.csv", index=False)
dispatch_df.to_csv("datasets/DispatchPerformance.csv", index=False)
inventory_df.to_csv("datasets/InventoryAccuracy.csv", index=False)
labour_df.to_csv("datasets/LabourUtilisation.csv", index=False)

"Datasets generated successfully."
