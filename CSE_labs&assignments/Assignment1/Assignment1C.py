print("[Centimeters to Feet and Inches Converter]")

Centi_Mes = float(input(f"Enter the length in centimeters: "))

Full_inches = (Centi_Mes / 2.54)

Feet = (Full_inches // 12)
inch = round(Full_inches % 12, 2)

print(f"The length is {Feet} feet and {inch} inches")
