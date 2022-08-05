import numbers
from src import element


class Filter(element.Element):
    """
        Filter is an object that represent the filter
    """
    SETTING_PATH_ROOT = "FILTER"
    SETTING_DEFAULT_NAME = "DEFAULT"

    def __init__(self, settings, name):
        """init for Filter
            Args :
                setting (Settings) : setting for Filter
                name (str) : name of the configuration in setting file
        """

        # Init
        self.str = "Filter : "

        self.band = "C"  # Band name
        self.central_wavelength = 0.6  # Central wavelength of the photometric band (µm)
        self.bandpass_width = 0.3  # band width of the photometric (µm)
        self.flux_mag_zero = 3100  # Flux at magnitude zero of the photometric band (Jy)
        self.transmission = 1  # transmission (optional)

        super().__init__(settings, name)
        if self.name is not None:
            self.setting_status = self.load_settings()

    def __str__(self):
        return str(self.str)

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
        if not self.set_band(self._get_setting_val("band")):
            return_val = False
        if not self.set_central_wavelength(self._get_setting_val("central_wavelength")):
            return_val = False
        if not self.set_bandpass_width(self._get_setting_val("bandpass_width")):
            return_val = False
        if not self.set_flux_mag_zero(self._get_setting_val("flux_mag_zero")):
            return_val = False
        if not self.set_transmission(self._get_setting_val("transmission")):
            return_val = False
        self.setting_status = return_val
        return return_val

    def set_band(self, band):
        """set_band set band value
            Args :
                band (numbers) : value for band
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.band = None
        if isinstance(band, str) :
            self.band = band
            return True
        elif band is None:
            return True

        self.logger.warning("Invalid band {} must be a str".format(band))
        return False

    def get_band(self):
        """get_band get band value
            Args :
            Returns :
                band (float) : return band value
        """
        return self.band

    def set_central_wavelength(self, central_wavelength):
        """set_central_wavelength set central_wavelength value
            Args :
                central_wavelength (numbers) : value for central_wavelength
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        central_wavelength = float(central_wavelength)
        self.central_wavelength = None
        if isinstance(central_wavelength, numbers.Number) and central_wavelength > 0:
            self.central_wavelength = central_wavelength
            return True
        elif central_wavelength is None:
            return True

        self.logger.warning("Invalid central_wavelength {} must be number > 0".format(central_wavelength))
        return False

    def get_central_wavelength(self):
        """get_central_wavelength get central_wavelength value
            Args :
            Returns :
                central_wavelength (float) : return central_wavelength value
        """
        return self.central_wavelength

    def set_bandpass_width(self, bandpass_width):
        """set_bandpass_width set bandpass_width value
            Args :
                bandpass_width (numbers) : value for bandpass_width
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        bandpass_width = float(bandpass_width)
        self.bandpass_width = None
        if isinstance(bandpass_width, numbers.Number) and bandpass_width > 0 :
            self.bandpass_width = bandpass_width
            return True
        elif bandpass_width is None:
            return True

        self.logger.warning("Invalid bandpass_width {} must be a number > 0".format(bandpass_width))
        return False

    def get_bandpass_width(self):
        """get_bandpass_width get bandpass_width value
            Args :
            Returns :
                bandpass_width (float) : return bandpass_width value
        """
        return self.bandpass_width

    def set_flux_mag_zero(self, flux_mag_zero):
        """set_flux_mag_zero set flux_mag_zero value
            Args :
                flux_mag_zero (numbers) : value for flux_mag_zero
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        flux_mag_zero = float(flux_mag_zero)
        self.flux_mag_zero = None
        if isinstance(flux_mag_zero, numbers.Number) and flux_mag_zero > 0 :
            self.flux_mag_zero = flux_mag_zero
            return True
        elif flux_mag_zero is None:
            return True

        self.logger.warning("Invalid flux_mag_zero {} must be a number > 0".format(flux_mag_zero))
        return False

    def get_flux_mag_zero(self):
        """get_flux_mag_zero get flux_mag_zero value
            Args :
            Returns :
                flux_mag_zero (float) : return flux_mag_zero value
        """
        return self.flux_mag_zero

    def set_transmission(self, transmission):
        """set_transmission set transmission value
            Args :
                transmission (numbers) : value for transmission
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        transmission = float(transmission)
        self.transmission = None
        if isinstance(transmission, numbers.Number) and 1 >= transmission >= 0:
            self.transmission = transmission
            return True
        elif transmission is None:
            return True

        self.logger.warning("Invalid transmission {} must be a number between 0 and 1".format(transmission))
        return False

    def get_transmission(self):
        """get_transmission get transmission value
            Args :
            Returns :
                transmission (float) : return transmission value
        """
        return self.transmission
