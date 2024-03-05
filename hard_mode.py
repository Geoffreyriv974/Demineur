import random
import tkinter as tk

#importation des images
photo_yes = tk.PhotoImage(file="image/emoji_content.png")
photo_no = tk.PhotoImage(file="image/emoji_triste.png")
emoji_win = tk.PhotoImage(file="image/emoji_win.png")

photo_flag = tk.PhotoImage(file="image/drapeau.png")
photo_question = tk.PhotoImage(file="image/interogation.png")
end_game = tk.PhotoImage(file="image/bombe.png")
gris = tk.PhotoImage(file="image/gris.png")
croix = tk.PhotoImage(file="image/close.png")
photo_flag2 = tk.PhotoImage(file="image/drapeau2.png")
photo_question2 = tk.PhotoImage(file="image/interogation2.png")

un = tk.PhotoImage(file="image/un.png")
deux = tk.PhotoImage(file="image/deux.png")
trois = tk.PhotoImage(file="image/trois.png")
quatre = tk.PhotoImage(file="image/quatre.png")
cinq = tk.PhotoImage(file="image/cinq.png")
six = tk.PhotoImage(file="image/six.png")
sept = tk.PhotoImage(file="image/sept.png")
huit = tk.PhotoImage(file="image/huit.png")
bombe_v = tk.PhotoImage(file="image/bombe_vert.png")

def hard():
    global bombe_in_game
    bombe_in_game = 50

    windows_hard = tk.Toplevel(bg="#B1A8A8")
    windows_hard.attributes('-fullscreen', True)

    def restart():
        windows_hard.destroy()
        hard()

    global nb_score
    nb_score = 0

    # frame pour séparer les 2 parties
    frame = tk.Frame(windows_hard)
    frame.pack(anchor="n",)

    frame1 = tk.Frame(windows_hard, borderwidth=10, background="#B1A8A8", relief="sunken")
    frame1.pack(anchor="n", ipadx=150, pady=10)

    frame2 = tk.Frame(windows_hard, borderwidth=10, background="#B1A8A8", relief="sunken")
    frame2.pack(anchor="n")

    # affichage du score
    score = tk.Label(frame1, background="black", borderwidth=5, width=3, text="0", fg="blue", font=("Retro Gaming", 20))
    score.pack(side="right", padx=5, pady=5)

    # affichage du nombre de bombe en jeu
    bombe = tk.Label(frame1, background="black", borderwidth=5, width=3, text=bombe_in_game, fg="blue", font=("retro Gaming", 20))
    bombe.pack(side="left", padx=5, pady=5)

    # affichage de l'émoji
    face = tk.Button(frame1, padx=20, pady=10, relief="raised", borderwidth=5, image=photo_yes, command=restart)
    face.pack(pady=5)

    #fonction pour afficher les drapeaux
    def flag(event):
        global bombe_in_game
        if bombe_in_game == 0:
            return
        if event.widget.cget("state") == "disabled":
            return
        bombe_in_game = bombe_in_game - 1
        event.widget.config(image=photo_flag)
        bombe.config(text=bombe_in_game)
        event.widget.config(state='disabled')

    # fonction pour retirer les drapeaux
    def reset(event):
        global bombe_in_game
        if bombe_in_game == 15:
            return
        event.widget.config(image=gris)
        bombe_in_game = bombe_in_game + 1
        bombe.config(text=bombe_in_game)
        event.widget.config(state='normal')

    #fonction pour afficher le point d'interrogation
    def interrogation(event):
        if event.widget.cget("image") == photo_flag:
            return
        if event.widget.cget("state") == "disabled":
            return
        event.widget.config(image=photo_question)

    #foction pour fermer la fenêtre
    def exit_windows():
        windows_hard.destroy()


    #fonction qui gère les different possibilité de résultat quand on clique sur un des bouton dans le jeu.
    def onclik(i,j,plateau_de_bombe, plateau_win):
        global nb_score

        # on verifie si on appuie sur une case avec une bombe
        if plateau_de_bombe[i][j]==9:
            #on parcour tous le tableau
            for i1, row in enumerate(plateau_de_bombe):
                for j1, value, in enumerate(row):
                    case = plateau_de_jeu[i1][j1]
                    case.config(state='disabled')
                    if plateau_de_bombe[i1][j1] == 9:
                        case = plateau_de_jeu[i1][j1]
                        case.config(image=end_game, relief="sunken")
                        case.image=end_game
            appel_score = tk.IntVar()
            appel_score.set(nb_score)
            face.config(image=photo_no)

            def loose():

                global score_sql, btn_save

                final_no = tk.Label(windows_hard, text="GAME OVER", bg="#B1A8A8", fg="blue", font=("Retro Gaming", 55))
                final_no.pack()

                frame_loose_score = tk.Frame(windows_hard)
                frame_loose_score.pack()

                display_score = tk.Label(frame_loose_score, text="Ton Score :", bg="#B1A8A8", fg="blue", font=("Retro Gaming", 30))
                display_score.pack(side="left")
                display_score_number = tk.Label(frame_loose_score, textvariable=appel_score, bg="#B1A8A8", fg="blue", font=("Retro Gaming", 30))

                score_sql = display_score_number.cget("text")

                display_score_number.pack(side="right")

                exit_game = tk.Button(windows_hard, text="QUITTER", pady=11, relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 18), command=exit_windows)
                exit_game.pack()

            global name_player_label

            def confirme_entry():
                name_player_label.config(text=name_player.get())

                btn_valid_entry.destroy()
                name_player.destroy()

                loose()

            def replace_entry(event):
                if name_player.get() == "Entrez votre pseudo...":
                    name_player.delete(0, "end")

            name_player = tk.Entry(windows_hard, font=("yellowstone", 20), borderwidth=4, fg="gray", bg="white")
            name_player.pack(pady=10)
            name_player.insert(0, "Entrez votre pseudo...")

            name_player.bind("<FocusIn>", replace_entry)

            btn_valid_entry = tk.Button(windows_hard, command=confirme_entry, text="Valider", relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 25))
            btn_valid_entry.pack(pady=10)

            frame_name_score = tk.Frame(windows_hard, bg="#B1A8A8")
            frame_name_score.pack()

            name_player_label = tk.Label(frame_name_score, font=("yellowstone", 20), borderwidth=4, fg="blue", bg="#B1A8A8")
            name_player_label.pack(side="left")

            btn_exit_game.destroy()

            cadre_interrogation.destroy()
            cadre_flags.destroy()
            cadre_suppr_affiche.destroy()

        if plateau_de_bombe[i][j]==1:
            case = plateau_de_jeu[i][j]
            case.config(image=un, relief="sunken", state='disabled')
            nb_score = nb_score +10
            plateau_win[i][j] = -1

        elif plateau_de_bombe[i][j]==2:
            case = plateau_de_jeu[i][j]
            case.config(image=deux, relief="sunken", state='disabled')
            nb_score = nb_score + 20
            plateau_win[i][j] = -1

        elif plateau_de_bombe[i][j]==3:
            case = plateau_de_jeu[i][j]
            case.config(image=trois, relief="sunken", state='disabled')
            nb_score = nb_score + 30
            plateau_win[i][j] = -1

        elif plateau_de_bombe[i][j]==4:
            case = plateau_de_jeu[i][j]
            case.config(image=quatre, relief="sunken", state='disabled')
            nb_score = nb_score + 40
            plateau_win[i][j] = -1

        elif plateau_de_bombe[i][j]==5:
            case = plateau_de_jeu[i][j]
            case.config(image=cinq, relief="sunken", state='disabled')
            nb_score = nb_score + 50
            plateau_win[i][j] = -1

        elif plateau_de_bombe[i][j]==6:
            case = plateau_de_jeu[i][j]
            case.config(image=six, relief="sunken", state='disabled')
            nb_score = nb_score + 60
            plateau_win[i][j] = -1

        elif plateau_de_bombe[i][j]==7:
            case = plateau_de_jeu[i][j]
            case.config(image=sept, relief="sunken", state='disabled')
            nb_score = nb_score + 70
            plateau_win[i][j] = -1

        elif plateau_de_bombe[i][j]==8:
            case = plateau_de_jeu[i][j]
            case.config(image=huit, relief="sunken", state='disabled')
            nb_score = nb_score + 80
            plateau_win[i][j] = -1

        elif plateau_de_bombe[i][j]==0:
            nb_score = nb_score + 90
            plateau_win[i][j] = -1
            case = plateau_de_jeu[i][j]
            case.config(relief="sunken", state='disabled')

        # vérification de la victoire
        if verif(plateau_win) == True:
            case.config(state='disabled')
            face.config(image=emoji_win)
            nb_score = nb_score + 100
            for i1, row in enumerate(plateau_de_bombe):
                for j1, value, in enumerate(row):
                    case = plateau_de_jeu[i1][j1]
                    if plateau_de_bombe[i1][j1] == 9:
                        case = plateau_de_jeu[i1][j1]
                        case.config(image=bombe_v, relief="sunken")
            appel_score = tk.IntVar()
            appel_score.set(nb_score)

            def win():

                global score_sql, btn_save

                final_yes = tk.Label(windows_hard, text="WINNER", bg="#B1A8A8", fg="blue", font=("Retro Gaming", 55))
                final_yes.pack()

                frame_win_score = tk.Frame(windows_hard)
                frame_win_score.pack()

                display_score = tk.Label(frame_win_score, text="Ton Score :", bg="#B1A8A8", fg="blue",
                                         font=("Retro Gaming", 30))
                display_score.pack(side="left")
                display_score_number = tk.Label(frame_win_score, textvariable=appel_score, bg="#B1A8A8", fg="blue",
                                                font=("Retro Gaming", 30))

                score_sql = display_score_number.cget("text")

                display_score_number.pack(side="right")

                exit_game = tk.Button(windows_hard, text="QUITTER", pady=11, relief="raised", bg="#B1A8A8", fg="blue",
                                      borderwidth=5, font=("Retro Gaming", 18), command=exit_windows)
                exit_game.pack()

            def confirme_entry():
                name_player_label.config(text=name_player.get())

                btn_valid_entry.destroy()
                name_player.destroy()

                win()

            def replace_entry(event):
                if name_player.get() == "Entrez votre pseudo...":
                    name_player.delete(0, "end")

            name_player = tk.Entry(windows_hard, font=("yellowstone", 20), borderwidth=4, fg="gray", bg="white")
            name_player.pack(pady=10)
            name_player.insert(0, "Entrez votre pseudo...")

            name_player.bind("<FocusIn>", replace_entry)

            btn_valid_entry = tk.Button(windows_hard, command=confirme_entry, text="Valider", relief="raised",
                                        bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 25))
            btn_valid_entry.pack(pady=10)

            frame_name_score = tk.Frame(windows_hard, bg="#B1A8A8")
            frame_name_score.pack()

            name_player_label = tk.Label(frame_name_score, font=("yellowstone", 20), borderwidth=4, fg="blue",
                                         bg="#B1A8A8")
            name_player_label.pack(side="left")

            btn_exit_game.destroy()

            cadre_interrogation.destroy()
            cadre_flags.destroy()
            cadre_suppr_affiche.destroy()

        score.config(text=nb_score)


    def exit_in_game():
        windows_hard.destroy()

    btn_exit_game = tk.Button(windows_hard, text="QUITTER", pady=11, relief="raised", bg="#B1A8A8", fg="blue",borderwidth=5, font=("Retro Gaming", 18), command=exit_in_game)
    btn_exit_game.pack(pady=30)

    cadre_interrogation = tk.Frame(windows_hard, bg="#B1A8A8")
    cadre_interrogation.pack()
    affiche_interrogation = tk.Label(cadre_interrogation, image=photo_question2, bg="#B1A8A8")
    affiche_interrogation.pack(side="left", padx=20)
    texte_interrogation = tk.Label(cadre_interrogation, text="Clique droit", bg="#B1A8A8", font=("Retro Gaming", 11))
    texte_interrogation.pack(side="right")

    cadre_flags = tk.Frame(windows_hard, bg="#B1A8A8")
    cadre_flags.pack()
    affiche_flags = tk.Label(cadre_flags, image=photo_flag2, bg="#B1A8A8")
    affiche_flags.pack(side="left", padx=20)
    texte_flags = tk.Label(cadre_flags, text="Double clique droit", bg="#B1A8A8", font=("Retro Gaming", 11))
    texte_flags.pack(side="right")

    cadre_suppr_affiche = tk.Frame(windows_hard, bg="#B1A8A8")
    cadre_suppr_affiche.pack()
    suppr_affiche = tk.Label(cadre_suppr_affiche, image=croix, bg="#B1A8A8")
    suppr_affiche.pack(side="left", padx=20)
    texte_suppr_affiche = tk.Label(cadre_suppr_affiche, text="Ctrl + Clic droit", bg="#B1A8A8",font=("Retro Gaming", 11))
    texte_suppr_affiche.pack(side="right")

    nb_bombe = 50
    nb_bombe_actuel = 0
    plateau_de_bombe = [[0 for j in range(18)] for i in range(8)]
    #boucle qui va placer le nombre de bombe en vérifiant qu'il y en ai assee
    while nb_bombe_actuel < nb_bombe:
        position_bombe_row = random.randint(0, 7)
        position_bombe_column = random.randint(0, 17)

        if plateau_de_bombe[position_bombe_row][position_bombe_column] != 9:
            plateau_de_bombe[position_bombe_row][position_bombe_column] = 9
            nb_bombe_actuel += 1

    # bouton du jeu
    plateau_de_jeu = []
    hauteur = 8
    largeur = 18

    def generate_number(tableau_de_bombe):
        ligne = len(tableau_de_bombe)
        colonne = len(tableau_de_bombe[0])
        #création de toute les case en fonction du nombre de lignes et colonnes
        for i in range(ligne):
            for j in range(colonne):
                if tableau_de_bombe[i][j] == 9:
                    for i2 in range(i - 1, i + 2):
                        for j2 in range(j - 1, j + 2):
                            if 0 <= i2 < ligne and 0 <= j2 < colonne and plateau_de_bombe[i2][j2] != 9:
                                plateau_de_bombe[i2][j2] += 1
        return tableau_de_bombe

    #creation du tableau pour vérifier si on a découvert tout les case sauf les bombes
    plateau_win = [[0 for j in range(18)] for i in range(8)]
    for i, row in enumerate(plateau_de_bombe):
        for j, value in enumerate(row):
            plateau_win[i][j] = value

    # marque un marquer (-1) sur toute les cases ou il n'y a pas de bombe
    def verif(plateau_win):
        compteur = 0
        for i, row in enumerate(plateau_win):
            for j, value in enumerate(row):
                if plateau_win[i][j] == -1:
                    compteur += 1
        if compteur == 94:
            return True
        else:
            return False

    #genération de toute les cases du plateau de jeux
    for i in range(hauteur):
        row = []
        for j in range(largeur):
            case = tk.Button(frame2, padx=22, pady=12, relief="raised", background="#B1A8A8", borderwidth=5, command=lambda i=i, j=j: onclik(i,j,plateau_de_bombe, plateau_win))
            case.grid(column=j, row=i)
            case.bind("<Double-Button-3>", flag)
            case.bind("<Control-Button-3>", reset)
            case.bind("<Button-3>", interrogation)
            row.append(case)
        plateau_de_jeu.append(row)

    plateau_de_bombe = generate_number(plateau_de_bombe)

    for row in plateau_de_bombe:
        print(row)
    print("\n 1 \n")

    for row in plateau_win:
        print(row)