# funkce na přepočet kelvin na celsius (Openweather vrací v kelvinech)
def kelvin_to_celsius(kelvin: float) -> float:
    if not type(kelvin) in [float, int]:  # dotaz na typ dat
        return ValueError()
    return float(kelvin)-273.15

# funkce na přepočet stop na metry (Openweather vrací ve stopách)
def feet_to_meters(feet: float) -> float: 
    if not type(feet) in [float, int]:  # dotaz na typ dat
        return ValueError()
    return float(feet)*0.3048