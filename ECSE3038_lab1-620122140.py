#Q1
def parallel(resistors):


    tot_inverse = sum(1 / resistor for resistor in resistors)
    effect_resistance = 1 / tot_inverse
    return f"{effect_resistance:.3f} ohms"


print(parallel([440, 1030, 5600]))

#Q2

def potential_divider(voltage_supply, resistors):



    tot_resistance = sum(resistors)
    voltage_drops = [voltage_supply * (resistor / tot_resistance) for resistor in resistors]
    formatfor_voltages = [f"{voltage:.3f}v" for voltage in voltage_drops]
    return formatfor_voltages


voltages = potential_divider(9, [3000, 1000])
for voltage in voltages:
    print(voltage)


    #Q3
def temperature_check(temperature, unit='C'):

    if unit == 'F':
        temperature = (temperature - 32) * 5/9  

    if temperature < 35.5:
        status = "Danger, the patient is hypothermic."

    elif 35.5 <= temperature <= 37.5:
        status = "The patient's body temperature is within normal range."

    else:
        status = "Danger, the patient is hyperthermic."
    
    return status

patient_temperature = 37.5 
temperature_unit = 'C'  
print(temperature_check(patient_temperature, temperature_unit))

