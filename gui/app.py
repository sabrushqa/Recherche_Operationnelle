import tkinter as tk
from tkinter import ttk
from config.settings import GUI_SETTINGS
from gui.dialogs import (BellmanFordDialog, WelshPowellDialog, DijkstraDialog, KruskalDialog,
                        FordFulkersonDialog, PotentielMetraDialog,
                        TransportDialog)

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title(GUI_SETTINGS['WINDOW_TITLE'])
        self.root.geometry(GUI_SETTINGS['WINDOW_SIZE'])
        self.root.config(bg="white")  # Changer la couleur de fond en blanc
        self.create_main_frame()

    def create_main_frame(self):
        """Crée la fenêtre principale de l'application"""
        # Détruire tous les widgets existants
        for widget in self.root.winfo_children():
            widget.destroy()

        # Ajouter un logo
        try:
            self.logo = tk.PhotoImage(file="C:/Users/hp/Downloads/emsi.png")
            self.logo = self.logo.subsample(2, 2)  # Ajuster la taille du logo
            logo_label = tk.Label(self.root, image=self.logo, bg="white")
            logo_label.pack(pady=10)
        except Exception as e:
            print(f"Erreur lors du chargement du logo : {e}")
        
        # Ajouter un titre en haut
        title_label = tk.Label(self.root, text="Nom étudiant: Sabrine Lakehal\nProf: Mme Mouna Elmkhalet", 
                               font=("Arial", 16), pady=10, bg="white", fg="black")
        title_label.pack()
        
        # Bouton Quitter en haut à droite
        btn_sortie = tk.Button(
            self.root,
            text="Quitter",
            font=GUI_SETTINGS['BUTTON_FONT'],
            bg="#F44336",  # Couleur de fond rouge
            fg="white",  # Couleur du texte blanche
            width=15,
            height=2,
            relief="groove",
            command=self.root.quit
        )
        btn_sortie.pack(anchor='ne', padx=10, pady=10)

        # Titre principal
        title = tk.Label(
            self.root,
            text="Interface Graphique",
            font=GUI_SETTINGS['TITLE_FONT'],
            fg="black",
            bg="white"
        )
        title.pack(pady=20)

        # Cadre pour le menu d'entrée
        frame = tk.Frame(
            self.root,
            bg="white",
            bd=3,
            relief="solid"
        )
        frame.pack(pady=20, padx=50)

        # Bouton Liste des Algorithmes au centre
        btn_entree = tk.Button(
            frame,
            text="Liste des Algorithmes",
            font=GUI_SETTINGS['BUTTON_FONT'],
            bg="#4CAF50",  # Couleur de fond verte
            fg="white",  # Couleur du texte blanche
            width=20,
            height=2,
            relief="groove",
            command=self.afficher_algorithmes
        )
        btn_entree.pack(pady=20)

    def afficher_algorithmes(self):
        """Affiche la liste des algorithmes disponibles"""
        for widget in self.root.winfo_children():
            widget.destroy()

        # Titre principal
        title = tk.Label(
            self.root,
            text="choisir un algorithme",
            font=GUI_SETTINGS['TITLE_FONT'],
            fg="black",
            bg="white"
        )
        title.pack(pady=20)

        # Cadre pour les boutons des algorithmes
        frame_algos = tk.Frame(
            self.root,
            bg="white",
            bd=3,
            relief="solid"
        )
        frame_algos.pack(pady=20, padx=50)

        algorithmes = {
            "Welsh Powell": lambda: WelshPowellDialog(self.root),
            "Dijkstra": lambda: DijkstraDialog(self.root),
            "Kruskal": lambda: KruskalDialog(self.root),
            "Bellman ford": lambda: BellmanFordDialog(self.root),
            "Ford Fulkerson": lambda: FordFulkersonDialog(self.root),
            "Potentiel METRA": lambda: PotentielMetraDialog(self.root),
            "Nord-Ouest": lambda: TransportDialog(self.root, "nord_ouest"),
            "Moindre Coût": lambda: TransportDialog(self.root, "moindre_cout"),
            "Stepping-Stone": lambda: TransportDialog(self.root, "stepping_stone")
        }

        # Ajouter les boutons dans une grille
        for i, (algo, command) in enumerate(algorithmes.items()):
            btn_algo = tk.Button(
                frame_algos,
                text=algo,
                font=GUI_SETTINGS['BUTTON_FONT'],
                bg="#2196F3",  # Couleur de fond bleue
                fg="white",  # Couleur du texte blanche
                width=20,
                height=2,
                relief="groove",
                command=command
            )
            btn_algo.grid(row=i//3, column=i%3, padx=10, pady=10)

        # Bouton Retour pour revenir à la page principale
        btn_retour = tk.Button(
            self.root,
            text="Retour",
            font=GUI_SETTINGS['BUTTON_FONT'],
            bg="#4CAF50",  # Couleur de fond verte
            fg="white",  # Couleur du texte blanche
            width=15,
            height=2,
            relief="groove",
            command=self.create_main_frame
        )
        btn_retour.pack(pady=20)

# Initialisation de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()