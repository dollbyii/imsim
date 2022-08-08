import tkinter as tk
# import filedialog module
from tkinter import filedialog
from tkinter import ttk

from tkinter.messagebox import showinfo

import os

from src.settings import Settings
from imsim import Imsim

GIMSIM_VERSION = "2.0.0"
GIMSIM_VERSION_DATE = "05/08/2022"

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
selected_config = tk.StringVar()
config_err_msg = tk.StringVar()
custom_config_val = tk.IntVar()

selected_camera = tk.StringVar()
selected_observatory = tk.StringVar()
selected_optic = tk.StringVar()
selected_filter = tk.StringVar()


# Init values
snr_val.set(7)
def_conf_file = ""
setting_path.set(def_conf_file)


# Definition des fonctions
def load_conf():
    """load the settings value for class source
        Args :
        Returns :
    """
    global imsim
    conf_file = setting_path.get()
    settings = Settings(conf_file)
    imsim = Imsim(settings, selected_config.get())
    if custom_config_val.get() == 1:
        imsim.set_camera(selected_camera.get())
        imsim.set_observatory(selected_observatory.get())
        imsim.set_optic(selected_optic.get())
        imsim.set_filter(selected_filter.get())
    else:
        selected_camera.set(imsim.get_camera().get_name())
        selected_optic.set(imsim.get_optic().get_name())
        selected_observatory.set(imsim.get_observatory().get_name())
        selected_filter.set(imsim.get_filter().get_name())
    if not imsim.setting_status:
        config_err_msg.set("Confuguration error")
    else:
        config_err_msg.set("")


def update_conf():
    """update the settings value
        Args :
        Returns :
    """
    global imsim
    conf_file = setting_path.get()
    if os.path.exists(conf_file):
        settings = Settings(conf_file)
        config_cb['values'] = list(settings.get_setting(["IMSIM"]).keys())
        camera_cb['values'] = list(settings.get_setting(["CAMERA"]).keys())
        observatory_cb['values'] = list(settings.get_setting(["OBSERVATORY"]).keys())
        optic_cb['values'] = list(settings.get_setting(["OPTIC"]).keys())
        filter_cb['values'] = list(settings.get_setting(["FILTER"]).keys())
        config_err_msg.set("")
    elif conf_file == "":
        config_err_msg.set("No config file !")
    else:
        config_err_msg.set("Config file doesn't exist !")
    update_config_display()


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
    if os.path.exists(filename):
        setting_path.set(filename)
        update_conf()


def aproposgest():
    """ callback when the about button clicked
    """
    global GIMSIM_VERSION
    showinfo(
        title='Gimsim version',
        message="## GImSim version : " + GIMSIM_VERSION + "  ## Imsim version : " + Imsim.VERSION
    )

def update_config_display():
    """ callback when custom_config_ch checkbutone is modified
    """
    if os.path.exists(setting_path.get()):
        if custom_config_val.get() == 1:
            config_cb['state'] = 'disabled'
            camera_cb['state'] = 'active'
            observatory_cb['state'] = 'active'
            optic_cb['state'] = 'active'
            filter_cb['state'] = 'active'
        else:
            config_cb['state'] = 'active'
            camera_cb['state'] = 'disabled'
            observatory_cb['state'] = 'disabled'
            optic_cb['state'] = 'disabled'
            filter_cb['state'] = 'disabled'
    else:
        config_cb['state'] = 'disabled'
        camera_cb['state'] = 'disabled'
        observatory_cb['state'] = 'disabled'
        optic_cb['state'] = 'disabled'
        filter_cb['state'] = 'disabled'

def gen_mag_lim():
    """ callback when the mag_lim button clicked
    """
    global imsim
    load_conf()
    snr = snr_val.get()
    exp_time = exp_time_in.get()
    mag_lim = imsim.limit_mag_from_snr_exposure_time(snr, exp_time)
    mag_lim_res.set(mag_lim)


def gen_exp_time():
    """ callback when the mag_lim button clicked
    """
    global imsim
    load_conf()
    snr = snr_val.get()
    mag_lim = mag_lim_in.get()
    exp_time = imsim.exposure_time_from_snr_mag(snr, mag_lim)
    exp_time_res.set(exp_time)

# Construction de la barre de menu
menuBar = tk.Menu(root)
root['menu'] = menuBar

# Définition des sous menus
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

# Construction widget config
setting_path_label_l = tk.Label(frame_config, text="Setting file path : ")
setting_path_e = tk.Entry(frame_config, textvariable=setting_path)
browse_b = tk.Button(frame_config, text='...', command=browsefiles)
update_b = tk.Button(frame_config, text='Update', command=update_conf)
config_l = tk.Label(frame_config, text="IMSIM config : ")
config_e = tk.Entry(frame_config, textvariable=config_val)
config_cb = ttk.Combobox(frame_config, textvariable=selected_config, values=[])
config_err_l = tk.Label(frame_config, textvariable=config_err_msg, fg="red")

custom_config_ch = tk.Checkbutton(frame_config, text="Config custom", command=update_config_display,
                                  variable=custom_config_val)

camera_l = tk.Label(frame_config, text="Camera : ")
camera_cb = ttk.Combobox(frame_config, textvariable=selected_camera, values=[])

observatory_l = tk.Label(frame_config, text="Observatory : ")
observatory_cb = ttk.Combobox(frame_config, textvariable=selected_observatory, values=[])

optic_l = tk.Label(frame_config, text="Optic : ")
optic_cb = ttk.Combobox(frame_config, textvariable=selected_optic, values=[])

filter_l = tk.Label(frame_config, text="Filter : ")
filter_cb = ttk.Combobox(frame_config, textvariable=selected_filter, values=[])

# Construction widget snr
snr_l = tk.Label(frame_snr, text="SNR :")
snr_e = tk.Entry(frame_snr, textvariable=snr_val)

# Construction widget mag_lim
exp_time_in_l = tk.Label(frame_mag_lim, text="Exposure time (s)")
exp_time_in_e = tk.Entry(frame_mag_lim, textvariable=exp_time_in)
mag_lim_res_l = tk.Label(frame_mag_lim, text="Limit mag")
mag_lim_res_e = tk.Entry(frame_mag_lim, textvariable=mag_lim_res, state="readonly")
mag_lim_b = tk.Button(frame_mag_lim, text='Calculate limit mag', command=gen_mag_lim, width=20)

# Construction widget exp_time
mag_lim_in_l = tk.Label(frame_exp_time, text="Limit mag")
mag_lim_in_e = tk.Entry(frame_exp_time, textvariable=mag_lim_in)
exp_time_res_l = tk.Label(frame_exp_time, text="Exposure time (s)")
exp_time_res_e = tk.Entry(frame_exp_time, textvariable=exp_time_res, state="readonly")
exp_time_b = tk.Button(frame_exp_time, text='Calculate exposure time', command=gen_exp_time, width=20)

# Placement des frames
frame_config.grid(row=0, column=0, sticky="w", columnspan=3, padx=5, pady=5)
frame_snr.grid(row=1, column=0, sticky="w", columnspan=3, padx=5, pady=5)
frame_mag_lim.grid(row=2, column=0, sticky="w", columnspan=3, padx=5, pady=5)
frame_exp_time.grid(row=3, column=0, sticky="w", columnspan=3, padx=5, pady=5)

# Placement des widget dans la frame config
setting_path_label_l.grid(row=0, column=0, sticky="e")
setting_path_e.grid(row=1, column=0, columnspan=2, sticky="nsew")
browse_b.grid(row=1, column=2, sticky="nsew")
update_b.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
config_l.grid(row=3, column=0, sticky="nse", padx=5, pady=5)
config_cb.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
config_err_l.grid(row=2, column=1, sticky="nsw", padx=5, pady=5)

custom_config_ch.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

camera_l.grid(row=5, column=0, sticky="nse", padx=5, pady=5)
camera_cb.grid(row=5, column=1, sticky="nsew", padx=5, pady=5)

observatory_l.grid(row=6, column=0, sticky="nse", padx=5, pady=5)
observatory_cb.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)

optic_l.grid(row=7, column=0, sticky="nse", padx=5, pady=5)
optic_cb.grid(row=7, column=1, sticky="nsew", padx=5, pady=5)

filter_l.grid(row=8, column=0, sticky="nse", padx=5, pady=5)
filter_cb.grid(row=8, column=1, sticky="nsew", padx=5, pady=5)

frame_config.columnconfigure(1, minsize=300)

# Placement des widget dans la frame config
snr_l.grid(row=0, column=0, sticky="e")
snr_e.grid(row=0, column=1, sticky="nsew")

# Placement des widget dans la frame mag_lim
exp_time_in_l.grid(row=0, column=0, sticky="nsew")
exp_time_in_e.grid(row=1, column=0, sticky="nsew")
mag_lim_res_l.grid(row=0, column=2, sticky="nsew")
mag_lim_res_e.grid(row=1, column=2, sticky="nsew")
mag_lim_b.grid(row=1, column=1, sticky="nsew")

# Placement des widget dans la frame exp_time
mag_lim_in_l.grid(row=0, column=0, sticky="nsew")
mag_lim_in_e.grid(row=1, column=0, sticky="nsew")
exp_time_res_l.grid(row=0, column=2, sticky="nsew")
exp_time_res_e.grid(row=1, column=2, sticky="nsew")
exp_time_b.grid(row=1, column=1, sticky="nsew")

# Init display
custom_config_ch.deselect()
update_config_display()

# Lancement de la «boucle principale»
root.mainloop()
