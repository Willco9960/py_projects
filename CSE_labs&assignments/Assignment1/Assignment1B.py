print("[Ideal Gas Law Calculator]")
Moles_Gas = float(input(f"Enter the number of moles of the gas: "))
Gas_C = float(input(f"Enter the temperature of the gas in Celsius: "))
Vol_Gas = float(input(f"Enter the volume of the gas in Liters: "))

Gas_K = (Gas_C + 273.15)
R = 0.0821

nRT = (Moles_Gas * Gas_K * R)
P = (nRT / Vol_Gas)

print(f"The pressure of the gas is", round(P, 2), "atm")
