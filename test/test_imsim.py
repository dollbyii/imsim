import unittest
from imsim import Imsim
import os.path
from settings import Settings


class ImSimTest(unittest.TestCase):
    # Test init
    def test_init_name(self):
        imsim = self.__setImsim("V")
        self.assertEqual(imsim.name, None)

    def test_init_bad_name(self):
        imsim = self.__setImsim("aimsim")
        self.assertEqual(imsim.name, None)

    def test_init_version(self):
        imsim = self.__setImsim("V")
        self.assertEqual(imsim.get_version(), imsim.VERSION)

    # Test deffault value
    def test_init_setting_str(self):
        conf_file = "imsim_conf_unitest.yml"
        imsim = Imsim(conf_file, "myconfig1")

        conf_file = os.path.abspath(conf_file)
        setting = Settings(conf_file)
        self.assertEqual(imsim.observatory.name, setting.get_setting(['IMSIM', 'myconfig1', 'OBSERVATORY']))

    # Test deffault value
    def test_init_default_source(self):
        imsim = self.__setImsim("aimsim")
        self.assertEqual(imsim.source, None)

    def test_init_default_observatory(self):
        imsim = self.__setImsim("aimsim")
        self.assertEqual(imsim.observatory, None)

    def test_init_default_camera(self):
        imsim = self.__setImsim("aimsim")
        self.assertEqual(imsim.camera, None)

    def test_init_default_optic(self):
        imsim = self.__setImsim("aimsim")
        self.assertEqual(imsim.optic, None)

    def test_init_default_filter(self):
        imsim = self.__setImsim("aimsim")
        self.assertEqual(imsim.filter, None)

    # Test myconfig1 value
    def test_init_myconfig1_source(self):
        imsim = self.__setImsim("myconfig1")
        self.assertEqual(imsim.source.name, "vega")

    def test_init_myconfig1_observatory(self):
        imsim = self.__setImsim("myconfig1")
        self.assertEqual(imsim.observatory.name, "myobservatory")

    def test_init_myconfig1_camera(self):
        imsim = self.__setImsim("myconfig1")
        self.assertEqual(imsim.camera.name, "KL6060bsi")

    def test_init_myconfig1_optic(self):
        imsim = self.__setImsim("myconfig1")
        self.assertEqual(imsim.optic.name, "rifast800")

    def test_init_myconfig1_filter(self):
        imsim = self.__setImsim("myconfig1")
        self.assertEqual(imsim.filter.name, "C")

    # Test Get
    def test_get_myconfig1_source(self):
        imsim = self.__setImsim("myconfig1")
        self.assertEquals(imsim.get_source().get_name(), "vega")

    def test_get_myconfig1_observatory(self):
        imsim = self.__setImsim("myconfig1")
        self.assertEqual(imsim.get_observatory().get_name(), "myobservatory")

    def test_get_myconfig1_camera(self):
        imsim = self.__setImsim("myconfig1")
        self.assertEqual(imsim.get_camera().get_name(), "KL6060bsi")

    def test_get_myconfig1_optic(self):
        imsim = self.__setImsim("myconfig1")
        self.assertEqual(imsim.get_optic().get_name(), "rifast800")

    def test_get_myconfig1_filter(self):
        imsim = self.__setImsim("myconfig1")
        self.assertEqual(imsim.get_filter().get_name(), "C")

    # Test set
    def test_set_myconfig1_source(self):
        imsim = self.__setImsim("myconfig1")
        imsim.set_source("aldebaran")
        self.assertEquals(imsim.get_source().get_name(), "aldebaran")

    def test_set_myconfig1_source2(self):
        imsim = self.__setImsim("myconfig1")
        conf_file = "../conf/imsim_sources.yml"
        conf_file = os.path.abspath(conf_file)
        imsim.set_source("acrux", conf_file)
        self.assertEquals(imsim.get_source().get_name(), "acrux")

    def test_set_myconfig1_observatory(self):
        imsim = self.__setImsim("myconfig1")
        imsim.set_observatory("DEFAULT")
        self.assertEqual(imsim.get_observatory().get_name(), "DEFAULT")

    def test_set_myconfig1_camera(self):
        imsim = self.__setImsim("myconfig1")
        imsim.set_camera("mycamera")
        self.assertEqual(imsim.get_camera().get_name(), "mycamera")

    def test_set_myconfig1_optic(self):
        imsim = self.__setImsim("myconfig1")
        imsim.set_optic("rifast400")
        self.assertEqual(imsim.get_optic().get_name(), "rifast400")

    def test_set_myconfig1_filter(self):
        imsim = self.__setImsim("myconfig1")
        imsim.set_filter("B")
        self.assertEqual(imsim.get_filter().get_name(), "B")

    def test_set_default_exposure_time(self):
        imsim = self.__setImsim("myconfig1")
        exp = 15
        imsim.set_default_exposure_time(exp)
        self.assertEqual(imsim.default_exposure_time, exp)

    def test_get_default_exposure_time(self):
        imsim = self.__setImsim("myconfig1")
        exp = 15
        imsim.default_exposure_time = exp
        self.assertEqual(imsim.get_default_exposure_time(), exp)

    def test_set_default_snr(self):
        imsim = self.__setImsim("myconfig1")
        snr = 7
        imsim.set_default_snr(snr)
        self.assertEqual(imsim.default_snr, snr)

    def test_get_default_snr(self):
        imsim = self.__setImsim("myconfig1")
        snr = 15
        imsim.default_snr = snr
        self.assertEqual(imsim.get_default_snr(), snr)

    def test_set_oversampling(self):
        imsim = self.__setImsim("myconfig1")
        oversampling = 20
        imsim.set_oversampling(oversampling)
        self.assertEqual(imsim.fpix_oversampling, oversampling)

    def test_get_oversampling(self):
        imsim = self.__setImsim("myconfig1")
        oversampling = 20
        imsim.fpix_oversampling = oversampling
        self.assertEqual(imsim.get_oversampling(), oversampling)

    def test_set_fpix_x_factor(self):
        imsim = self.__setImsim("myconfig1")
        x_factor = 0.2
        imsim.set_fpix_x_factor(x_factor)
        self.assertEqual(imsim.fpix_x_factor, x_factor)

    def test_get_fpix_x_factor(self):
        imsim = self.__setImsim("myconfig1")
        x_factor = 20
        imsim.fpix_x_factor = x_factor
        self.assertEqual(imsim.get_fpix_x_factor(), x_factor)

    def test_set_fpix_y_factor(self):
        imsim = self.__setImsim("myconfig1")
        y_factor = 0.2
        imsim.set_fpix_y_factor(y_factor)
        self.assertEqual(imsim.fpix_y_factor, y_factor)

    def test_get_fpix_y_factor(self):
        imsim = self.__setImsim("myconfig1")
        y_factor = 20
        imsim.fpix_y_factor = y_factor
        self.assertEqual(imsim.get_fpix_y_factor(), y_factor)

    def test_snr_obj(self):
        imsim = self.__setImsim("myconfig1")
        t = 10
        magnitude = 20
        exp_snr = 4.4888
        snr = imsim.snr_obj(t, magnitude)
        self.assertAlmostEqual(exp_snr, snr, 4)

    def test_exposure_time_from_snr_mag(self):
        imsim = self.__setImsim("myconfig1")
        snr = 7
        magnitude = 20
        exp_t = 22.37527
        t = imsim.exposure_time_from_snr_mag(snr, magnitude)
        self.assertAlmostEqual(exp_t, t, 4)

    def test_exposure_time_from_snr_mag_bin_ccd(self):
        imsim = self.__setImsim("myconfig1")
        imsim.set_camera("myCCDbin2")
        snr = 7
        magnitude = 20
        exp_t = 11.77828
        t = imsim.exposure_time_from_snr_mag(snr, magnitude)
        self.assertAlmostEqual(exp_t, t, 4)

    def test_exposure_time_from_snr_mag_bin_cmos(self):
        imsim = self.__setImsim("myconfig1")
        imsim.set_camera("myCMOSbin2")
        snr = 7
        magnitude = 20
        exp_t = 16.72891
        t = imsim.exposure_time_from_snr_mag(snr, magnitude)
        self.assertAlmostEqual(exp_t, t, 4)

    def test_limit_mag_from_snr_exposure_time(self):
        imsim = self.__setImsim("myconfig1")
        snr = 7
        exp = 10
        exp_mag = 19.38501
        mag = imsim.limit_mag_from_snr_exposure_time(snr, exp)
        self.assertAlmostEqual(exp_mag, mag, 4)

    def test_limit_mag_from_snr_exposure_time_bin_ccd(self):
        imsim = self.__setImsim("myconfig1")
        imsim.set_camera("myCCDbin2")
        snr = 7
        exp = 10
        exp_mag = 19.89019
        mag = imsim.limit_mag_from_snr_exposure_time(snr, exp)
        self.assertAlmostEqual(exp_mag, mag, 4)

    def test_limit_mag_from_snr_exposure_time_bin_cmos(self):
        imsim = self.__setImsim("myconfig1")
        imsim.set_camera("myCMOSbin2")
        snr = 7
        exp = 10
        exp_mag = 19.56917
        mag = imsim.limit_mag_from_snr_exposure_time(snr, exp)
        self.assertAlmostEqual(exp_mag, mag, 4)

    @staticmethod
    def __setImsim(name):
        conf_file = "imsim_conf_unitest.yml"
        conf_file = os.path.abspath(conf_file)
        setting = Settings(conf_file)
        return Imsim(setting, name)


if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig('./conf/logging.conf')
    unittest.main()
