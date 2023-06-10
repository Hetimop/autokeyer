import tkinter as tk
from tkinter import ttk
import pyautogui
import threading
import random
import pygetwindow as gw

# Fonction pour effectuer les frappes de touches automatiques
def auto_key_press():
    window_title = window_var.get()  # Obtenir le titre de la fenêtre à partir du menu déroulant
    keys_to_press = keys_entry.get()  # Obtenir les touches à partir de l'entrée de l'utilisateur
    base_delay = float(delay_entry.get())  # Obtenir le délai de répétition de base
    random_delay = float(random_delay_entry.get())  # Obtenir le délai aléatoire à ajouter

    # Récupérer la fenêtre spécifiée par son titre
    window = gw.getWindowsWithTitle(window_title)[0]

    # Fonction exécutée pour effectuer les frappes de touches automatiques en boucle
    def auto_key_press_loop():
        while running:
            window.activate()  # Activer la fenêtre spécifiée avant de simuler la frappe de touche
            for key in keys_to_press:
                pyautogui.press(key)
                if not running:
                    break
            if not running:
                break
            delay = base_delay + random.uniform(0, random_delay)  # Ajouter un délai aléatoire
            pyautogui.PAUSE = delay

    # Démarrer l'exécution des frappes de touches automatiques dans la fenêtre spécifiée
    global running
    running = True
    start_button.config(state=tk.DISABLED)  # Désactiver le bouton "Démarrer"
    stop_button.config(state=tk.NORMAL)  # Activer le bouton "Arrêter"
    thread = threading.Thread(target=auto_key_press_loop)
    thread.start()

# Fonction pour arrêter l'exécution des frappes de touches
def stop_auto_key_press():
    global running
    running = False
    start_button.config(state=tk.NORMAL)  # Activer le bouton "Démarrer"
    stop_button.config(state=tk.DISABLED)  # Désactiver le bouton "Arrêter"

# Créer la fenêtre principale
window = tk.Tk()
window.title("Hetimop Key Presser")
window.geometry("320x220")  # Définir la taille fixe de la fenêtre
window.resizable(False, False)  # Rendre la taille de la fenêtre non modifiable

# Créer les éléments de l'interface graphique
window_label = tk.Label(window, text="Titre de la fenêtre :")
window_label.pack()

# Obtenir les titres de toutes les fenêtres
window_titles = gw.getAllTitles()

window_var = tk.StringVar(window)
window_dropdown = ttk.Combobox(window, textvariable=window_var, values=window_titles)
window_dropdown.pack()

keys_label = tk.Label(window, text="Touches à appuyer :")
keys_label.pack()

keys_entry = tk.Entry(window)
keys_entry.pack()

delay_label = tk.Label(window, text="Délai de répétition (en secondes) :")
delay_label.pack()

delay_entry = tk.Entry(window)
delay_entry.pack()

random_delay_label = tk.Label(window, text="Délai aléatoire (en secondes) :")
random_delay_label.pack()

random_delay_entry = tk.Entry(window)
random_delay_entry.pack()

start_button = tk.Button(window, text="Démarrer", command=auto_key_press)
start_button.pack()

stop_button = tk.Button(window, text="Arrêter", command=stop_auto_key_press, state=tk.DISABLED)
stop_button.pack()

# Lancer la boucle principale de l'interface graphique
window.mainloop()