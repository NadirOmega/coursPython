class GestionnaireCSV:
    def exporter_auteurs_csv(self, auteurs, nom_fichier):
        with open(nom_fichier, 'w', newline='') as fichier_csv:
            writer = csv.writer(fichier_csv)
            writer.writerow(['Nom', 'Nationalite'])
            for auteur in auteurs:
                writer.writerow([auteur.nom, auteur.nationalite])
    def importer_auteurs_csv(self, nom_fichier):
        auteurs = []
        with open(nom_fichier, 'r') as fichier_csv:
            reader = csv.DictReader(fichier_csv)
            for ligne in reader:
                nom = ligne['Nom']
                nationalite = ligne['Nationalite']
                auteur = Auteur(nom, nationalite)
                auteurs.append(auteur)
        return auteurs              
