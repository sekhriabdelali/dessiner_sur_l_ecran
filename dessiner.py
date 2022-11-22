import threading
import time
from tkinter import *


def dessiner(lock, color):
    # pour travailler avec les variables globales
    global x
    global y
    global nx

    # pour que les threads ne seront pas traités en FIFO
    time.sleep(0.1)
    # pour accepter un thread et déverouiller les autres
    lock.acquire()
    # pour changer les coordonnées des cercles
    x = x + 50
    # pour créer les cercles dans la bonne position
    mycanvas.create_oval(100+x, 50+y, 50+x, 100+y, fill=color)
    # pour le nombre des cercles de la meme ligne
    nx = nx + 1
    # si on arrive à 10 cercles par ligne :
    if nx == 10:
        # pour faire une nouvelle ligne
        x = 0
        y = y + 50
        # pour recalculer le nombre des cercles par ligne
        nx = 0

    # pour voir le déroulement (on peut l'enlever)
    time.sleep(0.1)
    # pour vérouiller le thread actuel et dévérouiller un autre
    lock.release()


def main_task():

    for _ in range(30):
        # pour la création des threads
        t1 = threading.Thread(target=dessiner, name='t1', args=(lock, "green"))
        t2 = threading.Thread(target=dessiner, name='t2', args=(lock, "red"))
        t3 = threading.Thread(target=dessiner, name='t3', args=(lock, "blue"))
        # pour commencer les threads
        t1.start()
        t2.start()
        t3.start()


if __name__ == "__main__":

    # il faut déclarer les variables utiliser dans le programme globalement
    x = 0
    y = 0
    nx = 0
    # pour créer la fenetre
    fenetre = Tk()
    # pour les info de la fenetre
    fenetre.title("Tp3")
    fenetre.configure(bg='white', width=700, height=250)
    # pour créer le lock
    lock = threading.Lock()
    # pour créer le canvas
    mycanvas = Canvas(fenetre, width=1000, height=800, bg='#f5f0e1')
    mycanvas.create_rectangle(100, 50, 600, 500, width=3)
    mycanvas.pack()
    # pour la création des bouttons
    button1 = Button(fenetre, text='test', font=(
        "Myriad Arabic", 12), command=main_task)
    button1.config(bg='#1e3d59', fg='white', width=20, height=3)
    button1.place(x=750, y=40)

    fenetre.mainloop()
