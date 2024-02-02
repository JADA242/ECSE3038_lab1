#Q1
def parallel(resistors):


    tot_inverse = sum(1 / resistor for resistor in resistors)
    effect_resistance = 1 / tot_inverse
    return f"{effect_resistance:.3f} ohms"


print(parallel([440, 1030, 5600]))

#Q2

def pot_divider(voltage_supply, resistors):



    tot_resistance = sum(resistors)
    voltage_drops = [voltage_supply * (resistor / tot_resistance) for resistor in resistors]
    formatfor_voltages = [f"{voltage:.3f}v" for voltage in voltage_drops]
    return formatfor_voltages


voltages = pot_divider(9, [3000, 1000])
for voltage in voltages:
    print(voltage)