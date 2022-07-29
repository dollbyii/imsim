import math
import numbers
import numpy
from settings import Settings
from source import Source
from observatory import Observatory
from camera import Camera
from optic import Optic
from filter import Filter
import element


class Imsim(element.Element):
    """
        Imsim is the principal object
    """
    SETTING_PATH_ROOT = "IMSIM"
    SETTING_DEFAULT_NAME = "DEFAULT"
    VERSION = "1.0.0"

    def __init__(self, settings, name):
        """init for Imsim
            Args :
                setting (Settings) : setting for Imsim
                name (str) : name of the configuration in setting file
        """

        # Init
        self.str = "Imsim : "

        self.source = None
        self.observatory = None
        self.camera = None
        self.optic = None
        self.filter = None

        self.default_exposure_time = None  # exposure time (s)
        self.default_snr = None  # snr

        self.fpix_oversampling = 12
        self.fpix_x_factor = 0.5  # entre 0 (best case) 0.5 (worst case)
        self.fpix_y_factor = 0.5  # entre 0 (best case) 0.5 (worst case)

        self.jy_factor = 1.51e7

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
        return_val = True
        if not self.set_source(self._get_setting_val("SOURCE")):
            return_val = False
        if not self.set_observatory(self._get_setting_val("OBSERVATORY")):
            return_val = False
        if not self.set_camera(self._get_setting_val("CAMERA")):
            return_val = False
        if not self.set_optic(self._get_setting_val("OPTIC")):
            return_val = False
        if not self.set_filter(self._get_setting_val("FILTER")):
            return_val = False

        return return_val

    def __set_element(self, obj_var, obj_type, setting=None):
        """set_source set source value
            Args :
                source (source or str) : source or sournce name in setting file
                setting :
            Returns :
                obj_type : return the element to set
        """
        if isinstance(obj_var, obj_type):
            return obj_var
        elif isinstance(obj_var, str):
            setting = super()._get_setting_obj_from_param(setting)
            if setting is None:
                setting = self.local_setting

            return obj_type(setting, obj_var)
        self.logger.warning("Invalid argument source must be a source "
                            "object or the name of a configured source ".format(obj_var))
        return None

    def set_source2(self, source, setting=None):
        """set_source set source value
            Args :
                source (source or str) : source or sournce name in setting file
                setting :
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.source = None
        if isinstance(source, Source):
            self.source = source
            return True
        elif isinstance(source, str):
            setting = super()._get_setting_obj_from_param(setting)
            if setting is None:
                setting = self.local_setting

            self.source = Source(setting, source)
            if self.source.get_name() is None:
                return False
            return True
        self.logger.warning("Invalid argument source must be a source "
                            "object or the name of a configured source ".format(source))
        return False

    def set_source(self, source, setting=None):
        """set_source set source value
            Args :
                source (source or str) : source or source name in setting file
                setting :
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        if setting is None:
            setting = self.local_setting
        self.source = None
        if isinstance(source, Source):
            self.source = source
        else:
            self.source = Source(setting, source)
        if isinstance(self.source, Source):
            return True
        self.logger.warning("Invalid argument source must be a source "
                            "object or the name of a configured source ".format(source))
        return False

    def get_source(self):
        """get_source get source value
            Args :
            Returns :
                source (float) : return source value
        """
        return self.source

    def set_observatory(self, observatory):
        """set_observatory set observatory value
            Args :
                observatory (observatory or str) : value for observatory
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.observatory = None
        if isinstance(observatory, Observatory):
            self.observatory = observatory
            return True
        elif isinstance(observatory, str):
            self.observatory = Observatory(self.local_setting, observatory)
            if self.observatory.get_name() is None:
                return False
            return True

        self.logger.warning("Invalid argument observatory must be a observatory "
                            "object or the name of a configured observatory ".format(observatory))
        return False

    def get_observatory(self):
        """get_observatory get observatory value
            Args :
            Returns :
                observatory (float) : return observatory value
        """
        return self.observatory

    def set_camera(self, camera):
        """set_camera set camera value
            Args :
                camera (camera or str) : value for camera
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.camera = None
        if isinstance(camera, Camera):
            self.camera = camera
            return True
        elif isinstance(camera, str):
            self.camera = Camera(self.local_setting, camera)
            if self.camera.get_name() is None:
                return False
            return True

        self.logger.warning("Invalid argument camera must be a camera "
                            "object or the name of a configured camera ".format(camera))
        return False

    def get_camera(self):
        """get_camera get camera value
            Args :
            Returns :
                camera (float) : return camera value
        """
        return self.camera

    def set_optic(self, optic):
        """set_optic set optic value
            Args :
                optic (optic or str) : value for optic
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.optic = None
        if isinstance(optic, Optic):
            self.optic = optic
            return True
        elif isinstance(optic, str):
            self.optic = Optic(self.local_setting, optic)
            if self.optic.get_name() is None:
                return False
            return True

        self.logger.warning("Invalid argument optic must be a optic "
                            "object or the name of a configured optic ".format(optic))
        return False

    def get_optic(self):
        """get_optic get optic value
            Args :
            Returns :
                optic (float) : return optic value
        """
        return self.optic

    def set_filter(self, filter):
        """set_filter set filter value
            Args :
                filter (filter or str) : value for filter
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.filter = None
        if isinstance(filter, Filter):
            self.filter = filter
            return True
        elif isinstance(filter, str):
            self.filter = Filter(self.local_setting, filter)
            if self.filter.get_name() is None:
                return False
            return True

        self.logger.warning("Invalid argument filter must be a filter "
                            "object or the name of a configured filter ".format(filter))
        return False

    def get_filter(self):
        """get_filter get filter value
            Args :
            Returns :
                filter (float) : return filter value
        """
        return self.filter

    def set_default_exposure_time(self, exposure_time):
        """set_default_exposure_time set default_exposure_time value
            Args :
                default_exposure_time (filter or str) : value for default_exposure_time
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.default_exposure_time = None
        if isinstance(exposure_time, numbers.Number) and exposure_time > 0:
            self.default_exposure_time = exposure_time
            return True
        elif exposure_time is None:
            self.default_exposure_time = None
            return True

        self.logger.warning("Invalid argument exposure_time must be a exposure_time "
                            "object or the name of a configured exposure_time ".format(exposure_time))
        return False

    def get_default_exposure_time(self):
        """get_default_exposure_time get default_exposure_time value
            Args :
            Returns :
                default_exposure_time (float) : return default_exposure_time value
        """
        return self.default_exposure_time

    def set_default_snr(self, snr):
        """set_default_snr set snr value by default
            Args :
                snr (float) : value for snr
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.default_snr = None
        if isinstance(snr, numbers.Number) and snr > 0:
            self.default_snr = snr
            return True
        elif snr is None:
            self.default_snr = None
            return True

        self.logger.warning("Invalid argument exposure_time must be a exposure_time "
                            "object or the name of a configured exposure_time ".format(snr))
        return False

    def get_default_snr(self):
        """get_default_snr get snr value
            Args :
            Returns :
                snr (float) : return snr value
        """
        return self.default_snr

    def set_oversampling(self, oversampling):
        """set_oversampling set oversampling value
            Args :
                oversampling (number) : value for oversampling
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.fpix_oversampling = None
        if isinstance(oversampling, numbers.Number) and oversampling > 0:
            oversampling_min = 10
            if oversampling > oversampling_min:
                self.fpix_oversampling = oversampling
            else:
                self.fpix_oversampling = oversampling_min
            return True
        elif oversampling is None:
            self.fpix_oversampling = None
            return True

        self.logger.warning("Invalid argument oversampling, {} must be a number "
                            " > 10 ".format(oversampling))
        return False

    def get_oversampling(self):
        """get_oversampling get oversampling value
            Args :
            Returns :
                oversampling (float) : return oversampling value
        """
        return self.fpix_oversampling

    def set_fpix_x_factor(self, fpix_x_factor):
        """set_fpix_x_factor set fpix_x_factor value
            Args :
                fpix_x_factor (number) : value for fpix_x_factor
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.fpix_x_factor = None
        if isinstance(fpix_x_factor, numbers.Number) and fpix_x_factor > 0:
            fpix_x_factor_max = 0.5
            if fpix_x_factor > fpix_x_factor_max:
                self.fpix_x_factor = fpix_x_factor_max
            else:
                self.fpix_x_factor = fpix_x_factor
            return True
        elif fpix_x_factor is None:
            self.fpix_x_factor = None
            return True

        self.logger.warning("Invalid argument {} for fpix_y_factor "
                            "value must be between 0 (best case) and 0.5 (worst case) ".format(fpix_x_factor))
        return False

    def get_fpix_x_factor(self):
        """get_fpix_x_factor get fpix_x_factor value
            Args :
            Returns :
                fpix_x_factor (float) : return fpix_x_factor value
        """
        return self.fpix_x_factor

    def set_fpix_y_factor(self, fpix_y_factor):
        """set_fpix_y_factor set fpix_y_factor value
            Args :
                fpix_y_factor (number) : value for fpix_y_factor
            Returns :
                bool : The return value. True for success, False otherwise.
        """
        self.fpix_y_factor = None
        if isinstance(fpix_y_factor, numbers.Number) and fpix_y_factor > 0:
            fpix_y_factor_max = 0.5
            if fpix_y_factor > fpix_y_factor_max:
                self.fpix_y_factor = fpix_y_factor_max
            else:
                self.fpix_y_factor = fpix_y_factor
            return True
        elif fpix_y_factor is None:
            self.fpix_y_factor = None
            return True

        self.logger.warning("Invalid argument {} for fpix_y_factor "
                            "value must be between 0 (best case) and 0.5 (worst case) ".format(fpix_y_factor))
        return False

    def get_fpix_y_factor(self):
        """get_fpix_y_factor get fpix_y_factor value
            Args :
            Returns :
                fpix_y_factor (float) : return fpix_y_factor value
        """
        return self.fpix_y_factor

    # general function
    def __global_transmission(self):
        """global_transmission get global_transmission value
            Args :
            Returns :
                global_transmission (float) : return global_transmission value
        """
        return self.optic.get_transmission()*self.filter.get_transmission()

    def __pixel_solid_angle(self):
        """pixel_solid_angle get pixel_solid_angle value
            Args :
            Returns :
                pixel_solid_angle (float) : return pixel_solid_angle value
        """
        pixsize1 = self.camera.get_pixel_size_axis1()
        pixsize2 = self.camera.get_pixel_size_axis2()
        foclen = self.optic.get_focal_length()
        if pixsize1 is None or pixsize2 is None or foclen is None:
            return None
        cdelt1 = 2 * math.atan(pixsize1 / foclen / 2) * 180 * 3600 / math.pi
        cdelt2 = 2 * math.atan(pixsize2 / foclen / 2) * 180 * 3600 / math.pi

        return cdelt1 * cdelt2

    def __flux_fraction_brightest_pixel(self):
        """flux_fraction_brightest_pixel get flux_fraction_brightest_pixel value
            Args :
            Returns :
                flux_fraction_brightest_pixel (float) : return flux_fraction_brightest_pixel value
        """
        fwhm_psf_opt = self.optic.get_fwhm_psf_opt()
        seeing = self.observatory.get_seeing()
        foclen = self.optic.get_focal_length()
        pixsize1 = self.camera.get_pixel_size_axis1()
        pixsize2 = self.camera.get_pixel_size_axis2()

        fwhm_psf_seeing = seeing / 3600 * math.pi / 180 * foclen
        fwhm_psf = math.sqrt(fwhm_psf_opt ** 2 + fwhm_psf_seeing ** 2)
        if fwhm_psf is None or pixsize1 is None or pixsize2 is None:
            return None
        oversampling = self.get_oversampling()
        sigma = fwhm_psf/(2*math.sqrt(2*math.log(2)))
        sigma2 = sigma ** 2
        a1d = 1/sigma/math.sqrt(2*math.pi)
        a2d = a1d ** 2
        if pixsize1 >= pixsize2:
            p1 = pixsize2
            p2 = pixsize1
        else:
            p1 = pixsize1
            p2 = pixsize2
        dp = p1/oversampling
        som = 0
        x1 = -p1 * self.get_fpix_x_factor()
        y1 = -p2 * self.get_fpix_y_factor()
        x1max = x1 + p1 + dp
        y1max = y1 + p2 + dp
        for x in numpy.arange(x1, x1max, dp):
            dx2 = x ** 2
            for y in numpy.arange(y1, y1max, dp):
                dy2 = y ** 2
                d2 = dy2+dx2
                som = som + math.exp(-0.5*d2/sigma2)
        return som*a2d*dp ** 2

    # Object brightness
    def __object_brightness_ph(self, apparent_stellar_mag=None):
        """object_brightness_ph get brightness of the object in photon
            Args :
                p_m = None
            Returns :
                object_brightness_ph (float) : return object_brightness_ph value
        """
        fm0 = self.filter.get_flux_mag_zero()
        if apparent_stellar_mag is None:
            m = self.source.get_app_stellar_mag()
        else:
            m = apparent_stellar_mag
        di = self.filter.get_bandpass_width()
        i = self.filter.get_central_wavelength()
        if fm0 is None or m is None or di is None or i is None:
            return None
        f_jy = fm0 * 10 ** (-0.4 * m)
        return f_jy * self.jy_factor * di / i

    def __object_brightness_pixel_el(self, exposure_time=None, apparent_stellar_mag=None):
        """object_brightness_pixel_el get brightness of the object in electron on pixel (after passed through optic)
            Args :
            Returns :
                object_brightness_pixel_el (float) : return object_brightness_pixel_el value
        """
        f_ph = self.__object_brightness_ph(apparent_stellar_mag)
        d = self.optic.get_diameter()
        tatm = self.observatory.get_atmosphere_transmission_at_elevation()
        topt = self.__global_transmission()
        t = exposure_time
        if t is None:
            t = self.get_default_exposure_time()
        h = self.camera.get_quantum_efficiency()
        fpix = self.__flux_fraction_brightest_pixel()
        if f_ph is None or d is None or tatm is None or topt is None or t is None or h is None or fpix is None:
            return None
        ftot_ph = f_ph * math.pi * d ** 2 * tatm * topt * t / 4
        ftot_el = ftot_ph * h
        return ftot_el * fpix

    # Sky brightness
    def __sky_brightness_ph(self):
        """sky_brightness_ph get brightness of the sky in photon
                    Args :
                    Returns :
                        sky_brightness_ph (float) : return sky_brightness_ph value
                """
        fm0 = self.filter.get_flux_mag_zero()
        msky = self.observatory.get_sky_brightness()
        di = self.filter.get_bandpass_width()
        i = self.filter.get_central_wavelength()
        if fm0 is None or msky is None or di is None or i is None:
            return None
        sky_jy = fm0 * 10 ** (-0.4 * msky)

        return sky_jy * self.jy_factor * di / i

    def __sky_brightness_pixel_el(self, exposure_time=None):
        """sky_brightness_pixel_el get brightness of the sky in electron on pixel (after passed through optic)
                    Args :
                    Returns :
                        sky_brightness_pixel_el (float) : return sky_brightness_pixel_el value
                """
        sky_ph = self.__sky_brightness_ph()
        d = self.optic.get_diameter()
        w = self.__pixel_solid_angle()
        topt = self.__global_transmission()
        t = exposure_time
        if t is None:
            t = self.get_default_exposure_time()
        h = self.camera.get_quantum_efficiency()
        if sky_ph is None or d is None or w is None or topt is None or t is None or h is None:
            return None
        skypix_ph = sky_ph * math.pi * d ** 2 * w * topt * t / 4
        return skypix_ph * h

    def snr_obj(self, exposure_time=None, apparent_stellar_mag=None):
        """snr_obj get snr_obj value
            Args :
            Returns :
                snr_obj (float) : return snr_obj value
        """
        c_th = self.camera.get_dark_currant()
        bin1 = self.camera.get_bin_axis1()
        bin2 = self.camera.get_bin_axis2()
        t = exposure_time
        if t is None:
            t = self.get_default_exposure_time()
        fex = self.camera.get_emccd_express_noise_factor()
        em = self.camera.get_electron_multiplier()
        skypix_el = self.__sky_brightness_pixel_el(t)
        fpix_el = self.__object_brightness_pixel_el(t, apparent_stellar_mag)
        n_ro = self.camera.get_pixel_readout_noise()
        if all(x is None for x in [c_th, bin1, bin2, t, fex, em, skypix_el, fpix_el, n_ro]):
            return None

        n_th = math.sqrt(c_th * bin1 * bin2 * t * fex) * em
        n_sk = math.sqrt(skypix_el * fex) * em
        n_ph = math.sqrt(fpix_el * fex) * em

        n_tot = math.sqrt(n_ro ** 2 + n_th ** 2 + n_sk ** 2 + n_ph ** 2)

        return fpix_el / n_tot

    def exposure_time_from_snr_mag(self, snr=None, apparent_stellar_mag=None):
        """exposure_time_from_snr_mag get optimum exposure time for a given snr and apparent magnitude
            Args :
                snr (float) : signal noise ratio
                magnitude (float) : apparent magnitude
            Returns :
                exposure_time (float) : return exposure_time value
        """
        f_ph = self.__object_brightness_ph(apparent_stellar_mag)

        n_ro = self.camera.get_pixel_readout_noise()
        c_th = self.camera.get_pixel_dark_currant()
        # bin1 = self.camera.get_bin_axis1()
        # bin2 = self.camera.get_bin_axis2()
        fex = self.camera.get_emccd_express_noise_factor()
        em = self.camera.get_electron_multiplier()
        sky_ph = self.__sky_brightness_ph()
        w = self.__pixel_solid_angle()
        topt = self.__global_transmission()
        d = self.optic.get_diameter()
        tatm = self.observatory.get_atmosphere_transmission_at_elevation()
        h = self.camera.get_quantum_efficiency()
        fpix = self.__flux_fraction_brightest_pixel()

        if all(x is None for x in [c_th, fex, em, n_ro, sky_ph, w, topt, f_ph, d, tatm, h, fpix]):
            return None

        if snr is None or not isinstance(snr, numbers.Number) or snr <= 0:
            return None
        c = snr ** 2 * n_ro ** 2
        b = snr ** 2 * ((c_th * fex * em ** 2) +
                       (sky_ph * math.pi * d ** 2 / 4 * w * topt * h * fex * em ** 2) +
                       (f_ph * math.pi * d ** 2 / 4 * tatm * topt * h * fpix * fex * em ** 2))
        a = -(f_ph * math.pi * d ** 2 / 4 * tatm * topt * h * fpix * em) ** 2
        d = b * b - 4 * a * c

        return (- b - math.sqrt(d))/(2 * a)

    def limit_mag_from_snr_exposure_time(self, snr, exposure_time=None):
        """limit_mag_from_snr_exposure_time get limit apparent magnitude for a given snr and exposure time
            Args :
                snr (float) : signal noise ratio
                exposure_time (float) : exposure_time
            Returns :
                limit_magnitude (float) : return limit_magnitude value
        """
        t = exposure_time
        if t is None:
            t = self.get_default_exposure_time()
        n_ro = self.camera.get_pixel_readout_noise()
        c_th = self.camera.get_dark_currant()
        bin1 = self.camera.get_bin_axis1()
        bin2 = self.camera.get_bin_axis2()
        fex = self.camera.get_emccd_express_noise_factor()
        em = self.camera.get_electron_multiplier()
        sky_ph = self.__sky_brightness_ph()
        w = self.__pixel_solid_angle()
        topt = self.__global_transmission()
        d = self.optic.get_diameter()
        tatm = self.observatory.get_atmosphere_transmission_at_elevation()
        h = self.camera.get_quantum_efficiency()
        fpix = self.__flux_fraction_brightest_pixel()
        di = self.filter.get_bandpass_width()
        i = self.filter.get_central_wavelength()
        fm0 = self.filter.get_flux_mag_zero()

        if all(x is None for x in [c_th, bin1, bin2, fex, em, n_ro, sky_ph, w, topt, d, tatm, h, fpix, di, i, fm0]):
            return None

        c = snr ** 2 * (n_ro ** 2 + (c_th * bin1 * bin2 * fex * em ** 2 * t) +
                        (sky_ph * math.pi * d ** 2 / 4 * w * topt * h * fex * em ** 2 * t))
        b = snr ** 2 * (math.pi * d ** 2 / 4 * tatm * topt * h * fpix * fex * em ** 2 * t)
        a = -(math.pi * d ** 2 / 4 * tatm * topt * h * fpix * em * t) ** 2
        d = b ** 2 - 4 * a * c

        f_ph = (-b - math.sqrt(d)) / (2 * a)
        f_jy = f_ph / (self.jy_factor * di / i)

        return -2.5 * math.log10(f_jy / fm0)
