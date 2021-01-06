#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Ohm calculator | ----\n", fg("red")))

# class
class Calculator:
    def __init__(self, unit):
        self.unit = unit

    # output magic method
    def __repr__(self):
        if self.unit == "V":
            return f"\nVolts: {self.voltage()}\n"
        elif self.unit == "I":
            return f"\nAmpere: {self.current()}\n"
        elif self.unit == "R":
            return f"\nOhm: {self.resistance()}\n"
        elif self.unit == "P":
            return f"\nWatts: {self.power()}\n"
        else:
            return "\nInvalid Input\n"

    # methods
    def voltage(self):
        ampere = float(input("\nCurrent (I) in Ampere: "))
        ohm = float(input("Resistance (R) in Ohm: "))
        volts = ampere * ohm
        return stylize(volts, fg("red"))

    def current(self):
        volts = float(input("\nVoltage (V) in Volts: "))
        ohm = float(input("Resistance (R) in Ohm: "))
        ampere = volts / ohm
        return stylize(ampere, fg("red"))

    def resistance(self):
        volts = float(input("\nVoltage (V) in Volts: "))
        ampere = float(input("Current (I) in Ampere: "))
        ohm = volts / ampere
        return stylize(ohm, fg("red"))

    def power(self):
        volts = float(input("\nVoltage (V) in Volts: "))
        ampere = float(input("Current (I) in Ampere: "))
        watts = volts * ampere
        return stylize(watts, fg("red"))

# main execution
if __name__ == "__main__":

    # options
    print(stylize("Options:", fg("green")))
    print("> 'V' for voltage\n> 'I' for current\n> 'R' for resistance\n> 'P' for power")

    # user interaction
    unit = input("\nWhich unit do you want for output?\n: ").upper()

    print(Calculator(unit))
