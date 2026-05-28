
import header
import plotter
from pathlib import Path
import pandas as pd

header.logo(1)


class material():

    def __init__(self,Mm=0,mol=0,mass=0):

        self.Mm = Mm

        self.mol = mol

        self.mass = mass
    def calc_mol(self): self.mol = self.mass / self.Mm


co2_co3 = 1.3636

cao_ca = 0.7147


co3 = material(60.009)

ca = material(40.078)

caco3 = material(100.086)


co2 = material()

cao = material()


mass_total = 100


while True:

    try:

        purity = float(input("\n\n[Enter purity of CO2]: "))

        if 0<purity<=1: break

        else: raise ValueError

    except ValueError: print("Try again.\n")

x_data = []
y_data = []

for i in range(1000001):

    co2.mass = i*purity/10000

    cao.mass = mass_total - co2.mass

    co3.mass = co2.mass * co2_co3

    ca.mass = cao.mass * cao_ca 

    ca.calc_mol()
    co3.calc_mol()
    
    match (ca.mol >= co3.mol):
        case True: caco3.mol = co3.mol
        case False: caco3.mol = ca.mol
    
    caco3.mass = caco3.mol*caco3.Mm

    x_data.append(co2.mass)
    y_data.append(caco3.mass)
    print(f"[Success] CO2 {co2.mass}%:      CaCO3 {caco3.mass}g")
plotter.plotter(
    dataframe =  pd.DataFrame({
        'CO2': x_data,
        'CaCO3': y_data
    }),          
    path        = r'C:\Users\user\Downloads',
    x_key       = 'CO2', 
    y_keys      = ['CaCO3'],
    y_colors    = ["red"],
    title       = f"탄산칼슘 결정화 반응의 양적관계 수치 모델링 [이산화탄소 순도: {purity*100}%]",
    x_label     = "CO2 Input Mass (%)",
    y_label     = "CaCO3 Yield Mass (%)",
    xticks      = False
)
