import math
import numbers
from src import element


class Camera(element.Element):
    """
        Camera is an object that represent the camera
    """
    SETTING_PATH_ROOT = "CAMERA"
    SETTING_DEFAULT_NAME = "DEFAULT"

    def __init__(self, settings, name):
        """init for Camera
            Args :
                setting (Settings) : setting for Camera
                name (str) : name of the configuration in setting file
        """

        # Init
        self.str = "Camera : "
        self.sensor_type = "CCD"  # CCD or CMOS
        self.sensor_type_list = ["CCD", "CMOS"]  # Available sensor_type value

        self.nb_photocell_axis1 = None  # Number of photocell on axis1
        self.photocell_size_axis1 = None  # Photocell size on axis1 (m)
        self.bin_axis1 = None  # binning on axis1 (photocells/pixel)
        self.nb_photocell_axis2 = None  # Number of photocell on axis2
        self.photocell_size_axis2 = None  # Photocell size on axis2 (m)
        self.bin_axis2 = None  # binning on axis2 (photocells/pixel)
        self.quantum_efficiency = None  # quantum efficiency at I (electron/photon)
        self.readout_noise = None  # readout noise (electron)
        self.dark_currant = None  # dark currant (electron/sec/photocell)
        self.gain = None  # sensor Gain (electron/ADU)
        self.electron_multiplier = 1 # electron multiplier (>1 if EMCCD else = 1)

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
        self.setting_status = False
        if not super()._check_settings():
            return False
        return_val = True
        if not self.set_sensor_type(self._get_setting_val("sensor_type")):
            return_val = False
        if not self.set_nb_photocell_axis1(self._get_setting_val("nb_photocell_axis1")):
            return_val = False
        if not self.set_photocell_size_axis1(self._get_setting_val("photocell_size_axis1")):
            return_val = False
        if not self.set_bin_axis1(self._get_setting_val("bin_axis1")):
            return_val = False
        if not self.set_nb_photocell_axis2(self._get_setting_val("nb_photocell_axis2")):
            return_val = False
        if not self.set_photocell_size_axis2(self._get_setting_val("photocell_size_axis2")):
            return_val = False
        if not self.set_bin_axis2(self._get_setting_val("bin_axis2")):
            return_val = False
        if not self.set_quantum_efficiency(self._get_setting_val("quantum_efficiency")):
            return_val = False
        if not self.set_readout_noise(self._get_setting_val("readout_noise")):
            return_val = False
        if not self.set_dark_currant(self._get_setting_val("dark_currant")):
            return_val = False
        if not self.set_gain(self._get_setting_val("gain")):
            return_val = False
        if not self.set_electron_multiplier(self._get_setting_val("electron_multiplier")):
            return_val = False
        self.setting_status = return_val
        return return_val

    def set_sensor_type(self, sensor_type):
        """get_sensor_type set sensor_type value
            Args :
                sensor_type (numbers) : value for sensor_type
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.sensor_type = "CCD"
        if sensor_type in self.sensor_type_list:
            self.sensor_type = sensor_type
            return True

        self.logger.warning("Invalid sensor_type {} must be in {}".format(sensor_type, self.sensor_type_list))
        return False

    def get_sensor_type(self):
        """get_sensor_type get sensor_type value
            Args :
            Returns :
                sensor_type (float) : return sensor_type value
        """
        return self.sensor_type

    def set_nb_photocell_axis1(self, nb_photocell_axis1):
        """set_nb_photocell_axis1 set nb_photocell_axis1 value
            Args :
                nb_photocell_axis1 (numbers) : value for nb_photocell_axis1
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.nb_photocell_axis1 = None
        if isinstance(nb_photocell_axis1, numbers.Number) and nb_photocell_axis1 > 0:
            self.nb_photocell_axis1 = int(nb_photocell_axis1)
            return True
        elif nb_photocell_axis1 is None:
            return True

        self.logger.warning("Invalid nb_photocell_axis1 {} must be a number > 0".format(nb_photocell_axis1))
        return False

    def get_nb_photocell_axis1(self):
        """get_nb_photocell_axis1 get nb_photocell_axis1 value
            Args :
            Returns :
                nb_photocell_axis1 (float) : return nb_photocell_axis1 value
        """
        return self.nb_photocell_axis1

    def set_photocell_size_axis1(self, photocell_size_axis1):
        """set_photocell_size_axis1 set photocell_size_axis1 value
            Args :
                photocell_size_axis1 (numbers) : value for photocell_size_axis1
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.photocell_size_axis1 = None
        photocell_size_axis1 = float(photocell_size_axis1)
        if isinstance(photocell_size_axis1, numbers.Number) and photocell_size_axis1 > 0:
            self.photocell_size_axis1 = float(photocell_size_axis1)
            return True
        elif photocell_size_axis1 is None:
            return True

        self.logger.warning("Invalid photocell_size_axis1 {} must be a number > 0".format(photocell_size_axis1))
        return False

    def get_photocell_size_axis1(self):
        """get_photocell_size_axis1 get photocell_size_axis1
            Args :
            Returns :
                photocell_size_axis1 (float) : return photocell_size_axis1 value
        """
        return self.photocell_size_axis1

    def set_bin_axis1(self, bin_axis1):
        """set_bin_axis1 set bin_axis1 value
            Args :
                bin_axis1 (numbers) : value for bin_axis1
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.bin_axis1 = None
        if isinstance(bin_axis1, numbers.Number) and bin_axis1 > 0:
            self.bin_axis1 = int(bin_axis1)
            return True
        elif bin_axis1 is None:
            return True

        self.logger.warning("Invalid bin_axis1 {} must be a number > 0".format(bin_axis1))
        return False

    def get_bin_axis1(self):
        """set_bin_axis1 get bin_axis1 value
            Args :
            Returns :
                bin_axis1 (float) : return bin_axis1 value
        """
        return self.bin_axis1

    def set_nb_photocell_axis2(self, nb_photocell_axis2):
        """set_nb_photocell_axis2 set nb_photocell_axis2 value
            Args :
                nb_photocell_axis2 (numbers) : value for nb_photocell_axis2
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.nb_photocell_axis2 = None
        if isinstance(nb_photocell_axis2, numbers.Number) and nb_photocell_axis2 > 0:
            self.nb_photocell_axis2 = int(nb_photocell_axis2)
            return True
        elif nb_photocell_axis2 is None:
            return True

        self.logger.warning("Invalid nb_photocell_axis2 {} must be a number > 0".format(nb_photocell_axis2))
        return False

    def get_nb_photocell_axis2(self):
        """set_nb_photocell_axis2 set set nb_photocell_axis2 set value
            Args :
            Returns :
                nb_photocell_axis2 (float) : return nb_photocell_axis2 value
        """
        return self.nb_photocell_axis2

    def set_photocell_size_axis2(self, photocell_size_axis2):
        """set_photocell_size_axis2 set photocell_size_axis2 value
            Args :
                photocell_size_axis2 (numbers) : value for photocell_size_axis2
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.photocell_size_axis2 = None
        photocell_size_axis2 = float(photocell_size_axis2)
        if isinstance(photocell_size_axis2, numbers.Number) and photocell_size_axis2 > 0:
            self.photocell_size_axis2 = float(photocell_size_axis2)
            return True
        elif photocell_size_axis2 is None:
            return True

        self.logger.warning("Invalid photocell_size_axis2 {} must be a number > 0".format(photocell_size_axis2))
        return False

    def get_photocell_size_axis2(self):
        """set_photocell_size_axis2 get photocell_size_axis2
            Args :
            Returns :
                photocell_size_axis2 (float) : return photocell_size_axis2value
        """
        return self.photocell_size_axis2

    def set_bin_axis2(self, bin_axis2):
        """set_bin_axis2 set bin_axis2 value
            Args :
                bin_axis2 (numbers) : value for bin_axis2
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.bin_axis2 = None
        if isinstance(bin_axis2, numbers.Number) and bin_axis2 > 0:
            self.bin_axis2 = int(bin_axis2)
            return True
        elif bin_axis2 is None:
            return True

        self.logger.warning("Invalid bin_axis2 {} must be a number > 0".format(bin_axis2))
        return False

    def get_bin_axis2(self):
        """set_bin_axis2 get bin_axis2 value
            Args :
            Returns :
                bin_axis2 (float) : return bin_axis2 value
        """
        return self.bin_axis2

    def set_quantum_efficiency(self, quantum_efficiency):
        """set_quantum_efficiency set quantum_efficiency value
            Args :
                quantum_efficiency (numbers) : value for quantum_efficiency
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.quantum_efficiency = None
        if isinstance(quantum_efficiency, numbers.Number) and 0 < quantum_efficiency <= 1:
            self.quantum_efficiency = float(quantum_efficiency)
            return True
        elif quantum_efficiency is None:
            return True

        self.logger.warning("Invalid quantum_efficiency {} must be a number between 0 and 1".format(quantum_efficiency))
        return False

    def get_quantum_efficiency(self):
        """set_quantum_efficiency get quantum_efficiency value
            Args :
            Returns :
                quantum_efficiency (float) : return quantum_efficiency value
        """
        return self.quantum_efficiency

    def set_readout_noise(self, readout_noise):
        """set_readout_noise set readout_noise value
            Args :
                readout_noise (numbers) : value for readout_noise
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.readout_noise = None
        if isinstance(readout_noise, numbers.Number) and readout_noise > 0:
            self.readout_noise = float(readout_noise)
            return True
        elif readout_noise is None:
            return True

        self.logger.warning("Invalid readout_noise {} must be a number > 0".format(readout_noise))
        return False

    def get_readout_noise(self):
        """set_readout_noise get readout_noise value
            Args :
            Returns :
                readout_noise (float) : return readout_noise value
        """
        return self.readout_noise

    def get_pixel_readout_noise(self):
        """set_readout_noise get readout_noise value
            Args :
            Returns :
                readout_noise (float) : return readout_noise value
        """
        bin_factor = 1
        if self.sensor_type == "CMOS":
            bin_factor = self.bin_axis1 * self.bin_axis2

        return self.readout_noise * bin_factor

    def set_dark_currant(self, dark_currant):
        """set_dark_currant set dark_currant value
            Args :
                dark_currant (numbers) : value for dark_currant
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.dark_currant = None
        if isinstance(dark_currant, numbers.Number) and dark_currant > 0:
            self.dark_currant = float(dark_currant)
            return True
        elif dark_currant is None:
            return True

        self.logger.warning("Invalid dark_currant {} must be a number > 0".format(dark_currant))
        return False

    def get_dark_currant(self):
        """set_dark_currant get dark_currant value
            Args :
            Returns :
                dark_currant (float) : return dark_currant value
        """
        return self.dark_currant

    def get_pixel_dark_currant(self):
        """set_dark_currant get dark_currant value
            Args :
            Returns :
                dark_currant (float) : return dark_currant value
        """
        bin1 = self.get_bin_axis1()
        bin2 = self.get_bin_axis2()
        return self.dark_currant * bin1 * bin2

    def set_gain(self, gain):
        """set_gain set gain value
            Args :
                gain (numbers) : value for gain
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.gain = None
        if isinstance(gain, numbers.Number) and gain > 0:
            self.gain = float(gain)
            return True
        elif gain is None:
            return True

        self.logger.warning("Invalid gain {} must be a number > 0".format(gain))
        return False

    def get_gain(self):
        """set_gain get gain value
            Args :
            Returns :
                gain (float) : return gain value
        """
        return self.gain

    def set_electron_multiplier(self, electron_multiplier):
        """set_electron_multiplier set electron_multiplier value
            Args :
                electron_multiplier (numbers) : value for electron_multiplier
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.electron_multiplier = 1
        if isinstance(electron_multiplier, numbers.Number) and electron_multiplier >= 1:
            self.electron_multiplier = float(electron_multiplier)
            return True
        elif electron_multiplier is None:
            return True

        self.logger.warning("Invalid electron_multiplier {} must be a number >= 1".format(electron_multiplier))
        return False

    def get_electron_multiplier(self):
        """set_electron_multiplier get electron_multiplier value
            Args :
            Returns :
                electron_multiplier (float) : return electron_multiplier value
        """
        return self.electron_multiplier

    def set_pixel_size_axis1(self, pixel_size_axis1):
        """set_pixel_size_axis1 set focal pixel_size_axis1
            Args :
                pixel_size_axis1 (number) : value for pixel_size_axis1
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if isinstance(pixel_size_axis1, numbers.Number) and pixel_size_axis1 > 0 :
            if self.bin_axis1 is None or self.bin_axis1 <= 0:
                return False
            self.photocell_size_axis1 = float(pixel_size_axis1/self.bin_axis1)
            return True
        elif pixel_size_axis1 is None:
            return False
        self.logger.warning("Invalid pixel_size_axis1 {} must be e number".format(pixel_size_axis1))
        return False

    def get_pixel_size_axis1(self):
        """set_pixel_size_axis1 set pixel_size_axis1 set value
            Args :
            Returns :
                pixel_size_axis1 (float) : return diameter value
        """
        if self.bin_axis1 is None or self.bin_axis1 <= 0:
            self.logger.warning("get_pixel_size_axis1 : Invalid bin_axis1 {} . "
                                "Must be a positive not null number. ".format(self.bin_axis1))
            return None
        if self.photocell_size_axis1 is None or self.bin_axis1 <= 0:
            self.logger.warning("get_pixel_size_axis1 : Invalid photocell_size_axis1 {} . "
                                "Must be a positive number. ".format(self.photocell_size_axis1))
            return None

        return float(self.photocell_size_axis1*self.bin_axis1)

    def set_pixel_size_axis2(self, pixel_size_axis2):
        """set_pixel_size_axis2 set focal pixel_size_axis2
            Args :
                pixel_size_axis2 (number) : value for pixel_size_axis2
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if isinstance(pixel_size_axis2, numbers.Number) and pixel_size_axis2 > 0:
            if self.bin_axis2 is None or self.bin_axis2 <= 0:
                return False
            self.photocell_size_axis2 = float(pixel_size_axis2/self.bin_axis2)
            return True
        elif pixel_size_axis2 is None:
            return False
        self.logger.warning("Invalid pixel_size_axis2 {} must be e number".format(pixel_size_axis2))
        return False

    def get_pixel_size_axis2(self):
        """set_pixel_size_axis2 set pixel_size_axis2 set value
            Args :
            Returns :
                pixel_size_axis2 (float) : return pixel_size_axis2 value
        """
        if self.bin_axis2 is None or self.bin_axis2 <= 0:
            self.logger.warning("get_pixel_size_axis2 : Invalid bin_axis2 {} . "
                                "Must be a positive not null number. ".format(self.bin_axis2))
            return None
        if self.photocell_size_axis2 is None or self.bin_axis2 <= 0:
            self.logger.warning("get_pixel_size_axis2 : Invalid photocell_size_axis2 {} . "
                                "Must be a positive number. ".format(self.photocell_size_axis2))
            return None

        return float(self.photocell_size_axis2 * self.bin_axis2)

    def get_emccd_express_noise_factor(self):
        """set_pixel_size_axis2 set pixel_size_axis2 set value
            Args :
            Returns :
                pixel_size_axis2 (float) : return pixel_size_axis2 value
        """
        if self.electron_multiplier is None or self.electron_multiplier < 1:
            self.logger.warning("get_emccd_express_noise_factor : Invalid electron_multiplier {} . "
                                "Must be a positive not null number. ".format(self.electron_multiplier))
            return None

        return float(1+math.pow(2/math.pi*math.atan((self.electron_multiplier-1)*3), 3))

