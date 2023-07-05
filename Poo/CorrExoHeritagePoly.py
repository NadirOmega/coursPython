class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, nombre_portes, carburant):
        super().__init__(marque, modele, annee)
        self.nombre_portes = nombre_portes
        self.carburant = carburant

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, cylindree):
        super().__init__(marque, modele, annee)
        self.cylindree = cylindree

class Location:
    def __init__(self, vehicule, jours):
        self.vehicule = vehicule
        self.jours = jours
voiture1 = Voiture("Ford", "Focus", 2020, 4, "Essence")
moto1 = Moto("Honda", "CBR", 2021, 600)
location1 = Location(voiture1, 5)

vehicules = [voiture1, moto1, location1.vehicule]

for vehicule in vehicules:
    if isinstance(vehicule, Voiture):
        print(f"Voiture: {vehicule.marque} {vehicule.modele}, Année: {vehicule.annee}, Portes: {vehicule.nombre_portes}, Carburant: {vehicule.carburant}")
    elif isinstance(vehicule, Moto):
        print(f"Moto: {vehicule.marque} {vehicule.modele}, Année: {vehicule.annee}, Cylindrée: {vehicule.cylindree}")
    elif isinstance(vehicule, Location):
        print(f"Location: {vehicule.vehicule.marque} {vehicule.vehicule.modele}, Durée: {vehicule.jours} jours")
