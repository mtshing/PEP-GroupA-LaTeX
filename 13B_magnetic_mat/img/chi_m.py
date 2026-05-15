import numpy as np
import matplotlib.pyplot as plt

atomic_numbers = {
    "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
    "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20,
    "Sc": 21, "Ti": 22, "V": 23, "Cr": 24, "Mn": 25, "Fe": 26, "Co": 27, "Ni": 28, "Cu": 29, "Zn": 30,
    "Ga": 31, "Ge": 32, "As": 33, "Se": 34, "Br": 35, "Kr": 36, "Rb": 37, "Sr": 38, "Y": 39, "Zr": 40,
    "Nb": 41, "Mo": 42, "Tc": 43, "Ru": 44, "Rh": 45, "Pd": 46, "Ag": 47, "Cd": 48, "In": 49, "Sn": 50,
    "Sb": 51, "Te": 52, "I": 53, "Xe": 54, "Cs": 55, "Ba": 56, "La": 57, "Ce": 58, "Pr": 59, "Nd": 60,
    "Pm": 61, "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Dy": 66, "Ho": 67, "Er": 68, "Tm": 69, "Yb": 70,
    "Lu": 71, "Hf": 72, "Ta": 73, "W": 74, "Re": 75, "Os": 76, "Ir": 77, "Pt": 78, "Au": 79, "Hg": 80,
    "Tl": 81, "Pb": 82, "Bi": 83, "Po": 84, "At": 85, "Rn": 86, "Fr": 87, "Ra": 88, "Ac": 89, "Th": 90,
    "Pa": 91, "U": 92, "Np": 93, "Pu": 94, "Am": 95, "Cm": 96, "Bk": 97, "Cf": 98, "Es": 99, "Fm": 100,
    "Md": 101, "No": 102, "Lr": 103, "Rf": 104, "Db": 105, "Sg": 106, "Bh": 107, "Hs": 108, "Mt": 109,
    "Ds": 110, "Rg": 111, "Cn": 112, "Nh": 113, "Fl": 114, "Mc": 115, "Lv": 116, "Ts": 117, "Og": 118
}

# Molar Magnetic Susceptibility (SI units: m^3/mol)
# Note: Values for ferromagnetic elements (Fe, Co, Ni) are 'apparent' or field-dependent.
# Scientific notation: 1.2e-9 = 1.2 x 10^-9

chi_m = {
    "H": -3.99,      "He": -2.02,      "Li": 14.2,      "Be": -9.0,
    "B": -6.7,       "C": -6,          "N": -12,        "O": 10200,
    "F": -120,       "Ne": -6.96,      "Na": 16,        "Mg": 13.1,
    "Al": 16.5,      "Si": -3.12,      "P": -20.77,     "S": -15.5,
    "Cl": -40.4,     "Ar": -19.32,     "K": 20.8,       "Ca": 40,
    "Sc": 295.2,     "Ti": 151,        "V": 285,        "Cr": 1167,
    "Mn": 511,       "Fe": 100000000,  "Co": 100000000, "Ni": 100000000,
    "Cu": -5.46,     "Zn": -9.15,      "Ga": -21.6,     "Ge": -11.6,
    "As": -5.6,      "Se": -25,        "Br": -56.4,     "Kr": -29,
    "Rb": 17,        "Sr": 92,         "Y": 187.7,      "Zr": 120,
    "Nb": 208,       "Mo": 72,         "Tc": 115,       "Ru": 39,
    "Rh": 102,       "Pd": 540,        "Ag": -19.5,     "Cd": -19.7,
    "In": -10.2,     "Sn": -37.4,      "Sb": -99,       "Te": -38,
    "I": -90,        "Xe": -45.5,      "Cs": 29,        "Ba": 20.6,
    "La": 95.9,      "Ce": 2500,       "Pr": 5530,      "Nd": 5930,
    "Sm": 1278,      "Eu": 30900,      "Gd": 185000,    "Tb": 170000,
    "Dy": 98000,     "Ho": 72900,      "Er": 48000,     "Tm": 24700,
    "Yb": 67,        "Lu": 182.9,      "Hf": 71,        "Ta": 154,
    "W": 53,         "Re": 67,         "Os": 11,        "Ir": 25,
    "Pt": 193,       "Au": -28,        "Hg": -33.5,     "Tl": -50,
    "Pb": -23,       "Bi": -280.1,     
}

chi_m2 = {    
    "Th": 97,        "Pa": 277,
    "U": 409,        "Pu": 525,        "Am": 1000,    
}

text_adj = {
    "He": (0.5,1), "Be": (-0.5,1), "C": (0, 1/4), "Ne": (1,1), 
    "Na": (-0.5,1), "Mg": (0, 1/4), "Al": (0.5,1),
    "Si": (-0.5,1), "S": (0,1/4), "Ar": (0.5,1), 
    "K": (-1,1/1.5), "Ca": (-0.8,1), "Ti": (0, 1/4), "Sc":(-0.5,1), "V": (-0.5,1/1.1), "Mn": (0.2, 1/4),
    "Cu": (-1, 1/1.3), "Zn": (-0.5,1), "Ge": (-0.5, 1/4), "As": (0, 1/4), "Se": (-0.5,1), "Kr": (0.5,1),
    "Rb": (-1, 1), "Sr": (-1,1), "Zr": (0,1/4), "Mo": (0,1/4), "Tc": (-0.5, 1/1.3), "Ru": (0,1/4), "Rh": (-0.5,1),
    "Ag": (-1,1/1.2), "In": (0, 1/4), "Sn": (-0.5,1), "Te": (0, 1/4), "Xe": (0.5,1),
    "Ba": (0,1/4), "La": (1.5,1/1.3), "Ce": (-1.5,1/1.5), "Pr": (-0.5,1), "Nd": (0.5,1), "Sm": (1,1/4), 
    "Eu": (-1,1/1.5), "Gd": (-0.5,1/1.2), "Tb": (0.5,1/1.2), "Dy": (0.5,1/1.2), "Ho": (1,1/1.5), "Er": (1.2,1/2), "Tm": (1.5,1/2), 
    "Yb": (0,1/4), "Hf": (0,1/4), "W": (0,1/4), "Os": (0,1/4), "Ir": (-0.8,1/1.5),
    "Au": (-1.5,1/2), "Hg": (-0.7,1/1.2), "Pb": (0,1/4),
    "Th": (-1.5, 1/2), "Pa": (-1.5, 1/2), "Pu": (0,1/4)
}

A1 = np.array([atomic_numbers[element] for element in chi_m.keys()])
C1 = np.array([chi for chi in chi_m.values()])

A2 = np.array([atomic_numbers[element] for element in chi_m2.keys()])
C2 = np.array([chi for chi in chi_m2.values()])

fig, ax = plt.subplots()
ax.plot([atomic_numbers["Bi"], atomic_numbers["Th"]], [chi_m["Bi"], chi_m2["Th"]], c="#888888", ls="--")
ax.plot(A1, C1, c="k", label='Data Points', marker='o', mfc="w")
ax.plot(A2, C2, c="k", label='Data Points', marker='o', mfc="w")


for element, chi in chi_m.items():
    if (element == "Co") or (element == "Ni") or (element == "Fe"):
        continue

    adjust = text_adj[element] if element in text_adj else (0, 1)
    ax.text(atomic_numbers[element]+adjust[0], chi*1.5*adjust[1], element, fontsize=11, ha='center', va=('bottom' if (chi > 0) else 'top'))

for element, chi in chi_m2.items():
    
    adjust = text_adj[element] if element in text_adj else (0, 1)
    ax.text(atomic_numbers[element]+adjust[0], chi*1.5*adjust[1], element, fontsize=11, ha='center', va=('bottom' if (chi > 0) else 'top'))


ax.text(68, 0.1, "Paramagnetic", fontsize=11, ha="center", va="bottom")
ax.text(68, -0.1, "Diamagnetic", fontsize=11, ha="center", va="top")

#ax.annotate("adfadf", xytext=(27, 1e5), xy=(27, 10**5.5), ha='center', va='bottom',
#            arrowprops=dict(arrowstyle="-[, widthB=2.0, lengthB=1.5", ec="#000000", shrinkA=0, shrinkB=0))

ax.text(26.5, 10**5.5, "{", fontsize=40, ha="center", va="bottom", rotation=90, c="#888888")
ax.text(30, 10**5.5, "Fe, Co, Ni are ferromagnetic", fontsize=11, c="#888888")

theta = np.degrees(np.arctan2((chi_m2["Th"]) + (-chi_m["Bi"]), atomic_numbers["Th"] - atomic_numbers["Bi"]))
ax.text(86.5, 0.1, "No data", fontsize=11, c="#888888", rotation=theta/2, rotation_mode='anchor', transform_rotates_text=True)


ax.axhline(0, color='black', lw=0.5, ls='--')
ax.set_yscale('symlog', linthresh=1)
ax.set_ylim(-1e3, 1e6)

#ticks = [-1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000, 1000000]
ax.set_xticks(np.arange(0, 100, 10))
ax.set_xlim([0,98])
ax.set_xlabel("Atomic Number")
ax.set_ylabel(r"$\chi_m \times 10^{-6} \left(\frac{\text{cm}^3}{\text{mol}}\right)$")


plt.show()
    
