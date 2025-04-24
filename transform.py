# funkce na přepočet kelvin na celsius (Openweather vrací v kelvinech)
def kelvin_to_celsius(kelvin: float) -> float:
    return float(kelvin)-273.15

# funkce na přepočet stop na metry (Openweather vrací ve stopách)
def feet_to_meters(feet: float) -> float: 
    return float(feet)*0.3048