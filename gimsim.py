import tkinter as tk
# import filedialog module
from tkinter import filedialog

from tkinter import ttk
from tkinter.messagebox import showinfo

import os

from settings import Settings
from imsim import Imsim

GIMSIM_VERSION = "1.0.0"
GIMSIM_VERSION_DATE = "23/07/2022"

# Construction de la fenêtre principale «root»
root = tk.Tk()
#root.geometry("300x150")
root.resizable(False, False)
root.title('ImSim : Image simulation')

# Variable global tk
setting_path = tk.StringVar()
snr_val = tk.DoubleVar()
exp_time_in = tk.DoubleVar()
mag_lim_res = tk.StringVar()
mag_lim_in = tk.DoubleVar()
exp_time_res = tk.StringVar()
config_val = tk.StringVar()

# Init values
snr_val.set(7)
def_conf_file = "C:/Users/leymar/PycharmProjects/imsim/test/imsim_conf_unitest.yml"
setting_path.set(def_conf_file)
setting = Settings(def_conf_file)
config_val.set("tesca_1")
imsim = Imsim(setting, config_val.get())


# Definition des fonctions
def load_conf():
    """load the settings value for class source
        Args :
        Returns :
    """
    global imsim
    conf_file = setting_path.get()
    settings = Settings(conf_file)
    imsim = Imsim(settings, config_val.get())


# Fonction pour la fenaitre de l'explorateur
def browsefiles():
    cwd = os.getcwd()
    filename = filedialog.askopenfilename(initialdir=cwd,
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.yml*"),
                                                     ("all files",
                                                      "*.*")))
    # Change label contents
    setting_path.set(filename)


def aproposgest():
    """ callback when the about button clicked
    """
    global GIMSIM_VERSION, imsim
    showinfo(
        title='Gimsim version',
        message="## GImSim version : " + GIMSIM_VERSION + "  ## Imsim version : " + imsim.get_version()
    )


def gen_mag_lim():
    """ callback when the mag_lim button clicked
    """
    global imsim
    snr = snr_val.get()
    exp_time = exp_time_in.get()
    mag_lim = imsim.limit_mag_from_snr_exposure_time(snr, exp_time)
    mag_lim_res.set(mag_lim)


def gen_exp_time():
    """ callback when the mag_lim button clicked
    """
    global imsim
    snr = snr_val.get()
    mag_lim = mag_lim_in.get()
    exp_time = imsim.exposure_time_from_snr_mag(snr, mag_lim)
    exp_time_res.set(exp_time)

# Construction de la barre de menu
menuBar = tk.Menu(root)
root['menu'] = menuBar

# Définition des variables
sousMenu1 = tk.Menu(menuBar)
menuBar.add_cascade(label='File', menu=sousMenu1)
sousMenu1.add_command(label='Open', command=browsefiles)
sousMenu1.add_separator()
sousMenu1.add_command(label='Quit', command=root.quit)
sousMenu2 = tk.Menu(menuBar)
menuBar.add_cascade(label='Aide', menu=sousMenu2)
sousMenu2.add_command(label='About', command=aproposgest)

# Configuration des frames
frame_config = tk.LabelFrame(root, text="Configuration")
frame_snr = tk.Frame(root)
frame_mag_lim = tk.LabelFrame(root, text="Limit Magnitude")
frame_exp_time = tk.LabelFrame(root, text="Exposure time")

# Construction widget
setting_path_label_l = tk.Label(frame_config, text="Setting file path : ")
setting_path_l = tk.Label(frame_config, textvariable=setting_path)
config_l = tk.Label(frame_config, text="Config : ")
config_e = tk.Entry(frame_config, textvariable=config_val)
reload_b = tk.Button(frame_config, text='reload', command=load_conf)

snr_l = tk.Label(frame_snr, text="SNR :")
snr_e = tk.Entry(frame_snr, textvariable=snr_val)

exp_time_in_l = tk.Label(frame_mag_lim, text="Exposure time (s)")
exp_time_in_e = tk.Entry(frame_mag_lim, textvariable=exp_time_in)
mag_lim_res_l = tk.Label(frame_mag_lim, text="Limit mag")
mag_lim_res_e = tk.Entry(frame_mag_lim, textvariable=mag_lim_res)
mag_lim_b = tk.Button(frame_mag_lim, text='Calculate limit mag', command=gen_mag_lim, width=20)

mag_lim_in_l = tk.Label(frame_exp_time, text="Limit mag")
mag_lim_in_e = tk.Entry(frame_exp_time, textvariable=mag_lim_in)
exp_time_res_l = tk.Label(frame_exp_time, text="Exposure time (s)")
exp_time_res_e = tk.Entry(frame_exp_time, textvariable=exp_time_res)
exp_time_b = tk.Button(frame_exp_time, text='Calculate exposure time', command=gen_exp_time, width=20)



# Placement du bouton dans «root»
frame_config.grid(row=0, column=0, sticky="w", columnspan=3, padx=5, pady=5)
frame_snr.grid(row=1, column=0, sticky="w", columnspan=3, padx=5, pady=5)
frame_mag_lim.grid(row=2, column=0, sticky="w", columnspan=3, padx=5, pady=5)
frame_exp_time.grid(row=3, column=0, sticky="w", columnspan=3, padx=5, pady=5)

setting_path_label_l.grid(row=0, column=0, sticky="e")
setting_path_l.grid(row=0, column=1, columnspan=3, sticky="nsew")
config_l.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
config_e.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
reload_b.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

snr_l.grid(row=0, column=0, sticky="e")
snr_e.grid(row=0, column=1, sticky="nsew")

exp_time_in_l.grid(row=0, column=0, sticky="nsew")
exp_time_in_e.grid(row=1, column=0, sticky="nsew")
mag_lim_res_l.grid(row=0, column=2, sticky="nsew")
mag_lim_res_e.grid(row=1, column=2, sticky="nsew")
mag_lim_b.grid(row=1, column=1, sticky="nsew")

mag_lim_in_l.grid(row=0, column=0, sticky="nsew")
mag_lim_in_e.grid(row=1, column=0, sticky="nsew")
exp_time_res_l.grid(row=0, column=2, sticky="nsew")
exp_time_res_e.grid(row=1, column=2, sticky="nsew")
exp_time_b.grid(row=1, column=1, sticky="nsew")

# Lancement de la «boucle principale»
root.mainloop()