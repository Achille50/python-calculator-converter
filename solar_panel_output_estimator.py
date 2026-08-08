def daily_output(wattage, peak_sun_hours, efficiency):
    return wattage * peak_sun_hours * efficiency / 1000
def monthly_output(wattage, peak_sun_hours, efficiency):
    return daily_output(wattage, peak_sun_hours, efficiency) * 30
def yearly_output(wattage, peak_sun_hours, efficiency):
    return daily_output(wattage, peak_sun_hours, efficiency) * 365
print("Welcome to the Solar Panel Output Estimator!")
print("Would you like to estimate a daily, monthly, or yearly output?")
print("1. Daily output")
print("2. Monthly output")
print("3. Yearly output")
valid_choice = False
while not valid_choice:
    choice = input("Enter your choice (1/2/3): ")
    if choice in ["1", "2", "3"]:
        valid_choice = True
    else:
        print("Invalid choice. Please choose from 1, 2, or 3.")
wattage= float(input("Enter the wattage of the solar panel (in watts): "))
print("Do you know the average peak sun hours for your location?\nIf not, choose from the following locations presets that match your region:")
menu = ["1. Cotonou", "2. Parakou", "3. Abomey","4. Enter my own value"]
for option in menu:
    print(option)
sun_hours_by_location = {
    "cotonou": 4.5,
    "parakou": 4.2,
    "abomey": 4.7
}
valid_choice= False
while not valid_choice:
    location_choice = input("Enter your choice (1/2/3/4): ")
    if location_choice == "1":
        peak_sun_hours = sun_hours_by_location["cotonou"]
        valid_choice = True
    elif location_choice == "2":
        peak_sun_hours = sun_hours_by_location["parakou"]
        valid_choice = True
    elif location_choice == "3": 
        peak_sun_hours = sun_hours_by_location["abomey"]
        valid_choice = True
    elif location_choice == "4":
        peak_sun_hours = float(input("Enter the average peak sun hours per day: "))
        valid_choice = True
    else:
        print("Invalid choice. Please choose from 1, 2, 3, or 4.")
efficiency= float(input("Enter the efficiency of the solar panel (as a decimal): "))
if choice == "1":
    print(f"The estimated daily energy output is {round(daily_output(wattage, peak_sun_hours, efficiency), 2)} kWh.")
elif choice == "2":
    print(f"The estimated monthly energy output is {round(monthly_output(wattage, peak_sun_hours, efficiency), 2)} kWh.")
elif choice == "3":
    print(f"The estimated yearly energy output is {round(yearly_output(wattage, peak_sun_hours, efficiency), 2)} kWh.")