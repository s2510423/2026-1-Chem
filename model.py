import math

import header
import plotter

header.logo(1)


class material():

    def __init__(self,Mm,mol,mass):

        self.Mm = Mm

        self.mol = mol

        self.mass = mass


co2_co3 = 1.3636

cao_ca = 0.7147


co3 = material(60.009,0,0)

ca = material(40.078,0,0)

caco3 = material(100.086,0,0)


co2 = material(0,0,0)

cao = material(0,0,0)


mass_total = 100


while True:

    try:

        purity = float(input("\n\n[Enter purity of CO2]: "))

        if 0<purity<=1: break

        else: raise ValueError

    except ValueError: print("Try again.\n")



for i in range(1000001):

    co2.mass = i*purity/1000

    cao.mass = mass_total - co2.mass

    co3.mass = co2.mass * co2_co3

    ca.mass = cao.mass * cao_ca 