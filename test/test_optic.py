import unittest
from src.optic import Optic
from src.settings import Settings
import os.path


class OpticTest(unittest.TestCase):
    # Test init
    def test_init_name(self):
        optic = self.__setOptic("myoptic")
        self.assertEqual(optic.name, "myoptic")

    def test_init_bad_name(self):
        optic = self.__setOptic("aoptic")
        self.assertEqual(optic.name, None)

    # Test deffault value
    def test_init_default_diameter(self):
        optic = self.__setOptic("aoptic")
        self.assertEqual(optic.diameter, None)

    def test_init_default_focal_length(self):
        optic = self.__setOptic("aoptic")
        self.assertEqual(optic.focal_length, None)

    def test_init_default_transmission(self):
        optic = self.__setOptic("aoptic")
        self.assertEqual(optic.transmission, None)

    def test_init_default_fwhm_psf_opt(self):
        optic = self.__setOptic("aoptic")
        self.assertEqual(optic.fwhm_psf_opt, None)

    def test_init_default_corrected_circle(self):
        optic = self.__setOptic("aoptic")
        self.assertEqual(optic.corrected_circle, None)

    # Test rifast800 value
    def test_init_rifast800_diameter(self):
        optic = self.__setOptic("rifast800")
        self.assertEqual(optic.diameter, 0.8)

    def test_init_rifast800_focal_length(self):
        optic = self.__setOptic("rifast800")
        self.assertEqual(optic.focal_length, 3.04)

    def test_init_rifast800_transmission(self):
        optic = self.__setOptic("rifast800")
        self.assertEqual(optic.transmission, 0.4)

    def test_init_rifast800_corrected_circle(self):
        optic = self.__setOptic("rifast800")
        self.assertEqual(optic.corrected_circle, 0.08)

    def test_init_rifast800_fwhm_psf_opt(self):
        optic = self.__setOptic("rifast800")
        self.assertEqual(optic.fwhm_psf_opt, float(8e-6))

    # Test Get
    def test_get_rifast800_diameter(self):
        optic = self.__setOptic("rifast800")
        self.assertEqual(optic.get_diameter(), 0.8)

    def test_get_rifast800_focal_length(self):
        optic = self.__setOptic("rifast800")
        self.assertEqual(optic.get_focal_length(), 3.04)

    def test_get_rifast800_transmission(self):
        optic = self.__setOptic("rifast800")
        self.assertEqual(optic.get_transmission(), 0.4)

    def test_get_rifast800_corrected_circle(self):
        optic = self.__setOptic("rifast800")
        self.assertEqual(optic.get_corrected_circle(), 0.08)

    def test_get_rifast800_fwhm_psf_opt(self):
        optic = self.__setOptic("rifast800")
        self.assertEqual(optic.get_fwhm_psf_opt(), 8e-6)

    # Test rifast400 (test set F/D)
    def test_get_rifast400_get_app_stellar_mag(self):
        optic = self.__setOptic("rifast400")
        self.assertAlmostEqual(optic.get_focal_length(), 1.5, 1)

    def test_get_rifast400_get_abs_stellar_mag(self):
        optic = self.__setOptic("rifast400")
        self.assertAlmostEqual(optic.get_foc_diameter_ratio(), 3.8, 1)

    def test_get_rifast400_get_dl_mpc(self):
        optic = self.__setOptic("rifast400")
        self.assertEqual(optic.get_diameter(), 0.4)

    # Test set
    def test_rifast800_set_focal_length(self):
        optic = self.__setOptic("rifast800")
        optic.set_focal_length(5)
        self.assertEqual(optic.get_focal_length(), 5)

    def test_rifast800_set_diameter(self):
        optic = self.__setOptic("rifast800")
        optic.set_diameter(2)
        self.assertEqual(optic.get_diameter(), 2)

    def test_rifast800_set_transmission(self):
        optic = self.__setOptic("rifast800")
        optic.set_transmission(0.3)
        self.assertEqual(optic.get_transmission(), 0.3)

    def test_rifast800_set_fwhm_psf_opt(self):
        optic = self.__setOptic("rifast800")
        optic.set_fwhm_psf_opt(4)
        self.assertEqual(optic.get_fwhm_psf_opt(), 4)

    def test_rifast800_set_corrected_circle(self):
        optic = self.__setOptic("rifast800")
        optic.set_corrected_circle(0.04)
        self.assertEqual(optic.get_corrected_circle(), 0.04)

    def test_rifast800_set_foc_diameter_ratio(self):
        optic = self.__setOptic("rifast800")
        optic.set_foc_diameter_ratio(4)
        self.assertEqual(optic.get_foc_diameter_ratio(), 4)

    @staticmethod
    def __setOptic(name):
        conf_file = "imsim_conf_unitest.yml"
        conf_file = os.path.abspath(conf_file)
        setting = Settings(conf_file)
        return Optic(setting, name)


if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig('./conf/logging.conf')
    unittest.main()
