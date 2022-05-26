import unittest
from filter import Filter
from settings import Settings
import os.path


class FilterTest(unittest.TestCase):
    # Test init
    def test_init_name(self):
        filter = self.__setFilter("V")
        self.assertEqual(filter.name, "V")

    def test_init_bad_name(self):
        filter = self.__setFilter("afilter")
        self.assertEqual(filter.name, None)

    # Test deffault value
    def test_init_default_band(self):
        filter = self.__setFilter("afilter")
        self.assertEqual(filter.band, "C")

    def test_init_default_central_wavelength(self):
        filter = self.__setFilter("afilter")
        self.assertEqual(filter.central_wavelength, 0.6)

    def test_init_default_bandpass_width(self):
        filter = self.__setFilter("afilter")
        self.assertEqual(filter.bandpass_width, 0.3)

    def test_init_default_flux_mag_zero(self):
        filter = self.__setFilter("afilter")
        self.assertEqual(filter.flux_mag_zero, 3100)

    def test_init_default_transmission(self):
        filter = self.__setFilter("afilter")
        self.assertEqual(filter.transmission, 1)

    # Test U value
    def test_init_U_band(self):
        filter = self.__setFilter("U")
        self.assertEqual(filter.band, "U")

    def test_init_U_central_wavelength(self):
        filter = self.__setFilter("U")
        self.assertEqual(filter.central_wavelength, 0.36)

    def test_init_U_bandpass_width(self):
        filter = self.__setFilter("U")
        self.assertEqual(filter.bandpass_width, 0.15)

    def test_init_U_flux_mag_zero(self):
        filter = self.__setFilter("U")
        self.assertEqual(filter.flux_mag_zero, 1810)

    def test_init_U_transmission(self):
        filter = self.__setFilter("U")
        self.assertEqual(filter.transmission, 1)

    # Test Get
    def test_get_U_band(self):
        filter = self.__setFilter("U")
        self.assertEqual(filter.get_band(), "U")

    def test_get_U_central_wavelength(self):
        filter = self.__setFilter("U")
        self.assertEqual(filter.get_central_wavelength(), 0.36)

    def test_get_U_bandpass_width(self):
        filter = self.__setFilter("U")
        self.assertEqual(filter.get_bandpass_width(), 0.15)

    def test_get_U_flux_mag_zero(self):
        filter = self.__setFilter("U")
        self.assertEqual(filter.get_flux_mag_zero(), 1810)

    def test_get_U_transmission(self):
        filter = self.__setFilter("U")
        self.assertEqual(filter.get_transmission(), 1)

    # Test set
    def test_set_U_band(self):
        filter = self.__setFilter("U")
        filter.set_band("z")
        self.assertEqual(filter.get_band(), "z")

    def test_set_U_central_wavelength(self):
        filter = self.__setFilter("U")
        filter.set_central_wavelength(0.47)
        self.assertEqual(filter.get_central_wavelength(), 0.47)

    def test_set_U_bandpass_width(self):
        filter = self.__setFilter("U")
        filter.set_bandpass_width(1.2)
        self.assertEqual(filter.get_bandpass_width(), 1.2)

    def test_set_U_flux_mag_zero(self):
        filter = self.__setFilter("U")
        filter.set_flux_mag_zero(3054)
        self.assertEqual(filter.get_flux_mag_zero(), 3054)

    def test_set_U_transmission(self):
        filter = self.__setFilter("U")
        filter.set_transmission(0.2)
        self.assertEqual(filter.get_transmission(), 0.2)

    def test_set_U_transmission_bad(self):
        filter = self.__setFilter("U")
        filter.set_transmission(5)
        self.assertEqual(filter.get_transmission(), None)

    @staticmethod
    def __setFilter(name):
        conf_file = "imsim_conf_unitest.yml"
        conf_file = os.path.abspath(conf_file)
        setting = Settings(conf_file)
        return Filter(setting, name)


if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig('./conf/logging.conf')
    unittest.main()
