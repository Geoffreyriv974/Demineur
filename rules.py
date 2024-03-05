import tkinter as tk

pioche_droite = tk.PhotoImage(file="image/pioche_en_or_rules1.png")
pioche_gauche = tk.PhotoImage(file="image/pioche_en_or_rules.png")

def rules():

    windows_rules = tk.Toplevel(bg="#B1A8A8")
    windows_rules.attributes('-fullscreen', True)

    def exit_rules():
        windows_rules.destroy()

    pchd = tk.Label(windows_rules, image=pioche_droite, bg="#B1A8A8")
    pchd.pack(side="right")

    pchg = tk.Label(windows_rules, image=pioche_gauche, bg="#B1A8A8")
    pchg.pack(side="left")

    display_rules = tk.Text(windows_rules, wrap=tk.WORD,width=25, height=15, bg="#B1A8A8", relief="sunken", borderwidth=10, font=("Retro Gaming", 15))
    display_rules.pack(pady=150)


    long_texte = """
    -- Le jeu du démineur consiste à détruire les cases du plateau de jeu en évitant de détruire les mines cachées.
    
    -- À chaque fois que le joueur clique sur une case : 
    - Soit la case est vide est donc il n'y a aucune bombe aux alentour ;
    - Soit un chiffre allant de 1 à 8 apparaît en fonction du nombre de bombes a cotés de la case ;
    - Ou Soit la case est une mine est dans ce cas la partie est perdu ;
        
    -- Le joueur dispose de 2 outils pour l'aider :
    - Un point d'interrogation qui lui permettra de marquer une case potentiellement minée ;
    - Et un drapeau qui lui permettra de verrouiller une case s'il pense qu'une mine s'y cache ;
    
    -- À savoir, il n'est possible de placer qu'un nombre de drapeaux proportionnels aux nombres de mines (15 mines = 15 drapeaux)
    
    -- En fonction des cases qu'il a découvert le score du joueur augmente :
    - Case vide = +90 points ;
    - 1 = +10 points ;
    - 2 = +20 points ;
    - 3 = +30 points ;
    - 4 = +40 points ;
    - 5 = +50 points ;
    - 6 = +60 points ;
    - 7 = +70 points ;
    - 8 = +80 points ;
    - Défaite = +0 point ;
    - Victoire = +100 points ;
    
    -- Le jeu dispose de 3 niveaux de difficulté :
    - Facile = 15 bombes pour 64 cases ;
    - Normal = 30 bombes pour 96 cases ;
    - Difficile = 50 bombes pour 144 cases ;
    
    -- Défaite :
    - Le joueur détruit une case contenant une mine ;
    
    -Victoire :
    - Le joueur a découvert l'entièreté du tableau sans activer une seule mine ;
    """

    display_rules.insert(tk.END, long_texte)

    #bouton pour fermer la page des règles
    btn_exit = tk.Button(windows_rules, text="QUITTER", relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 25), command=exit_rules)
    btn_exit.pack()