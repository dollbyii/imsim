import math
import numbers
from src import element


class Observatory(element.Element):
    """
        Observatory is an object that represent the condition of observation
    """
    SETTING_PATH_ROOT = "OBSERVATORY"
    SETTING_DEFAULT_NAME = "DEFAULT"

    def __init__(self, settings, name):
        """init for Observatory
            Args :
                setting (Settings) : setting for Observatory
                name (str) : name of the configuration in setting file
        """

        # Init
        self.str = "Observatory : "

        self.elevation = None  # elevation of source above horizon (deg)
        self.atmosphere_transmission = None  # transmission of the atmosphere in the photometric band
        self.seeing = None  # Fwhm of the seeing (arcsec)

        self.sky_brightness = None  # sky brightness in the photometric band (mag/arcsec2)
        self.sky_brightness_tab = { 'U':
                                    {0: 22.0,
                                     3: 21.5,
                                     7: 19.9,
                                     10: 18.5,
                                     14: 17.0},
                                'B':
                                    {0: 22.7,
                                     3: 22.4,
                                     7: 21.6,
                                     10: 20.7,
                                     14: 19.5},
                                'V':
                                    {0: 21.8,
                                     3: 21.7,
                                     7: 21.4,
                                     10: 20.7,
                                     14: 20.0},
                                'R':
                                    {0: 20.9,
                                     3: 20.8,
                                     7: 20.6,
                                     10: 20.3,
                                     14: 19.9},
                                'I':
                                    {0: 19.9,
                                     3: 19.9,
                                     7: 19.7,
                                     10: 19.5,
                                     14: 19.2}
                                }

        super().__init__(settings, name)
        if self.name is not None:
            self.load_settings()

    def __str__(self):
        return str(self.str)

    def load_settings(self):
        """load the settings value for class source
            Args :
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if not super()._check_settings():
            return False

        self.set_elevation(self._get_setting_val("elevation"))
        self.set_atmosphere_transmission(self._get_setting_val("atmosphere_transmission"))
        self.set_seeing(self._get_setting_val("seeing"))
        self.set_sky_brightness(self._get_setting_val("sky_brightness"))
        if self.get_sky_brightness() is None:
            lunar_age = self._get_setting_val("lunar_age")
            photometric_band = self._get_setting_val("photometric_band")
            if lunar_age is not None and photometric_band is not None:
                self.set_sky_brightness_with_lunar_ages(lunar_age, photometric_band)
        return True

    def set_elevation(self, elevation):
        """set_elevation set elevation value
            Args :
                elevation (numbers) : value for elevation
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.elevation = None
        if isinstance(elevation, numbers.Number):
            elevation = float(elevation)
            if 90 >= elevation > 0:
                self.elevation = elevation
                return True
        elif elevation is None:
            return True

        self.logger.warning("Invalid elevation {} must be a number between 90 and 0 ".format(elevation))
        return False

    def get_elevation(self):
        """get_elevation get elevation value
            Args :
            Returns :
                elevation (float) : return elevation value
        """
        return self.elevation

    def set_atmosphere_transmission(self, atmosphere_transmission):
        """set_central_wavelength set central_wavelength value
            Args :
                central_wavelength (numbers) : value for central_wavelength
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.atmosphere_transmission = None
        if isinstance(atmosphere_transmission, numbers.Number):
            atmosphere_transmission = float(atmosphere_transmission)
            if 1 >= atmosphere_transmission >= 0:
                self.atmosphere_transmission = atmosphere_transmission
                return True
        elif atmosphere_transmission is None:
            return True

        self.logger.warning("Invalid atmosphere_transmission {} "
                            "must be number between 1 and 0".format(atmosphere_transmission))
        return False

    def get_atmosphere_transmission(self):
        """get_atmosphere_transmission get atmosphere_transmission value
            Args :
            Returns :
                atmosphere_transmission (float) : return atmosphere_transmission value
        """
        return self.atmosphere_transmission

    def set_seeing(self, seeing):
        """set_seeing set seeing value
            Args :
                seeing (numbers) : value for seeing
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.seeing = None
        if isinstance(seeing, numbers.Number):
            seeing = float(seeing)
            if seeing >= 0:
                self.seeing = seeing
                return True
        elif seeing is None:
            return True

        self.logger.warning("Invalid seeing {} "
                            "must be number > 0".format(seeing))
        return False

    def get_seeing(self):
        """get_seeing get seeing value
            Args :
            Returns :
                seeing (float) : return seeing value
        """
        return self.seeing

    def set_sky_brightness(self, sky_brightness):
        """set_sky_brightness set sky_brightness value
            Args :
                sky_brightness (numbers) : value for sky_brightness
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.sky_brightness = None
        if isinstance(sky_brightness, numbers.Number):
            sky_brightness = float(sky_brightness)
            if sky_brightness >= 0:
                self.sky_brightness = sky_brightness
                return True
        elif sky_brightness is None:
            return True

        self.logger.warning("Invalid sky_brightness {} "
                            "must be number between > 0".format(sky_brightness))
        return False

    def set_sky_brightness_with_lunar_ages(self, lunar_age, photometric_band):
        """set_sky_brightness_with_lunar_ages set sky_brightness with photometric_band and lunar_age
            Args :
                lunar_age (numbers) : value for lunar_age
                photometric_band (numbers) : value for photometric_band
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.sky_brightness = None
        if photometric_band is None or lunar_age is None:
            return True
        if photometric_band in self.sky_brightness_tab.keys():
            if lunar_age in self.sky_brightness_tab[photometric_band].keys():
                self.sky_brightness = self.sky_brightness_tab[photometric_band][lunar_age]
            else:
                self.logger.warning("Invalid lunar_age {} "
                                    "must be in {}".format(lunar_age, self.sky_brightness_tab[photometric_band].keys()))
        else:
            self.logger.warning("Invalid photometric_band {} "
                                "must be in {}".format(photometric_band,self.sky_brightness_tab.keys()))
        return False

    def get_sky_brightness(self):
        """get_sky_brightness get sky_brightness value
            Args :
            Returns :
                sky_brightness (float) : return sky_brightness value
        """
        return self.sky_brightness

    def get_atmosphere_transmission_at_elevation(self):
        """get_atmosphere_transmission_at_elevation get atmosphere transmission at elevation
            Args :
            Returns :
                atmosphere_transmission_at_elevation (float) : return atmosphere_transmission_at_elevation
        """
        atmosphere_transmission = self.get_atmosphere_transmission()
        elevation = self.get_elevation()
        if atmosphere_transmission is None or elevation is None:
            return None
        return self.get_atmosphere_transmission()*math.sin(math.radians(self.get_elevation()))
