import math
import numbers
from src import element


class Source(element.Element):
    """
        Source is an object that represent the source object
    """
    SETTING_PATH_ROOT = "SOURCE"
    SETTING_DEFAULT_NAME = "DEFAULT"

    def __init__(self, settings, name):
        """init for Source
            Args :
                setting (Settings) : setting for source
                name (str) : name of the configuration in setting file
        """

        # Init
        self.abs_stellar_mag = None  # Absolut stellar magnitude
        self.dl_mpc = None  # Distance luminosity in Mpc
        self.app_stellar_mag = None  # Apparent stellar magnitude
        self.ph_band = None  # Photometric Band (B, V, R, I, C)
        self.ph_band_list = ["B", "V", "R", "I", "C"]

        super().__init__(settings, name)
        if self.name is not None:
            self.setting_status = self.load_settings()

    def __str__(self):
        return str(self.str)

    def __update_app_stellar_mag(self):
        """update all value for class source
            Args :
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if self.abs_stellar_mag is None:
            return False
        if self.dl_mpc is None:
            return False

        dl = self.dl_mpc * 1E5
        self.app_stellar_mag = float(self.abs_stellar_mag + 5 * math.log10(dl))
        return True

    def update(self):
        """update all value for class source
            Args :
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        return self.__update_app_stellar_mag()

    def load_settings(self):
        """load the settings value for class source
            Args :
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.setting_status = False
        if not super()._check_settings():
            return False
        return_val = True

        if not self.set_app_stellar_mag(self.local_setting.get_setting([self.name, "app_stellar_mag"])):
            if not self.set_abs_stellar_mag(self._get_setting_val("abs_stellar_mag")):
                return_val = False
            if not self.set_dl_mpc(self._get_setting_val("dl_mpc")):
                return_val = False
        if not self.set_ph_band(self._get_setting_val("ph_band")):
            return_val = False
        self.setting_status = return_val
        return return_val

    def set_abs_stellar_mag(self, abs_stellar_mag):
        """set_abs_stellar_mag set abs_stellar_mag value
            Args :
                abs_stellar_mag (numbers) : value for abs_stellar_mag
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if isinstance(abs_stellar_mag, numbers.Number):
            self.abs_stellar_mag = float(abs_stellar_mag)
            return True
        elif abs_stellar_mag is None:
            self.abs_stellar_mag = None
            return True

        self.logger.warning("Invalid absolut stellar magnitude {} must be e number".format(abs_stellar_mag))
        return False

    def set_dl_mpc(self, dl_mpc):
        """set_dl_mpc set the distance light in Mpc
            Args :
                dl_mpc (numbers) : value for dl_mpc
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if isinstance(dl_mpc, numbers.Number):
            self.dl_mpc = float(dl_mpc)
            return True
        elif dl_mpc is None:
            self.dl_mpc = None
            return True
        self.logger.warning("Invalid distance luminosity {} must be e number".format(dl_mpc))
        return False

    def set_app_stellar_mag(self, app_stellar_mag):
        """set_dl_mpc set the apparent stellar magnitude
            Args :
                app_stellar_mag (numbers) : value for app_stellar_mag
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if isinstance(app_stellar_mag, numbers.Number):
            self.set_abs_stellar_mag(None)
            self.set_dl_mpc(None)
            self.app_stellar_mag = float(app_stellar_mag)
            return True
        elif app_stellar_mag is not None:
            self.logger.warning("Invalid apparent stellar magnitude {} must be e number".format(app_stellar_mag))
        return False

    def set_ph_band(self, ph_band):
        """set_dl_mpc set the photometric band
            Args :
                ph_band (numbers) : value for ph_band
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if ph_band in self.ph_band_list:
            self.ph_band = ph_band
            return True
        self.logger.warning("Invalid photometric band {} must be in {}".format(ph_band, self.ph_band_list))
        return False

    def get_abs_stellar_mag(self):
        """set_abs_stellar_mag set set abs_stellar_mag set value
            Args :
            Returns :
                abs_stellar_mag (float) : return abs_stellar_mag value
        """
        return self.abs_stellar_mag

    def get_dl_mpc(self):
        """get_dl_mpc get the distance light in Mpc
            Args :
            Returns :
                dl_mpc (float) : return dl_mpc value
        """
        return self.dl_mpc

    def get_app_stellar_mag(self):
        """get_app_stellar_mag get the apparent stellar magnitude
            Args :
            Returns :
                app_stellar_mag (float) : return app_stellar_mag value
        """
        self.__update_app_stellar_mag()
        return self.app_stellar_mag

    def get_ph_band(self):
        """get_ph_band get the photometric band
            Args :
            Returns :
                ph_band (float) : return ph_band value
        """
        return self.ph_band

    def get_ph_band_list(self):
        """get_ph_band_list get the list of available photometric band
            Args :
            Returns :
                ph_band_list (float) : return ph_band_list value
        """
        return self.ph_band_list
