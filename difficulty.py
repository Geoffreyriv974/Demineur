import tkinter as tk
import easy_mode
import normal_mode
import hard_mode

easy = tk.PhotoImage(file="image/Pioche_facile.png")
normal = tk.PhotoImage(file="image/Pioche_normal.png")
hardcore = tk.PhotoImage(file="image/Pioche_difficile.png")

def choice_dif():
    dif_windows = tk.Toplevel(bg="#B1A8A8")
    dif_windows.config(pady=100)
    dif_windows.attributes('-fullscreen', True)

    def mode1():
        easy_mode.easy()

    def mode2():
        normal_mode.normal()

    def mode3():
        hard_mode.hard()


    def exit_diff():
        dif_windows.destroy()

    picture_frame = tk.Frame(dif_windows,  bg="#B1A8A8")
    picture_frame.pack(fill="x")

    pche = tk.Label(picture_frame, image=easy, bg="#B1A8A8")
    pche.pack(side="left", padx=100)
    pchn = tk.Label(picture_frame, image=normal, bg="#B1A8A8")
    pchn.pack(side="left")
    pchd = tk.Label(picture_frame, image=hardcore, bg="#B1A8A8")
    pchd.pack(side="right", padx=100)

    btn_frame = tk.Frame(dif_windows,  bg="#B1A8A8")
    btn_frame.pack(fill="x")

    btn_easy = tk.Button(btn_frame, text="FACILE", relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5,font=("Retro Gaming", 25), command=mode1)
    btn_easy.pack(side="left", padx=200)
    btn_normal = tk.Button(btn_frame, text="NORMAL", relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5,font=("Retro Gaming", 25), command=mode2)
    btn_normal.pack(side="left", padx=87)
    btn_hard = tk.Button(btn_frame, text="DIFFICILE", pady=11, relief="raised", bg="#B1A8A8", fg="blue", borderwidth=5,font=("Retro Gaming", 17), command=mode3)
    btn_hard.pack(side="right", padx=200)

    btn_exit = tk.Button(dif_windows, text="QUITTER", relief="raised", pady=11, bg="#B1A8A8", fg="blue", borderwidth=5, font=("Retro Gaming", 18), command=exit_diff)
    btn_exit.pack(pady=50)