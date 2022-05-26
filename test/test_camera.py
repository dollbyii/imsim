import unittest
from camera import Camera
from settings import Settings
import os.path


class CameraTest(unittest.TestCase):
    # Test init
    def test_init_name(self):
        camera = self.__setCamera("mycamera")
        self.assertEqual(camera.name, "mycamera")

    def test_init_bad_name(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.name, None)

    # Test deffault value
    def test_init_default_sensor_type(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.sensor_type, "CCD")

    def test_init_default_nb_photocell_axis1(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.nb_photocell_axis1, None)

    def test_init_default_photocell_size_axis1(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.photocell_size_axis1, None)

    def test_init_default_bin_axis1(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.bin_axis1, None)

    def test_init_default_nb_photocell_axis2(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.nb_photocell_axis2, None)

    def test_init_default_photocell_size_axis2(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.photocell_size_axis2, None)

    def test_init_default_bin_axis2(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.bin_axis2, None)

    def test_init_default_quantum_efficiency(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.quantum_efficiency, None)

    def test_init_default_readout_noise(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.readout_noise, None)

    def test_init_default_dark_currant(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.dark_currant, None)

    def test_init_default_gain(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.gain, None)

    def test_init_default_electron_multiplier(self):
        camera = self.__setCamera("acamera")
        self.assertEqual(camera.electron_multiplier, 1)

    # Test KL6060bsi value
    def test_init_kl6060_sensor_type(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.sensor_type, "CMOS")

    def test_init_kl6060_nb_photocell_axis1(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.nb_photocell_axis1, 6144)

    def test_init_KL6060bsi_photocell_size_axis1(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.photocell_size_axis1, 10e-6)

    def test_init_KL6060bsi_bin_axis1(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.bin_axis1, 1)

    def test_init_KL6060bsi_nb_photocell_axis2(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.nb_photocell_axis2, 6144)

    def test_init_KL6060bsi_photocell_size_axis2(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.photocell_size_axis2, 10e-6)

    def test_init_KL6060bsi_bin_axis2(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.bin_axis2, 1)

    def test_init_KL6060bsi_quantum_efficiency(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.quantum_efficiency, 0.85)

    def test_init_KL6060bsi_readout_noise(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.readout_noise, 4)

    def test_init_KL6060bsi_dark_currant(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.dark_currant, 0.6)

    def test_init_KL6060bsi_gain(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.gain, 7.3)

    def test_init_KL6060bsi_electron_multiplier(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.electron_multiplier, 1)

    # Test Get
    def test_get_l6060_sensor_type(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_sensor_type(), "CMOS")

    def test_get_l6060_nb_photocell_axis1(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_nb_photocell_axis1(), 6144)

    def test_get_KL6060bsi_photocell_size_axis1(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_photocell_size_axis1(), 10e-6)

    def test_get_KL6060bsi_bin_axis1(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_bin_axis1(), 1)

    def test_get_KL6060bsi_nb_photocell_axis2(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_nb_photocell_axis2(), 6144)

    def test_get_KL6060bsi_photocell_size_axis2(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_photocell_size_axis2(), 10e-6)

    def test_get_KL6060bsi_bin_axis2(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_bin_axis2(), 1)

    def test_get_KL6060bsi_quantum_efficiency(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_quantum_efficiency(), 0.85)

    def test_get_KL6060bsi_readout_noise(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_readout_noise(), 4)

    def test_get_KL6060bsi_dark_currant(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_dark_currant(), 0.6)

    def test_get_KL6060bsi_gain(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_gain(), 7.3)

    def test_get_KL6060bsi_electron_multiplier(self):
        camera = self.__setCamera("KL6060bsi")
        self.assertEqual(camera.get_electron_multiplier(), 1)

    def test_get_emccd_express_noise_factor(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_electron_multiplier(2)
        self.assertAlmostEqual(camera.get_emccd_express_noise_factor(), 1.503, 2)

    # Test set
    def test_set_Kl6060_sensor_type_1(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_sensor_type("CMOS")
        self.assertEqual(camera.get_sensor_type(), "CMOS")

    def test_set_Kl6060_sensor_type_2(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_sensor_type("TOTO")
        self.assertEqual(camera.get_sensor_type(), "CCD")

    def test_set_Kl6060_nb_photocell_axis1(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_nb_photocell_axis1(100)
        self.assertEqual(camera.get_nb_photocell_axis1(), 100)

    def test_set_KL6060bsi_photocell_size_axis1(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_photocell_size_axis1(1)
        self.assertEqual(camera.get_photocell_size_axis1(), 1)

    def test_set_KL6060bsi_bin_axis1(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_bin_axis1(3)
        self.assertEqual(camera.get_bin_axis1(), 3)

    def test_set_KL6060bsi_nb_photocell_axis2(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_nb_photocell_axis2(300)
        self.assertEqual(camera.get_nb_photocell_axis2(), 300)

    def test_set_KL6060bsi_nb_photocell_axis2_neg(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_nb_photocell_axis2(-300)
        self.assertEqual(camera.get_nb_photocell_axis2(), None)

    def test_set_KL6060bsi_photocell_size_axis2(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_photocell_size_axis2(5e-5)
        self.assertEqual(camera.get_photocell_size_axis2(), 5e-5)

    def test_set_KL6060bsi_bin_axis2(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_bin_axis2(5)
        self.assertEqual(camera.get_bin_axis2(), 5)

    def test_set_KL6060bsi_quantum_efficiency(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_quantum_efficiency(0.3)
        self.assertEqual(camera.get_quantum_efficiency(), 0.3)

    def test_set_KL6060bsi_quantum_efficiency_bad(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_quantum_efficiency(3)
        self.assertEqual(camera.get_quantum_efficiency(), None)

    def test_set_KL6060bsi_readout_noise(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_readout_noise(7)
        self.assertEqual(camera.get_readout_noise(), 7)

    def test_set_KL6060bsi_dark_currant(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_dark_currant(30)
        self.assertEqual(camera.get_dark_currant(), 30)

    def test_set_KL6060bsi_gain(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_gain(8.3)
        self.assertEqual(camera.get_gain(), 8.3)

    def test_set_KL6060bsi_electron_multiplier(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_electron_multiplier(4)
        self.assertEqual(camera.get_electron_multiplier(), 4)

    def test_set_pixel_size_axis1_1(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_bin_axis1(1)
        camera.set_pixel_size_axis1(3e-6)
        self.assertEqual(camera.get_pixel_size_axis1(), 3e-6)

    def test_set_pixel_size_axis1_2(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_bin_axis1(2)
        camera.set_pixel_size_axis1(6e-6)
        self.assertEqual(camera.get_photocell_size_axis1(), 3e-6)

    def test_set_pixel_size_axis2_1(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_bin_axis2(1)
        camera.set_pixel_size_axis2(3e-6)
        self.assertEqual(camera.get_pixel_size_axis2(), 3e-6)

    def test_set_pixel_size_axis2_2(self):
        camera = self.__setCamera("KL6060bsi")
        camera.set_bin_axis2(2)
        camera.set_pixel_size_axis2(6e-6)
        self.assertEqual(camera.get_photocell_size_axis2(), 3e-6)

    @staticmethod
    def __setCamera(name):
        conf_file = "imsim_conf_unitest.yml"
        conf_file = os.path.abspath(conf_file)
        setting = Settings(conf_file)
        return Camera(setting, name)


if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig('./conf/logging.conf')
    unittest.main()
