import numbers
from src import element


class Optic(element.Element):
    """
        Optic is an object that represent the optic tube
    """
    SETTING_PATH_ROOT = "OPTIC"
    SETTING_DEFAULT_NAME = "DEFAULT"

    def __init__(self, settings, name):
        """init for OPTIC
            Args :
                setting (Settings) : setting for Optic
                name (str) : name of the configuration in setting file
        """

        # Init
        self.str = "Optic : "

        self.diameter = None  # Optic diameter
        self.transmission = None  # Optic transmission
        self.fwhm_psf_opt = None  # fwhm of th point spread function in the image plane (m)
        self.focal_length = None  # focal length
        self.corrected_circle = None  # Corrected circle

        super().__init__(settings, name)
        if self.name is not None:
            self.setting_status = self.load_settings()

    def __str__(self):
        return str(self.str)

    def __update_focal_length(self, foc_diameter_ratio):
        """__update_focal_length
            Args :
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if self.diameter is None:
            return False
        if foc_diameter_ratio is None:
            return False

        self.focal_length = float(foc_diameter_ratio*self.diameter)
        return True

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
        if not self.set_diameter(self._get_setting_val("diameter")):
            return_val = False
        if not self.set_focal_length(self._get_setting_val("focal_length")):
            return_val = False
        if not self.set_foc_diameter_ratio(self._get_setting_val("foc_diameter_ratio")):
            return_val = False
        if not self.set_transmission(self._get_setting_val("transmission")):
            return_val = False
        if not self.set_fwhm_psf_opt(self._get_setting_val("fwhm_psf_opt")):
            return_val = False
        if not self.set_corrected_circle(self._get_setting_val("corrected_circle")):
            return_val = False
        self.setting_status = return_val
        return return_val

    def set_diameter(self, diameter):
        """set_diameter set diameter value
            Args :
                diameter (numbers) : value for diameter
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if isinstance(diameter, numbers.Number) and diameter > 0:
            self.diameter = float(diameter)
            return True
        elif diameter is None:
            self.diameter = None
            return True

        self.logger.warning("Invalid diameter {} must be a number > 0".format(diameter))
        return False

    def get_diameter(self):
        """set_diameter set set diameter set value
            Args :
            Returns :
                diameter (float) : return diameter value
        """
        return self.diameter

    def set_foc_diameter_ratio(self, foc_diameter_ratio):
        """set_foc_diameter_ratio set focal diameter ratio
            Args :
                foc_diameter_ratio (number) : value for foc_diameter_ratio
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if isinstance(foc_diameter_ratio, numbers.Number):
            self.__update_focal_length(float(foc_diameter_ratio))
            return True
        elif foc_diameter_ratio is None:
            return False
        self.logger.warning("Invalid focal diameter ratio {} must be e number".format(foc_diameter_ratio))
        return False

    def get_foc_diameter_ratio(self):
        """set_foc_diameter_ratio set foc_diameter_ratio set value
            Args :
            Returns :
                foc_diameter_ratio (float) : return diameter value
        """
        if self.diameter is None or self.diameter <= 0:
            self.logger.warning("get_foc_diameter_ratio : Invalid diameter {} . "
                                "Must be a positive not null number. ".format(self.diameter))
            return None
        if self.focal_length is None:
            self.logger.warning("get_foc_diameter_ratio : Invalid focal_length {} . "
                                "Must be a positive number. ".format(self.focal_length))
            return None

        return float(self.focal_length/self.diameter)

    def set_transmission(self, transmission):
        """set_transmission set the transmission
            Args :
                transmission (numbers) : value for transmission
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if isinstance(transmission, numbers.Number) and transmission > 0 and transmission < 1:
            self.transmission = float(transmission)
            return True
        elif transmission is not None:
            self.logger.warning("Invalid optic transmission {} must be e number".format(transmission))
        return False

    def get_transmission(self):
        """set_transmission set transmission set value
            Args :
            Returns :
                transmission (float) : return transmission value
        """
        return self.transmission

    def set_focal_length(self, focal_length):
        """set_focal_length set the focal_length
            Args :
                focal_length (numbers) : value for focal_length
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if isinstance(focal_length, numbers.Number):
            self.focal_length = float(focal_length)
            return True
        elif focal_length is not None:
            self.logger.warning("Invalid apparent stellar magnitude {} must be e number".format(focal_length))
        return False

    def get_focal_length(self):
        """set_focal_length set focal_length set value
            Args :
            Returns :
                focal_length (float) : return focal_length value
        """
        return self.focal_length

    def set_fwhm_psf_opt(self, fwhm_psf_opt):
        """set_fwhm_psf_opt set fwhm_psf_opt
            Args :
                fwhm_psf_opt (numbers) : value for fwhm_psf_opt
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if isinstance(float(fwhm_psf_opt), numbers.Number):
            self.fwhm_psf_opt = float(fwhm_psf_opt)
            return True
        elif fwhm_psf_opt is not None:
            self.logger.warning("Invalid fwhm_psf_opt {} must be a number".format(fwhm_psf_opt))
        return False

    def get_fwhm_psf_opt(self):
        """get_fwhm_psf_opt get the fwhm_psf_opt
            Args :
            Returns :
                fwhm_psf_opt (float) : return fwhm_psf_opt value
        """
        return self.fwhm_psf_opt

    def set_corrected_circle(self, corrected_circle):
        """set_corrected_circle set corrected_circle
            Args :
                corrected_circle (numbers) : value for corrected_circle in m
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if isinstance(corrected_circle, numbers.Number):
            self.corrected_circle = corrected_circle
            return True
        elif corrected_circle is not None:
            self.logger.warning("set_corrected_circle : Invalid corrected_circle {} "
                                "must be a number".format(corrected_circle))
        return False

    def get_corrected_circle(self):
        """get_corrected_circle get the corrected_circle
            Args :
            Returns :
                corrected_circle (float) : return corrected_circle value
        """
        return self.corrected_circle
