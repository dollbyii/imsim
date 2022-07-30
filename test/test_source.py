import unittest
from src.source import Source
from src.settings import Settings
import os.path


class SourceTest(unittest.TestCase):
    # Test init
    def test_init_name(self):
        source = self.__setSource("mysource")
        self.assertEqual(source.name, "mysource")

    def test_init_bad_name(self):
        source = self.__setSource("asource")
        self.assertEqual(source.name, None)

    # Test deffault value
    def test_init_default_app_stellar_mag(self):
        source = self.__setSource("asource")
        self.assertEqual(source.app_stellar_mag, None)

    def test_init_default_abs_stellar_mag(self):
        source = self.__setSource("asource")
        self.assertEqual(source.abs_stellar_mag, None)

    def test_init_default_dl_mpc(self):
        source = self.__setSource("asource")
        self.assertEqual(source.dl_mpc, None)

    def test_init_default_ph_band(self):
        source = self.__setSource("asource")
        self.assertEqual(source.ph_band, None)

    # Test vega value
    def test_init_vega_abs_stellar_mag(self):
        source = self.__setSource("vega")
        self.assertEqual(source.abs_stellar_mag, 0.582)

    def test_init_vega_dl_mpc(self):
        source = self.__setSource("vega")
        self.assertEqual(source.dl_mpc, 7.67e-06)

    def test_init_vega_ph_band(self):
        source = self.__setSource("vega")
        self.assertEqual(source.ph_band, "C")

    def test_init_vega_app_stellar_mag(self):
        source = self.__setSource("vega")
        self.assertEqual(source.app_stellar_mag, None)

    def test_init_vega_get_abs_stellar_mag(self):
        source = self.__setSource("vega")
        self.assertEqual(source.get_abs_stellar_mag(), 0.582)

    def test_init_vega_get_dl_mpc(self):
        source = self.__setSource("vega")
        self.assertEqual(source.get_dl_mpc(), 7.67e-06)

    def test_init_vega_get_ph_band(self):
        source = self.__setSource("vega")
        self.assertEqual(source.get_ph_band(), "C")

    def test_init_vega_get_app_stellar_mag(self):
        source = self.__setSource("vega")
        self.assertLess(abs(source.get_app_stellar_mag()), 0.01)

    # Test aldebaran (set app_stellar_mag)
    def test_init_aldebaran_get_app_stellar_mag(self):
        source = self.__setSource("aldebaran")
        self.assertAlmostEqual(source.get_app_stellar_mag(), 0.85, 2)

    def test_init_aldebaran_get_abs_stellar_mag(self):
        source = self.__setSource("aldebaran")
        self.assertEqual(source.get_abs_stellar_mag(), None)

    def test_init_aldebaran_get_dl_mpc(self):
        source = self.__setSource("aldebaran")
        self.assertEqual(source.get_dl_mpc(), None)

    # Test set
    def test_vega_set_abs_stellar_mag(self):
        source = self.__setSource("vega")
        source.set_abs_stellar_mag(5)
        self.assertEqual(source.get_abs_stellar_mag(), 5)

    def test_vega_set_dl_mpc(self):
        source = self.__setSource("vega")
        source.set_dl_mpc(2)
        self.assertEqual(source.get_dl_mpc(), 2)

    def test_vega_set_app_stellar_mag0(self):
        source = self.__setSource("vega")
        source.set_app_stellar_mag(4)
        self.assertEqual(source.get_app_stellar_mag(), 4)

    def test_vega_set_app_stellar_mag1(self):
        source = self.__setSource("vega")
        source.update()
        source.set_app_stellar_mag(4)
        source.update()
        self.assertEqual(source.get_app_stellar_mag(), 4)

    def test_vega_set_app_stellar_mag2(self):
        source = self.__setSource("vega")
        source.set_app_stellar_mag(4)
        self.assertEqual(source.get_abs_stellar_mag(), None)

    def test_vega_set_app_stellar_mag3(self):
        source = self.__setSource("vega")
        source.set_app_stellar_mag(4)
        self.assertEqual(source.get_dl_mpc(), None)

    @staticmethod
    def __setSource(name):
        conf_file = "imsim_conf_unitest.yml"
        conf_file = os.path.abspath(conf_file)
        setting = Settings(conf_file)
        return Source(setting, name)


if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig('./conf/logging.conf')
    unittest.main()
