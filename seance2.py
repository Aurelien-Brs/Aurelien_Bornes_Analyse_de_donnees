
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

with open("src/data/resultats-elections-presidentielles-2022-1er-tour.csv","r",encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier,sep=",")
print(contenu.head())

# Question 2
print (contenu.shape)

# Question 3
print (contenu.dtypes)

# Question 4
print (contenu.columns)
# aperçu
print (contenu.head())

# Question 5
print (contenu["Inscrits"].head())

# Question 6
colonnes_numériques = contenu.select_dtypes(include=["int64","float64"])
print (colonnes_numériques.sum())
Path("images").mkdir(exist_ok=True)

# Etape 11
for i, row in contenu.iterrows():
    dept= str(row["Libellé du département"]).replace(" ","-").replace("/","-")

    plt.figure()
    plt.bar(["Inscrits","Votants"],[row["Inscrits"],row["Votants"]])
    plt.title(dept)
    plt.tight_layout()
    plt.savefig(f"images/bar_{i}_{dept}.png")
    plt.close()

# Etape 12
for i, row in contenu.iterrows():
    dept = str(row["Libellé du département"]).replace(" ","_").replace("/","-")
    
    valeurs= [
        row["Blancs"],
        row["Nuls"],
        row["Exprimés"],
        row["Abstentions"]
    ]
    labels= ["Blancs","Nuls","Exprimés","Abstentions"]

    plt.figure()
    plt.pie(valeurs,labels=labels,autopct="%1.1f%%")
    plt.title(dept)
    plt.tight_layout()
    plt.savefig(f"images/pie_{i}_{dept}.png")
    plt.close()

# Etape 13
plt.figure()
plt.hist(contenu["Inscrits"], bins=30, density=True)
plt.title("Distribution des inscrits")
plt.xlabel("Inscrits")
plt.ylabel("Densité")
plt.tight_layout()
plt.savefig("images/hist_inscrits.png")
plt.close()

print("Boucle pie terminée")

 