import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "data", "mock", "transactions.csv")
print(csv_path)