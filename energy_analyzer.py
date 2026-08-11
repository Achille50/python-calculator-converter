import matplotlib.pyplot as plt
import pandas as pd
print("Welcome to the Energy Analyzer!")
data=pd.read_csv("energy_usage.csv")
print(data)
print(data["kwh_used"].sum())
print(data["kwh_used"].mean())
print(data["kwh_used"].max())
solar_data = data[data["source"] == "solar"]    
grid_data = data[data["source"] == "grid"]
solar_total = solar_data["kwh_used"].sum()
grid_total = grid_data["kwh_used"].sum()
print(f"Total energy used from solar: {round(solar_total, 2)} kWh")
print(f"Total energy used from grid: {round(grid_total, 2)} kWh")
plt.scatter(solar_data["date"], solar_data["kwh_used"], color="orange", label="Solar")
plt.scatter(grid_data["date"], grid_data["kwh_used"], color="gray", label="Grid")
plt.xlabel("Date")
plt.ylabel("kWh Used")
plt.title("Daily Energy Usage by Source")
plt.xticks(rotation=45)
plt.legend()
plt.show()