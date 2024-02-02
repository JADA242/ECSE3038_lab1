# ECSE3038_lab1

LAB SUMMARY:

## Description
This project contains Python functions for temperature and electrical calculations.

## Functions

### 1. `parallel(resistors)`

This function calculates the effective resistance of a network of resistors connected in parallel.

- Parameters:
  - `resistors`: A list of resistance values of resistors connected in parallel.

- Returns:
  - A string indicating the effective resistance of the network.
 
### 2. `potential_divider(voltage_supply, resistors)`

This function calculates the voltage drop across each resistor in a potential divider circuit.

- Parameters:
  - `voltage_supply`: The voltage supply value.
  - `resistors`: A list of resistance values of resistors connected in series.

- Returns:
  - A list of strings indicating the voltage drop across each resistor.

### 3. `temperature_check(temperature, unit='C')`

This function checks the patient's body temperature and determines whether they are hypothermic, hyperthermic, or have a normal body temperature based on the temperature value and the unit of temperature provided.

- Parameters:
  - `temperature`: The patient's body temperature.
  - `unit`: The unit of temperature, either 'C' for Celsius or 'F' for Fahrenheit. Default is Celsius.

- Returns:
  - A string indicating the patient's temperature status.


## Example Usage

# Example usage of parallel
print(parallel([440, 1030, 5600]))

# Example usage of potential_divider
voltages = potential_divider(9, [3000, 1000])
for voltage in voltages:
    print(voltage)
    
# Example usage of temperature_check
patient_temperature = 37.5 
temperature_unit = 'C'  
print(temperature_check(patient_temperature, temperature_unit))


Reason for code: Assignment for class.

A joke: Why don't skeletons fight each other?
      -They dont have any guts.




