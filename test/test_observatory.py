import unittest
from observatory import Observatory
from settings import Settings
import os.path


class ObservatoryTest(unittest.TestCase):
    # Test init
    def test_init_name(self):
        observatory = self.__setObservatory("myobservatory")
        self.assertEqual(observatory.name, "myobservatory")

    def test_init_bad_name(self):
        observatory = self.__setObservatory("anobservatory")
        self.assertEqual(observatory.name, None)

    # Test deffault value
    def test_init_default_elevation(self):
        observatory = self.__setObservatory("anobservatory")
        self.assertEqual(observatory.elevation, None)

    def test_init_default_atmosphere_transmission(self):
        observatory = self.__setObservatory("anobservatory")
        self.assertEqual(observatory.atmosphere_transmission, None)

    def test_init_default_seeing(self):
        observatory = self.__setObservatory("anobservatory")
        self.assertEqual(observatory.seeing, None)

    def test_init_default_sky_brightness(self):
        observatory = self.__setObservatory("anobservatory")
        self.assertEqual(observatory.sky_brightness, None)

    # Test myobservatory value
    def test_init_myobservatory_elevation(self):
        observatory = self.__setObservatory("myobservatory")
        self.assertEqual(observatory.elevation, 65.0)

    def test_init_myobservatory_atmosphere_transmission(self):
        observatory = self.__setObservatory("myobservatory")
        self.assertEqual(observatory.atmosphere_transmission, 0.5)

    def test_init_myobservatory_seeing(self):
        observatory = self.__setObservatory("myobservatory")
        self.assertEqual(observatory.seeing, 3)

    def test_init_myobservatory_sky_brightness(self):
        observatory = self.__setObservatory("myobservatory")
        self.assertEqual(observatory.sky_brightness, 21.8)

    # Test Get
    def test_get_myobservatory_elevation(self):
        observatory = self.__setObservatory("myobservatory")
        self.assertEqual(observatory.get_elevation(), 65)

    def test_get_myobservatory_atmosphere_transmission(self):
        observatory = self.__setObservatory("myobservatory")
        self.assertEqual(observatory.get_atmosphere_transmission(), 0.5)

    def test_get_myobservatory_seeing(self):
        observatory = self.__setObservatory("myobservatory")
        self.assertEqual(observatory.get_seeing(), 3)

    def test_get_myobservatory_sky_brightness(self):
        observatory = self.__setObservatory("myobservatory")
        self.assertEqual(observatory.get_sky_brightness(), 21.8)

    # Test set
    def test_set_myobservatory_elevation(self):
        observatory = self.__setObservatory("myobservatory")
        observatory.set_elevation(55)
        self.assertEqual(observatory.get_elevation(), 55)

    def test_set_myobservatory_atmosphere_transmission(self):
        observatory = self.__setObservatory("myobservatory")
        observatory.set_atmosphere_transmission(0.7)
        self.assertEqual(observatory.get_atmosphere_transmission(), 0.7)

    def test_set_myobservatory_atmosphere_transmission_bad(self):
        observatory = self.__setObservatory("myobservatory")
        observatory.set_atmosphere_transmission(1.7)
        self.assertEqual(observatory.get_atmosphere_transmission(), None)

    def test_set_myobservatory_seeing(self):
        observatory = self.__setObservatory("myobservatory")
        observatory.set_seeing(5)
        self.assertEqual(observatory.get_seeing(), 5)

    def test_set_myobservatory_sky_brightness(self):
        observatory = self.__setObservatory("myobservatory")
        observatory.set_sky_brightness(19.5)
        self.assertEqual(observatory.get_sky_brightness(), 19.5)

    def test_get_myobservatory_sky_brightness_with_lunar_ages(self):
        observatory = self.__setObservatory("myobservatory")
        observatory.set_sky_brightness_with_lunar_ages(7, 'R')
        self.assertEqual(observatory.get_sky_brightness(), 20.6)

    def test_get_myobservatory_sky_brightness_with_lunar_ages_bad(self):
        observatory = self.__setObservatory("myobservatory")
        observatory.set_sky_brightness_with_lunar_ages(4, 'R')
        self.assertEqual(observatory.get_sky_brightness(), None)

    @staticmethod
    def __setObservatory(name):
        conf_file = "imsim_conf_unitest.yml"
        conf_file = os.path.abspath(conf_file)
        setting = Settings(conf_file)
        return Observatory(setting, name)


if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig('./conf/logging.conf')
    unittest.main()
