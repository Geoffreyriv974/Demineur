import tkinter as tk
import pygame


def main():
    pygame.mixer.init()
    pygame.mixer.music.load("musique/musique_de_fond.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.config(bg="#B1A8A8")

    pioche_droite = tk.PhotoImage(file="image/Pioche_en_diamant_droite.png")
    pioche_gauche = tk.PhotoImage(file="image/Pioche_en_diamant_gauche.png")

    pchg = tk.Label(root, image=pioche_gauche, bg="#B1A8A8")
    pchg.pack(side="left")
    pchd = tk.Label(root, image=pioche_droite, bg="#B1A8A8")
    pchd.pack(side="right")

    def exit():
        root.destroy()

    def display_rules():
        import rules
        rules.rules()

    def start_diff():
        import difficulty
        difficulty.choice_dif()

    name = tk.Label(root, text="DEMINEUR", fg="blue", bg="#B1A8A8", font=("Retro Gaming", 50))
    name.pack(ipady=100)

    frame_btn_1 = tk.Frame(root, bg="#B1A8A8")
    frame_btn_1.pack()
    frame_btn_2 = tk.Frame(root, bg="#B1A8A8")
    frame_btn_2.pack()
    frame_btn_3 = tk.Frame(root, bg="#B1A8A8")
    frame_btn_3.pack()

    btn_game = tk.Button(frame_btn_1, text="JOUER", relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 25), command=start_diff)
    btn_game.pack(side="left", ipadx=25)

    btn_rules = tk.Button(frame_btn_1, text="RÉGLES", relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 25), command=display_rules)
    btn_rules.pack(side="right", ipadx=25)

    btn_exit = tk.Button(frame_btn_3, text="QUITTER", pady=11, relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 18), command=exit)
    btn_exit.pack()

    def activate():
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        act.config(relief="sunken")
        desact.config(relief="raised")

    def desactivate():
        pygame.mixer.music.stop()
        act.config(relief="raised")
        desact.config(relief="sunken")

    photo_activate = tk.PhotoImage(file="image/activer.png")
    photo_desactivate = tk.PhotoImage(file="image/desactiver.png")

    frame = tk.Frame(root, bg="#B1A8A8")
    frame.pack(pady=40)

    act = tk.Button(frame, relief="sunken", bg="#B1A8A8", fg="blue", borderwidth=5, padx=20, pady=13, image=photo_activate, command=activate)
    act.pack(side=tk.LEFT)
    desact = tk.Button(frame, relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5, padx=20, pady=13, image=photo_desactivate, command=desactivate)
    desact.pack(side=tk.LEFT)

    root.mainloop()


if __name__ == "__main__":
    main()
