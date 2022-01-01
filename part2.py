class etudiant:
    def _init_(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne


etudiant = [
    {'nom': 'EL YAKINI', 'prenom': 'WIAME',
        'age': 22, 'cne': "KB123451", 'moyenne': 18},
    {'nom': 'ALAOUI', 'prenom': 'AHMED', 'age': 23,
        'cne': "KB123452", 'moyenne': 16},
]

# liste ordonnée selon l'age
print("la Liste triée selon age :")
etudiant.sort(key=lambda x: x.get('age'))
print(etudiant)
# liste ordonnéé selon la moyenne
print("\nla Liste triée selon la moyenne :")
etudiant.sort(key=lambda x: x.get('moyenne'))
print(etudiant)
