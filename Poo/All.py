class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def dire_bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")

personne1 = Personne("Alice", 25)
personne1.dire_bonjour()  # Affiche "Bonjour, je m'appelle Alice et j'ai 25 ans."

############################
############################

class Personne:
    def __init__(self, nom):
        self.nom = nom

personne = Personne("Alice")
print(personne.nom)  # Accès à l'attribut public "nom"
personne.nom = "Bob"  # Modification de l'attribut public "nom"


#########################
########################
class Personne:
    def __init__(self, nom):
        self._age = 25  # Attribut protégé

personne = Personne("Alice")
print(personne._age)  # Accès à l'attribut protégé "_age"
personne._age = 30    # Modification de l'attribut protégé "_age"


########################
#########################
class Personne:
    def __init__(self, nom):
        self.__salaire = 5000  # Attribut privé

personne = Personne("Alice")
print(personne.__salaire) #Erreur d'accès
print(personne._Personne__salaire)  # Accès à l'attribut privé "__salaire" de manière non recommandée
personne.__salaire = 6000         # Tentative de modification de l'attribut privé "__salaire"


##################
#################


class ClasseEnfant(ClasseParent):
    # Définition de la classe enfant
    ...

    
##############################
#############################
class CompteBancaire:
    def __init__(self, solde):
        self.solde = solde      # Attribut public
        self._transactions = [] # Attribut protégé
        self.__pin = 1234       # Attribut privé

    def deposer(self, montant):
        self.solde += montant
        self._transactions.append(f"Dépôt de {montant}")

    def __retirer(self, montant):  # Méthode privée
        if montant <= self.solde:
            self.solde -= montant
            self._transactions.append(f"Retrait de {montant}")
        else:
            print("Solde insuffisant.")

    def afficher_transactions(self):
        print("Transactions :")
        for transaction in self._transactions:
            print(transaction)

compte1 = CompteBancaire(1000)
compte1.deposer(500)
compte1._CompteBancaire__retirer(200)  # Appel de la méthode privée
compte1.afficher_transactions()        # Affiche les transactions

################
################
class Employe(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)
        self.salaire = salaire

    def afficher_salaire(self):
        print(f"Le salaire de {self.nom} est {self.salaire}.")

class Manager(Employe):
    def __init__(self, nom, age, salaire, equipe):
        super().__init__(nom, age, salaire)
        self.equipe = equipe

    def afficher_equipe(self):
        print(f"L'équipe de {self.nom} : {', '.join(self.equipe)}.")

class Vendeur(Employe):
    def __init__(self, nom, age, salaire, commission):
        super().__init__(nom, age, salaire)
        self.commission = commission

    def vendre(self, montant):
        vente = montant * self.commission
        print(f"{self.nom} a réalisé une vente de {vente}.")

personne1 = Employe("Alice", 25, 3000)
personne1.afficher_salaire()  # Affiche "Le salaire de Alice est 3000."

manager1 = Manager("Bob", 30, 5000, ["Anna", "John"])
manager1.afficher_salaire()  # Affiche "Le salaire de Bob est 5000."
manager1.afficher_equipe()   # Affiche "L'équipe de Bob : Anna, John."

vendeur1 = Vendeur("Charlie", 35, 2000, 0.1)
vendeur1.afficher_salaire()  # Affiche "Le salaire de Charlie est 2000."
vendeur1.vendre(1000)        # Affiche "Charlie a réalisé une vente de 100."

# Polymorphisme avec une liste d'objets
employes = [personne1, manager1, vendeur1]

for employe in employes:
    employe.afficher_salaire()


###################
###################

class MaClasse:
    attribut_de_classe = 10

    def __init__(self):
        self.attribut_d_instance = 20

    @classmethod
    def methode_de_classe(cls):
        print(cls.attribut_de_classe)

    def methode_d_instance(self):
        print(self.attribut_d_instance)

    @staticmethod
    def methode_statique():
        print("Méthode statique")

MaClasse.methode_de_classe()  # Affiche 10

objet = MaClasse()
objet.methode_d_instance()  # Affiche 20

MaClasse.methode_statique()  # Affiche "Méthode statique"


######################
######################

from abc import ABC, abstractmethod

class Personne(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def dire_bonjour(self):
        pass

class Etudiant(Personne):
    def dire_bonjour(self):
        print(f"Bonjour, je suis l'étudiant {self.nom}.")

class Enseignant(Personne):
    def dire_bonjour(self):
        print(f"Bonjour, je suis l'enseignant {self.nom}.")

personne1 = Etudiant("Alice")
personne2 = Enseignant("Bob")

personne1.dire_bonjour()  # Affiche "Bonjour, je suis l'étudiant Alice."
personne2.dire_bonjour()  # Affiche "Bonjour, je suis l'enseignant Bob."


#####################
#####################
