def parallel(resistors):
    tot_inverse = sum(1 / resistor for resistor in resistors)
    effect_resistance = 1 / tot_inverse
    return f"{effect_resistance:.3f} ohms"


print(parallel([440, 1030, 5600]))